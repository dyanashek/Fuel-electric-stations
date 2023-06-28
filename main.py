import threading
from python_whatsapp_bot import Whatsapp
from python_whatsapp_bot import Inline_keyboard
from flask import Flask, request

import config
import utils
import functions
import messages_requests

app = Flask(__name__)

bot = Whatsapp(config.PHONE_ID, config.FB_TOKEN)

threading.Thread(daemon=True, target=functions.update_database).start()

@app.route('/', methods=['GET'])
def handle_get_requests():
    # Verify token endpoint
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    

def verify_fb_token(token_sent):
    if token_sent == config.VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


@app.route('/', methods=['POST'])
def handle_posts_requests():
    output = request.get_json()

    message_type = utils.extract_message_type(output)
    user_number = utils.extract_phone_number(output)

    # processing all types of messages from users
    if message_type != 0 and user_number != 0:
        user_info = functions.is_new_user(user_number)
    
        # if user already in DB
        if user_info:

            # and we got a message with type 'interactive'
            if message_type == 'interactive':
                message_button, title_button = utils.extract_button_info(output)

                # user choose english
                if message_button == config.ENG_BUTTON:
                    functions.set_language(user_number, config.ENG_BUTTON)
                    messages_requests.send_message(messages_requests.energy_eng(user_number))
                    
                # user choose italian
                elif message_button == config.ITA_BUTTON:
                    functions.set_language(user_number, config.ITA_BUTTON)
                    messages_requests.send_message(messages_requests.energy_ita(user_number))

                # user choose 'gas' - primary type
                elif 'gas' in message_button:

                    if 'eng' in message_button:
                        messages_requests.send_message(messages_requests.gas_eng(user_number))

                    elif 'ita' in message_button:
                        messages_requests.send_message(messages_requests.gas_ita(user_number))
                
                # user choose 'electric' - primary type
                elif 'electric' in message_button:

                    if 'eng' in message_button:
                        messages_requests.send_message(messages_requests.electric_eng(user_number))

                    elif 'ita' in message_button:
                        messages_requests.send_message(messages_requests.electric_ita(user_number))

                # user choose final type of fuel
                elif 'ffuel' in message_button:
                    functions.set_fuel_type(user_number, title_button)

                    if 'eng' in message_button:
                        messages_requests.settings_send_eng(user_number, title_button)

                    elif 'ita' in message_button:
                        messages_requests.settings_send_ita(user_number, title_button)
                
                # sends chargers or stations location
                elif 'station' in message_button:
                    info = message_button.split('_')
                    final_name = info[2]
                    final_lat = info[3]
                    final_lon = info[4]
                    final_lang = info[5]

                    messages_requests.send_message(messages_requests.location_params(
                        user_number,
                        final_lat,
                        final_lon,
                        final_name,
                        final_lang,
                    )
                    )

                # user wants to change fuel type
                elif message_button == config.CHANGE_FUEL_BUTTON_ENG:
                    messages_requests.send_message(messages_requests.energy_eng(user_number))

                elif message_button == config.CHANGE_FUEL_BUTTON_ITA:
                    messages_requests.send_message(messages_requests.energy_ita(user_number))

                # user wants to change language
                elif message_button == config.CHANGE_LANG_BUTTON_ENG or message_button == config.CHANGE_LANG_BUTTON_ITA:
                        
                        try:
                            bot.send_message(user_number,
                                                             config.CHOOSE_LANG,
                                                             reply_markup=Inline_keyboard(
                                                                 [config.ENG_BUTTON, config.ITA_BUTTON]))
                        except:
                            pass
            
            # gets different type of message:
            else:
                # if there are some undefined fields
                if None in user_info:
                    language = user_info[2]

                    if language is None:
                        try:
                            bot.send_message(user_number,
                                            config.CHOOSE_LANG,
                                            reply_markup=Inline_keyboard([
                                                    config.ENG_BUTTON, 
                                                    config.ITA_BUTTON,
                                                    ]
                                                    ),
                                            )
                        except:
                            pass
                    
                    else:
                        if language == 'English':
                            messages_requests.send_message(messages_requests.energy_eng(user_number))

                        elif language == 'Italiana':
                            messages_requests.send_message(messages_requests.energy_ita(user_number))
                
                # if all fields are defined
                else:
                    language = user_info[2]
                    fuel = user_info[3]

                    # if the message type is location
                    if message_type == 'location':
                        lat, lon = utils.extract_coords(output)

                        # extracted coordinates
                        if lat and lon:

                            # not electric energy
                            if fuel not in config.connection_types:
                                province = functions.get_province(lat, lon)

                                # if its not possible to get connect to location API
                                if province == 'connection error':
                                    if language == 'English':
                                        try:
                                            bot.send_message(user_number, config.CONNECTION_LOC_ERROR_ENG)
                                        except:
                                            pass

                                    elif language == 'Italiana':
                                        try:
                                            bot.send_message(user_number, config.CONNECTION_LOC_ERROR_ITA)
                                        except:
                                            pass
                                
                                # detected province
                                elif province:
                                    fuel_stations = functions.get_province_stations(province, fuel)
                                    cheapest_stations = functions.get_cheapest_stations(fuel_stations, lat, lon)

                                    # there are some stations around
                                    if cheapest_stations:
                                        buttons, text = functions.construct_stations_buttons_text(
                                            cheapest_stations, 
                                            language, 
                                            fuel,
                                            )
                                        
                                        try:
                                            bot.send_message(
                                                user_number,
                                                text,
                                                reply_markup=Inline_keyboard(buttons),
                                                )
                                        except:
                                            pass

                                    # there are not any stations
                                    else:
                                        if language == 'English':
                                            try:
                                                settings = config.NO_STATIONS_ENG
                                                footer = config.FOOTER_FUEL_ENG
                                                if fuel in config.connection_types:
                                                    settings = config.NO_CHARGERS_ENG
                                                    footer = config.FOOTER_ELECTRIC_ENG

                                                bot.send_message(
                                                    user_number,
                                                    settings,
                                                    reply_markup=Inline_keyboard(
                                                        [config.CHANGE_FUEL_BUTTON_ENG]),
                                                    footer=f'{footer} {fuel}'
                                                )
                                            except:
                                                pass

                                        elif language == 'Italiana':
                                            try:
                                                settings = config.NO_STATIONS_ITA
                                                footer = config.FOOTER_FUEL_ITA
                                                if fuel in config.connection_types:
                                                    settings = config.NO_CHARGERS_ITA
                                                    footer = config.FOOTER_ELECTRIC_ITA

                                                bot.send_message(
                                                    user_number,
                                                    settings,
                                                    reply_markup=Inline_keyboard(
                                                        [config.CHANGE_FUEL_BUTTON_ITA]),
                                                    footer=f'{footer} {fuel}'
                                                )
                                            except:
                                                pass

                                # location out of Italy
                                else:
                                    if language == 'English':
                                        try:
                                            bot.send_message(user_number, config.LOCATION_ERROR_ENG)
                                        except:
                                            pass

                                    elif language == 'Italiana':
                                        try:
                                            bot.send_message(user_number, config.LOCATION_ERROR_ITA)
                                        except:
                                            pass

                            # electric energy
                            else:
                                connector_id = config.connection_types[fuel]

                                electric_charges = functions.get_electric_charges(lat, lon, connector_id)
                                cheapest_charges = functions.get_cheapest_electric_charges(electric_charges, connector_id)

                                # there are charges around
                                if cheapest_charges != []:
                                    buttons, text = functions.construct_chargers_buttons_text(
                                        cheapest_charges, 
                                        language,
                                        fuel,
                                        )
                                    
                                    try:
                                        bot.send_message(
                                            user_number,
                                            text,
                                            reply_markup=Inline_keyboard(buttons))
                                    except:
                                        pass
                                
                                # no charges found
                                else:
                                    if language == 'English':
                                        try:
                                            settings = config.NO_STATIONS_ENG
                                            footer = config.FOOTER_FUEL_ENG

                                            if fuel in config.connection_types:
                                                settings = config.NO_CHARGERS_ENG
                                                footer = config.FOOTER_ELECTRIC_ENG

                                            bot.send_message(
                                                user_number,
                                                settings,
                                                reply_markup=Inline_keyboard([config.CHANGE_FUEL_BUTTON_ENG]),
                                                footer=f'{footer} {fuel}',
                                            )

                                        except:
                                            pass

                                    elif language == 'Italiana':
                                        try:
                                            settings = config.NO_STATIONS_ITA
                                            footer = config.FOOTER_FUEL_ITA

                                            if fuel in config.connection_types:
                                                settings = config.NO_CHARGERS_ITA
                                                footer = config.FOOTER_ELECTRIC_ITA

                                            bot.send_message(
                                                user_number,
                                                settings,
                                                reply_markup=Inline_keyboard([config.CHANGE_FUEL_BUTTON_ITA]),
                                                footer=f'{footer} {fuel}'
                                            )
                                        except:
                                            pass
                        
                        # failed to extract coordinates                  
                        else:
                            if language == 'English':
                                try:
                                    bot.send_message(user_number, config.DATA_ERROR_ENG)
                                except:
                                    pass

                            elif language == 'Italiana':
                                try:
                                    bot.send_message(user_number, config.DATA_ERROR_ITA)
                                except:
                                    pass
                    
                    # the message type is different from location
                    else:
                        if language == 'English':
                            try:
                                settings = config.SETTINGS_SAVED_ENG
                                footer = config.FOOTER_FUEL_ENG

                                if fuel in config.connection_types:
                                    settings = config.ELECTRIC_SETTINGS_SAVED_ENG
                                    footer = config.FOOTER_ELECTRIC_ENG

                                bot.send_message(
                                    user_number,
                                    settings,
                                    reply_markup=Inline_keyboard([
                                        config.CHANGE_FUEL_BUTTON_ENG,
                                        config.CHANGE_LANG_BUTTON_ITA
                                    ]),
                                    header=config.SETTINGS_HEADER_ENG,
                                    header_type='text',
                                    footer=f'{footer} {fuel}\n{config.FOOTER_LANG_ENG} {language}',
                                )

                            except:
                                pass

                        elif language == 'Italiana':
                            try:
                                settings = config.SETTINGS_SAVED_ITA
                                footer = config.FOOTER_FUEL_ITA

                                if fuel in config.connection_types:
                                    settings = config.ELECTRIC_SETTINGS_SAVED_ITA
                                    footer = config.FOOTER_ELECTRIC_ITA

                                bot.send_message(
                                    user_number,
                                    settings,
                                    reply_markup=Inline_keyboard([
                                        config.CHANGE_FUEL_BUTTON_ITA,
                                        config.CHANGE_LANG_BUTTON_ENG
                                    ]),
                                    header=config.SETTINGS_HEADER_ITA,
                                    header_type='text',
                                    footer=f'{footer} {fuel}\n{config.FOOTER_LANG_ITA} {language}',
                                )

                            except:
                                pass
        
        # a new user
        else:
            functions.add_new_user(user_number)

            try:
                bot.send_message(user_number,
                                config.START_MESSAGE,
                                reply_markup=Inline_keyboard([config.ENG_BUTTON, config.ITA_BUTTON]),
                                header=config.START_HEADER,
                                header_type='text',
                                footer=config.START_FOOTER)

            except:
                pass
    
    return "Message Processed"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)