import config

def validate_station_info(fuel_station: str):
    '''Validates if information about fuel station can be interpreted.'''

    fuel_station = fuel_station.split(';')

    if len(fuel_station) != 10:
        return False
    
    try:
        int(fuel_station[0])
        float(fuel_station[8])
        float(fuel_station[9])
    except:
        return False
    
    return fuel_station


def validate_price_info(price_info: str):
    '''Validates if information about prices can be interpreted.'''

    price_info = price_info.split(';')

    if len(price_info) != 5:
        return False
    
    try:
        int(price_info[0])
        float(price_info[2])
        int(price_info[3])
    except:
        return False
    
    if price_info[1].upper() not in config.fuel_types:
        return False
    
    return price_info
        

def extract_message_type(output):
    '''Extracts type of inbound message.'''

    try:
        message_type = output.get('entry')[0].get('changes')[0].get('value').get(
            'messages')[0].get('type')

    except:
        message_type = 0

    return message_type


def extract_phone_number(output):
    '''Extracts phone number from inbound message.'''

    try:
        user_number = output.get('entry')[0].get('changes')[0].get('value').get(
            'messages')[0].get('from')
        if user_number == '79834118628':
            user_number = '789834118628'
        elif user_number == '79312126866':
            user_number = '789312126866'
    except:
        user_number = 0

    return user_number


def extract_button_info(output):
    '''Extract text and id from button or list-button.'''

    try:
        message_button = output.get('entry')[0].get('changes')[0].get(
            'value').get('messages')[0].get('interactive').get(
                'button_reply').get('id')
        title_button = False

    except:
        message_button = output.get('entry')[0].get('changes')[0].get(
            'value').get('messages')[0].get('interactive').get(
                'list_reply').get('id')
        title_button = output.get('entry')[0].get('changes')[0].get(
            'value').get('messages')[0].get('interactive').get(
                'list_reply').get('title')
    
    return message_button, title_button


def extract_coords(output):
    '''Extract coordinates from location message.'''

    try:
        lat = float(
            output.get('entry')[0].get('changes')[0].get('value').get(
                'messages')[0].get('location').get('latitude'))
        lon = float(
            output.get('entry')[0].get('changes')[0].get('value').get(
                'messages')[0].get('location').get('longitude'))
    except:
        lat = False
        lon = False

    return lat, lon