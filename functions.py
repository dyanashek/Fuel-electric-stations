import requests
import sqlite3
import inspect
import logging
import time
import math
import numpy

from python_whatsapp_bot import Whatsapp
from python_whatsapp_bot import Inline_button
from typing import List

import classes
import utils
import config


def is_in_database(id):
    '''Checks if id already in database. Returns empty list if it isn't and full info if it is.'''

    database = sqlite3.connect("energy.db")
    cursor = database.cursor()

    fuel_station = cursor.execute(f"SELECT * FROM fuel_stations WHERE unique_id=?", (id,)).fetchall()

    cursor.close()
    database.close()

    if fuel_station:
        fuel_station = fuel_station[0]
    
    return fuel_station


def add_station(fuel_station: classes.FuelStation):
    '''Adds information about new station.'''

    database = sqlite3.connect("energy.db")
    cursor = database.cursor()

    try:
        cursor.execute(f'''
                INSERT INTO fuel_stations (unique_id, manager, brand, name, address, province, lat, long)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', 
                (fuel_station.id, fuel_station.manager, fuel_station.brand, 
                 fuel_station.name, fuel_station.address, fuel_station.province,
                 fuel_station.lat, fuel_station.long,)
                )
        database.commit()

    except Exception as ex:
        logging.error(f'{inspect.currentframe().f_code.co_name}: Не удалось добавить данные: {ex}.')
    
    cursor.close()
    database.close()


def update_station(fuel_station: classes.FuelStation):
    '''Updates information about station.'''

    database = sqlite3.connect("energy.db")
    cursor = database.cursor()

    try:
        cursor.execute(f'''UPDATE fuel_stations
                        SET manager=?, brand=?, name=?,
                        address=?, province=?, lat=?, long=?,
                        updated=1
                        WHERE unique_id=?
                        ''',
                        (fuel_station.manager, fuel_station.brand, 
                         fuel_station.name, fuel_station.address, fuel_station.province,
                         fuel_station.lat, fuel_station.long, fuel_station.id,)
                        )
        database.commit()

    except Exception as ex:
        logging.error(f'{inspect.currentframe().f_code.co_name}: Не удалось обновить данные: {ex}.')
    
    cursor.close()
    database.close()


def drop_update_status():
    '''Sets update status to False for all fuel stations.'''

    database = sqlite3.connect("energy.db")
    cursor = database.cursor()

    cursor.execute("UPDATE fuel_stations SET updated=0")

    database.commit()
    cursor.close()
    database.close()


def delete_outdated_stations():
    '''Deletes stations that were outdated.'''

    database = sqlite3.connect("energy.db")
    cursor = database.cursor()

    cursor.execute("DELETE FROM fuel_stations WHERE updated=0")

    database.commit()
    cursor.close()
    database.close()


def get_fuel_stations_info():
    '''Gets information about fuel station, converts in to a string.'''

    response = requests.get(url='https://www.mimit.gov.it/images/exportCSV/anagrafica_impianti_attivi.csv')

    if response.status_code == 200:
        return str(response.content)
    
    return False


def handle_fuel_station_info(stations_info):
    '''Extracts information about fuel station and adds it to database.'''

    if stations_info:
        stations_info = stations_info.split('\\n')

        for station_info in stations_info:
            fuel_station = utils.validate_station_info(station_info)

            if fuel_station:
                fuel_station = classes.FuelStation(fuel_station)

                in_database = is_in_database(fuel_station.id)

                if in_database:
                    update_station(fuel_station)

                else:
                    add_station(fuel_station)


def get_prices_info():
    '''Gets information about prices, converts in to a string.'''

    response = requests.get(url='https://www.mimit.gov.it/images/exportCSV/prezzo_alle_8.csv')

    if response.status_code == 200:
        return str(response.content)
    
    return False


def update_price(price_info: classes.PriceInfo):
    '''Updates price on current fuel station.'''

    database = sqlite3.connect("energy.db")
    cursor = database.cursor()

    try:
        cursor.execute(f'''UPDATE fuel_stations
                        SET {price_info.field}=?
                        WHERE unique_id=?
                        ''',
                        (price_info.price, price_info.id,)
                        )
        database.commit()

    except Exception as ex:
        logging.error(f'{inspect.currentframe().f_code.co_name}: Не удалось обновить данные по цене: {ex}.')
    
    cursor.close()
    database.close()


def handle_prices_info(prices_info):
    '''Extracts information about prices and adds it to database.'''

    if prices_info:
        prices_info = prices_info.split('\\n')

        for price_info in prices_info:
            price_info = utils.validate_price_info(price_info)

            if price_info:
                price_info = classes.PriceInfo(price_info)

                update_price(price_info)


def update_database():
    '''Keeps the database up to date.'''

    while True:
        handle_fuel_station_info(get_fuel_stations_info())
        handle_prices_info(get_prices_info())

        delete_outdated_stations()
        drop_update_status()

        time.sleep(86400)


def is_new_user(user_number):
    '''Checks if user already in database. Return an empty list if he isn't.'''

    database = sqlite3.connect("energy.db")
    cursor = database.cursor()

    user_info = cursor.execute(f"SELECT * FROM users WHERE number={user_number}").fetchall()

    cursor.close()
    database.close()

    if user_info:
        user_info = user_info[0]

    return user_info


def add_new_user(user_number):
    '''Adds new users phone number to database.'''

    database = sqlite3.connect("energy.db")
    cursor = database.cursor()

    cursor.execute(f"INSERT INTO users (number) VALUES ('{user_number}')")

    database.commit()
    cursor.close()
    database.close()


def set_language(user_number, language):
    '''Sets language for user.'''

    database = sqlite3.connect("energy.db")
    cursor = database.cursor()

    cursor.execute(f"UPDATE users SET language='{language}' WHERE number='{user_number}'")

    database.commit()
    cursor.close()
    database.close()


def set_fuel_type(user_number, fuel_type):
    '''Sets fuel type for user.'''

    database = sqlite3.connect("energy.db")
    cursor = database.cursor()

    cursor.execute(f"UPDATE users SET fuel='{fuel_type}' WHERE number='{user_number}'")

    database.commit()
    cursor.close()
    database.close()


def get_electric_charges(lat, lon, connector_id):
    '''Gets electric charges based on location.'''

    params = {
        'key' : config.KEY_ELECTRIC,
        'latitude' : lat,
        'longitude' : lon,
        'distance' : config.ELECTRIC_RADIUS,
        'maxresults' : 100,
        'connectiontypeid' : [connector_id],
        'statustypeid' : [10, 20, 50, 75],
        'usagetypeid' : [1, 4, 5, 7]
    }

    electric_charges = requests.get(url=config.URL_ELECTRIC, params=params).json()

    return electric_charges


def get_cheapest_electric_charges(electric_charges, connector_id):
    '''Gets three cheapest charges located nearby.'''

    charges = []

    for charge in electric_charges:
        charges.append(classes.Charger(charge, connector_id))
    
    length = len(charges)

    if length >= 3:
        length = 3

    try:    
        charges = sorted(charges, key=lambda x: x.price)[0:length]
    except:
        charges = []

    return charges


def construct_chargers_buttons_text(charges: List[classes.Charger], language, fuel):
    '''Constructs buttons and text with cheapest charges.'''

    buttons = []
    text = ''
    for num, charger in enumerate(charges):
        name = charger.address
        if len(charger.address) > 17:
            name = f'{num + 1}. {charger.address[0:14]}...'
        else:
            name = f'{num + 1}. {charger.address}'

        buttons.append(
            Inline_button(
                text=name,
                button_id=
                f'station_{charger.name}_{charger.address}_{charger.lat}_{charger.lon}_{language}_{num}'
            ))

        if language == 'English':
            price = charger.price
            if price == '':
                price = config.PRICE_ENG

            text += f'*{num + 1}. {charger.address}*\n{charger.operator}\n*Price:* {price}\n*Distance:* {charger.distance} km\n*Connector:* {fuel}\n*Power:* {charger.power_eng} kW\n\n'

        elif language == 'Italiana':

            price = charger.price
            if price == '':
                price = config.PRICE_ITA

            text += f'*{num + 1}. {charger.address}*\n{charger.operator}\n*Prezzo:* {price}\n*Distanza:* {charger.distance} km\n*Connettore:* {fuel}\n*Potenza:* {charger.power_ita} kW\n\n'

    text = text.rstrip('\n\n\n')

    return buttons, text


def get_province(lat, lon):
    '''Indicates province of request.'''

    try:
        response = requests.get(f"https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={lat}&lon={lon}")
    except:
        return 'connection error'

    province = response.json().get('address').get('ISO3166-2-lvl6')
    country = response.json().get('address').get('country')

    if country == 'Italia':

        if province is None:
            province = response.json().get('address').get('ISO3166-2-lvl4')

            if province == 'IT-23':
                province = 'AO'

            elif province == 'IT-88':
                province = 'SS'

            else:
                return False
            
        else:
            province = province.replace('IT-', '')
    
    else:
        return False
    
    if province not in config.PROVINCES:
        return False

    return province


def get_province_stations(province, fuel):
    '''Gets all station of province.'''

    field = config.fuel_field[fuel]

    database = sqlite3.connect("energy.db")
    cursor = database.cursor()

    stations = cursor.execute(f'''SELECT brand, name, address, lat, long, {field}_self, {field}_service
                                FROM fuel_stations 
                                WHERE province="{province}" 
                                AND ({field}_self is not Null 
                                OR {field}_service is not Null)'''
                              ).fetchall()

    cursor.close()
    database.close()

    return stations


def get_cheapest_stations(stations, lat, lon):
    '''Indicates cheapest stations nearby.'''

    final_stations = []

    for station in stations:
        station = classes.CheapestStation(station)
        distance = 2 * 6371 * math.asin(
            math.sqrt(math.sin((math.radians(station.lat) - math.radians(lat)) / 2)**2 + 
                      math.cos(math.radians(lat)) * math.cos(math.radians(station.lat)) * 
                      math.sin((math.radians(station.lon) - math.radians(lon)) / 2)**2))
        
        if distance <= config.RADIUS:
            station.distance = numpy.round(distance, 2)
            final_stations.append(station)
    
    if final_stations != []:
        length = len(final_stations)
        if length >= 3:
            length = 3

        final_stations = sorted(final_stations, key=lambda x: x.find_minimum())[0:length]
        
    return final_stations


def construct_stations_buttons_text(final_stations: List[classes.CheapestStation], language, fuel):
    buttons = []
    text = ''
    for num, station in enumerate(final_stations):
        brand = station.brand

        if len(station.brand) > 17:
            brand = f'{num + 1}. {station.brand[0:14]}...'
        else:
            brand = f'{num + 1}. {station.brand}'

        buttons.append(
            Inline_button(
                text=brand,
                button_id=
                f'station_{station.brand}_{station.name}_{station.lat}_{station.lon}_{language}_{num}'
            ))
        
        price_self_eng = f'{station.price_self} €'
        price_self_ita = f'{station.price_self} €'

        if station.price_self is None:
            price_self_eng = 'not defined'
            price_self_ita = 'non definito'
        
        price_service_eng = f'{station.price_service} €'
        price_service_ita = f'{station.price_service} €'

        if station.price_service is None:
            price_service_eng = 'not defined'
            price_service_ita = 'non definito'


        if language == 'English':
            text += f'{num + 1}. {station.brand}\n*{station.address}*\n*Price* ({fuel}):\n*Self-service:* {price_self_eng}\n*Service:* {price_service_eng}\n*Distance:* {station.distance} km\n\n'

        elif language == 'Italiana':
            text += f'{num + 1}. {station.brand}\n*{station.address}*\n*Prezzo* ({fuel}):\n*Self-service:* {price_self_ita}\n*Servito:* {price_service_ita}\n*Distanza:* {station.distance} km\n\n'

    text = text.rstrip('\n\n\n')

    return buttons, text