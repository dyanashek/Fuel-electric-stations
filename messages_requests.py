import json
import requests
from python_whatsapp_bot import Whatsapp
from python_whatsapp_bot import Inline_keyboard

import config

bot = Whatsapp(config.PHONE_ID, config.FB_TOKEN)

def energy_eng(user_number):
    '''Constructs list with fuel types in english.'''

    params = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": f"{user_number}",
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": config.CHOOSE_FUEL_ENG
            },
            "action": {
                "button":
                config.CHOOSE_FUEL_LIST_ENG,
                "sections": [{
                    "title":
                    config.FUEL_TITLE_ENG,
                    "rows": [
                        {
                            "id": "ffuel1_eng",
                            "title": config.GASOLINE_BUTTON_ENG
                        },
                        {
                            "id": "ffuel2_eng",
                            "title": config.DIESEL_BUTTON_ENG
                        },
                        {
                            "id": "gas_eng",
                            "title": config.GAS_BUTTON_ENG
                        },
                        {
                            "id": "electric_eng",
                            "title": config.ELECTRIC_BUTTON_ENG
                        }
                    ]
                }]
            }
        }
    })
    return params


def energy_ita(user_number):
    '''Constructs list with fuel types in italian.'''

    params = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": f"{user_number}",
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": config.CHOOSE_FUEL_ITA
            },
            "action": {
                "button":
                config.CHOOSE_FUEL_LIST_ITA,
                "sections": [{
                    "title":
                    config.FUEL_TITLE_ITA,
                    "rows": [
                        {
                            "id": "ffuel3_ita",
                            "title": config.GASOLINE_BUTTON_ITA
                        },
                        {
                            "id": "ffuel4_ita",
                            "title": config.DIESEL_BUTTON_ITA
                        },
                        {
                            "id": "gas_ita",
                            "title": config.GAS_BUTTON_ITA
                        },
                        {
                            "id": "electric_ita",
                            "title": config.ELECTRIC_BUTTON_ITA
                        }
                    ]
                }]
            }
        }
    })
    return params


def gas_eng(user_number):
    '''Constructs list with gas types in english.'''

    params = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": f"{user_number}",
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": config.GAS_TYPE_ENG
            },
            "action": {
                "button":
                config.GAS_TYPE_BUTTON_ENG,
                "sections": [{
                    "title":
                    config.GAS_TITLE_ENG,
                    "rows": [
                        {
                            "id": "ffuel5_eng",
                            "title": "GNL",
                        },
                        {
                            "id": "ffuel6_eng",
                            "title": "GPL",
                        },
                        {
                            "id": "ffuel7_eng",
                            "title": "L-GNC",
                        },
                        {
                            "id": "ffuel8_eng",
                            "title": "Methane",
                        },
                        {
                            "id": config.CHANGE_FUEL_BUTTON_ENG,
                            "title": config.CHANGE_TITLE_ENG,
                            "description": config.CHANGE_DESCR_ENG,
                        },
                    ]
                }]
            }
        }
    })

    return params


def gas_ita(user_number):
    params = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": f"{user_number}",
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": config.GAS_TYPE_ITA
            },
            "action": {
                "button":
                config.GAS_TYPE_BUTTON_ITA,
                "sections": [{
                    "title":
                    config.GAS_TITLE_ITA,
                    "rows": [
                        {
                            "id": "ffuel9_ita",
                            "title": "GNL",
                        },
                        {
                            "id": "ffuel10_ita",
                            "title": "GPL",
                        },
                        {
                            "id": "ffuel11_ita",
                            "title": "L-GNC",
                        },
                        {
                            "id": "ffuel12_ita",
                            "title": "Metano",
                        },
                        {
                            "id": config.CHANGE_FUEL_BUTTON_ITA,
                            "title": config.CHANGE_TITLE_ITA,
                            "description": config.CHANGE_DESCR_ITA,
                        },
                    ]
                }]
            }
        }
    })
    return params


def electric_eng(user_number):
    params = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": f"{user_number}",
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": config.ELECTRIC_TYPE_ENG
            },
            "action": {
                "button":
                config.CONNECTION_TYPE_BUTTON_ENG,
                "sections": [{
                    "title":
                    config.CONNECTION_TITLE_ENG,
                    "rows": [
                        {
                            "id": "ffuel26_eng",
                            "title": "CCS (Type 1)"
                        },
                        {
                            "id": "ffuel27_eng",
                            "title": "CCS (Type 2)"
                        },
                        {
                            "id": "ffuel28_eng",
                            "title": "CHAdeMO"
                        },
                        {
                            "id": "ffuel29_eng",
                            "title": "Tesla (Model S/X)"
                        },
                        {
                            "id": "ffuel30_eng",
                            "title": "Tesla Supercharger"
                        },
                        {
                            "id": "ffuel31_eng",
                            "title": "Type 1 (J1772)"
                        },
                        {
                            "id": "ffuel32_eng",
                            "title": "Type 2 (Socket Only)"
                        },
                        {
                            "id": "ffuel33_eng",
                            "title": "Type 2 (Tethered C.)"
                        },
                        {
                            "id": config.CHANGE_FUEL_BUTTON_ENG,
                            "title": config.CHANGE_TITLE_ENG,
                            "description": config.CHANGE_DESCR_ENG
                        },
                    ]
                }]
            }
        }
    })

    return params


def electric_ita(user_number):
    params = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": f"{user_number}",
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": config.ELECTRIC_TYPE_ITA
            },
            "action": {
                "button":
                config.CONNECTION_TYPE_BUTTON_ITA,
                "sections": [{
                    "title":
                    config.CONNECTION_TITLE_ITA,
                    "rows": [
                        {
                            "id": "ffuel26_ita",
                            "title": "CCS (Tipo 1)"
                        },
                        {
                            "id": "ffuel27_ita",
                            "title": "CCS (Tipo 2)"
                        },
                        {
                            "id": "ffuel28_ita",
                            "title": "CHAdeMO"
                        },
                        {
                            "id": "ffuel29_ita",
                            "title": "Tesla (Modello S/X)"
                        },
                        {
                            "id": "ffuel30_ita",
                            "title": "Supercharger Tesla"
                        },
                        {
                            "id": "ffuel31_ita",
                            "title": "Tipo 1 (J1772)"
                        },
                        {
                            "id": "ffuel32_ita",
                            "title": "Tipo 2 (solo presa)"
                        },
                        {
                            "id": "ffuel33_ita",
                            "title": "Tipo 2 (Tethered C.)"
                        },
                        {
                            "id": config.CHANGE_FUEL_BUTTON_ITA,
                            "title": config.CHANGE_TITLE_ITA,
                            "description": config.CHANGE_DESCR_ITA
                        },
                    ]
                }]
            }
        }
    })
    return params


def send_message(data):
    try:
        requests.post(url=config.URL,
                        headers=config.HEADER,
                        data=data,
                    )
    except:
        pass


def settings_send_eng(user_number, title_button):
    '''Sends message in english to user when settings completed.'''
    
    try:
        settings = config.SETTINGS_SAVED_ENG
        footer = config.FOOTER_FUEL_ENG

        if title_button in config.connection_types:
            settings = config.ELECTRIC_SETTINGS_SAVED_ENG
            footer = config.FOOTER_ELECTRIC_ENG

        bot.send_message(
            user_number,
            settings,
            reply_markup=Inline_keyboard([
                config.CHANGE_FUEL_BUTTON_ENG,
                config.CHANGE_LANG_BUTTON_ITA,
            ]),
            header=config.SETTINGS_HEADER_ENG,
            header_type='text',
            footer=f'{footer} {title_button}',
            )
        
    except:
        pass


def settings_send_ita(user_number, title_button):
    '''Sends message in italian to user when settings completed.'''
    
    try:
        settings = config.SETTINGS_SAVED_ITA
        footer = config.FOOTER_FUEL_ITA

        if title_button in config.connection_types:
            settings = config.ELECTRIC_SETTINGS_SAVED_ITA
            footer = config.FOOTER_ELECTRIC_ITA

        bot.send_message(
            user_number,
            settings,
            reply_markup=Inline_keyboard([
                config.CHANGE_FUEL_BUTTON_ITA,
                config.CHANGE_LANG_BUTTON_ENG,
            ]),
            header=config.SETTINGS_HEADER_ITA,
            header_type='text',
            footer=f'{footer} {title_button}',
            )
        
    except:
        pass


def location_params(user_number, lat, lon, name, language):
    '''Construct location message.'''

    address_str = ''
    if language == 'English':
        address_str = config.ADDRESS_ENG

    elif language == 'Italiana':
        address_str = config.ADDRESS_ITA

    params = json.dumps({
        "messaging_product": "whatsapp",
        "to": f"{user_number}",
        "type": "location",
        "location": {
            "longitude": lon,
            "latitude": lat,
            "name": address_str,
            "address": name,
        }
    })
    return params