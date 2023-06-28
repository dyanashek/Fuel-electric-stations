import config

class FuelStation:

    def __init__(self, station_info):
        self.id = int(station_info[0])
        self.manager = station_info[1].strip(' ')
        self.brand = station_info[2].strip(' ')
        self.name = station_info[4].strip(' ')
        self.address = station_info[5].strip(' ')
        self.province = station_info[7].replace(' ', '')
        self.lat = float(station_info[8])
        self.long = float(station_info[9])


class CheapestStation:

    def __init__(self, station_info):
        self.brand = station_info[0]

        self.name = station_info[1]
        if self.name == '':
            self.name = station_info[2]

        self.address = station_info[2]

        self.lat = station_info[3]
        self.lon = station_info[4]
        self.price_self = station_info[5]
        self.price_service = station_info[6]
        self.distance = 0

    def find_minimum(self):
        price_self = self.price_self
        if price_self is None:
            price_self = 10000
        
        price_service = self.price_service
        if price_service is None:
            price_service = 10000

        return min(price_self, price_service)


class PriceInfo:

    def __init__(self, price_info):
        self.id = int(price_info[0])
        self.type = price_info[1]
        self.price = float(price_info[2])

        if int(price_info[3]) == 0:
            self.action = 'service'
        else:
            self.action = 'self'

        self.field = f'{config.fuel_types[self.type.upper()]}_{self.action}'


class Charger:

    def __init__(self, data, id):
        try:
            self.address = data.get('AddressInfo').get('AddressLine1').strip(' ')
        except:
            self.address = 'Not defined'

        self.lat = float(data.get('AddressInfo').get('Latitude'))
        self.lon = float(data.get('AddressInfo').get('Longitude'))
        self.distance = round(float(data.get('AddressInfo').get('Distance')), 2)

        try:
            self.name = data.get('AddressInfo').get('Title').strip(' ')
        except:
            self.name = 'Not defined'

        if data.get('UsageCost') is None:
            self.price = ''
        else:
            self.price = data.get('UsageCost').strip(' ').replace(',', '.').replace('€', ' €')

        try:
            self.operator = data.get('OperatorInfo').get('Title').strip(' ')
        except:
            self.operator = 'Not defined'

        connections = data.get('Connections')

        self.power_eng = 'undefined'
        self.power_ita = 'non definito'

        for connection in connections:
            if connection.get('ConnectionTypeID') == id:
                if connection.get('PowerKW') is not None:
                    self.power_eng = self.power_ita = int(connection.get('PowerKW'))
                    break


# class FuelStation:
#     def __init__(self, id, manager, brand, name, address, province, lat, long):
#         self.id = id
#         self.manager = manager
#         self.brand = brand
#         self.name = name
#         self.address = address
#         self.province = province
#         self.lat = lat
#         self.long = long
        