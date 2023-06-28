import os
from dotenv import load_dotenv
 
load_dotenv()

# config
PHONE_ID = os.getenv('PHONE_ID')  # отмечено на скриншотах
FB_TOKEN = os.getenv('FB_TOKEN')  # отмечено на скриншотах
VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')  # придумывается самостоятельно, на скриншотах отмечено, где указывать
RADIUS = int(os.getenv('RADIUS'))
ELECTRIC_RADIUS = int(os.getenv('ELECTRIC_RADIUS'))
KEY_ELECTRIC = os.getenv('KEY_ELECTRIC')
URL_ELECTRIC = os.getenv('URL_ELECTRIC')

HEADER = {
    'Authorization': f'Bearer {FB_TOKEN}',
    'Content-Type': 'application/json'
}

URL = f'https://graph.facebook.com/v16.0/{PHONE_ID}/messages'

fuel_types = {
    'BENZINA' : 'gasoline',
    'GASOLIO' : 'diesel',
    'GNL' : 'gnl',
    'GPL' : 'gpl',
    'L-GNC' : 'gnc',
    'METANO' : 'metan',
}

fuel_field = {
    'Gasoline' : 'gasoline',
    'Benzina' : 'gasoline',
    'Diesel' : 'diesel',
    'Gasolio' : 'diesel',
    'Gas' : 'gas',
    'GNL' : 'gnl',
    'GPL' : 'gpl',
    'L-GNC' : 'gnc',
    'Metano' : 'metan',
    'Methane' : 'metan',
}


# connections types:
connection_types = {'CCS (Type 1)' : 32,
                    'CCS (Type 2)': 33,
                    'CHAdeMO': 2,
                    'Tesla (Model S/X)' : 30,
                    'Tesla Supercharger' : 27,
                    'Type 1 (J1772)': 1,
                    'Type 2 (Socket Only)': 25,
                    'Type 2 (Tethered C.)' : 1036,
                    'CCS (Tipo 1)': 32,
                    'CCS (Tipo 2)': 33,
                    'Tesla (Modello S/X)': 30,
                    'Supercharger Tesla': 27,
                    'Tipo 1 (J1772)': 1,
                    'Tipo 2 (solo presa)': 25,
                    'Tipo 2 (Tethered C.)': 1036,
}

# messages
START_MESSAGE = "I'm AnyWire Bot and I'll help you to find the cheapest fuel within 3 km. / Sono AnyWire Bot e ti aiuterò a trovare il carburante più economico entro 3 km."  # приветственное сообщение (желательно составить на двух языках, т.к. мы не знаем язык нового пользователя)

CHOOSE_LANG = 'Choose your language / Scegli la tua lingua:'  # сообщение, возникающее после нажатия кнопки "Изменить язык"
CHOOSE_FUEL_ENG = 'Choose the type of fuel:'  # сообщение, возникающее после выбора языка или после нажатия кнопки "Изменить тип топлива (английский)"
CHOOSE_FUEL_ITA = 'Scegli il tipo di carburante:'  # сообщение, возникающее после выбора языка или после нажатия кнопки "Изменить тип топлива (итальянский)"

SETTINGS_SAVED_ENG = 'Share your current location to get the nearest fuel stations with the cheapest prices. Tap "+" (iOS) or "Clip" (Android) and choose "Location". *We guarantee that your location will not be used for other purposes.*'  # сообщение, появляющееся после полной инициализации пользователя (когда сохранен язык и выбрано топливо) - английский
SETTINGS_SAVED_ITA = 'Condividi la tua posizione attuale per ottenere le stazioni di rifornimento più vicine con i prezzi più economici. Tocca "+" (iOS) o "Clip" (Android) e scegli "Posizione". *Garantiamo che la tua posizione non verrà utilizzata per altri scopi.*'  # сообщение, появляющее после полной инициализации пользователя (когда сохранен язык и выбрано топливо) - итальянский

# !!!!
ELECTRIC_SETTINGS_SAVED_ENG = 'Share your current location to get the nearest charger stations. Tap "+" (iOS) or "Clip" (Android) and choose "Location". *We guarantee that your location will not be used for other purposes.*'  # сообщение, появляющее после полной инициализации пользователя (когда сохранен язык и выбрано топливо) - английский
ELECTRIC_SETTINGS_SAVED_ITA = 'Condividi la tua posizione attuale per ottenere le stazioni di ricarica più vicine. Tocca "+" (iOS) o "Clip" (Android) e scegli "Posizione". *Garantiamo che la tua posizione non verrà utilizzata per altri scopi.*'  # сообщение, появляющее после полной инициализации пользователя (когда сохранен язык и выбрано топливо) - итальянский

NO_STATIONS_ENG = 'There are no fuel stations within a radius of 3 km that match your requirements.'  # сообщение, возникающее, когда в радиусе 5 км нет запровок, удовлетворяющих запросу (англйиский)
NO_STATIONS_ITA = 'Non ci sono distributori di carburante nel raggio di 3 km che soddisfano le tue esigenze.'  # сообщение, возникающее, когда в радиусе 5 км нет запровок, удовлетворяющих запросу (итальянский)

# !!!!
NO_CHARGERS_ENG = 'There are no charger stations within a radius of 3 km that match your requirements.'  # сообщение, возникающее, когда в радиусе 5 км нет станций, удовлетворяющих запросу (англйиский)
NO_CHARGERS_ITA = 'Non ci sono stazioni di ricarica nel raggio di 3 km che soddisfano le tue esigenze.'  # сообщение, возникающее, когда в радиусе 5 км нет станций, удовлетворяющих запросу (итальянский)

CONNECTION_ERROR_ENG = 'Connection error.'  # сообщение возникающее при отсутствии связи с внешним API для поиска заправок (английский)
CONNECTION_ERROR_ITA = 'Errore di connessione.'  # сообщение возникающее при отсутствии связи с внешним API для поиска заправок (итальянский)

BOT_ERROR_ENG = 'Bot error'  # сообщение, возникающее если бот столкнулся с проблемами в БД (английский)
BOT_ERROR_ITA = 'Errore del robot'  # сообщение, возникающее если бот столкнулся с проблемами в БД (итальянский)

LOCATION_ERROR_ENG = "Can't get data for this location."  # сообщение, возникающее, если отправленная геопозиция не относится ни к одной из 52 провинций (английский)
LOCATION_ERROR_ITA = "Impossibile recuperare i dati per questa posizione."  # сообщение, возникающее, если отправленная геопозиция не относится ни к одной из 52 провинций (итальянский)

CONNECTION_LOC_ERROR_ENG = 'Connection error.'  # сообщение возникающее при отсутствии связи с внешним API для определения провинции (английский)
CONNECTION_LOC_ERROR_ITA = 'Errore di connessione.'  # сообщение возникающее при отсутствии связи с внешним API для определения провинции (итальянский)

DATA_ERROR_ENG = 'Bot error'  # сообщение, возникающее если бот столкнулся с проблемами при обработке запроса (английский)
DATA_ERROR_ITA = 'Errore del robot'  # сообщение, возникающее если бот столкнулся с проблемами при обработке запроса (итальянский)

GASOLINE_TYPE_ENG = 'Choose gasoline type:'  # сообщение, возникающее при выборе типа бензина (английский)
GASOLINE_TYPE_ITA = 'Scegli il tipo di benzina:'  # сообщение, возникающее при выборе типа бензина (итальянский)
DIESEL_TYPE_ENG = 'Choose diesel type:'  # сообщение, возникающее при выборе типа дизеля (английский)
DIESEL_TYPE_ITA = 'Scegli il tipo gasolio:'  # сообщение, возникающее при выборе типа дизеля (итальянский)
GAS_TYPE_ENG = 'Choose gas type:'  # сообщение, возникающее при выборе типа газа (английский)
GAS_TYPE_ITA = 'Scegli il tipo di gas:'  # сообщение, возникающее при выборе типа газа (итальянский)
#!!!!
ELECTRIC_TYPE_ENG = 'Choose connection type: (we display nearest chargers, without ranging by price)' # сообщение, возникающее при выборе типа зарядки (английский)
#!!!!
ELECTRIC_TYPE_ITA = 'Scegli il tipo di connessione: (visualizziamo i caricabatterie più vicini, senza variare in base al prezzo)' # сообщение, возникающее при выборе типа зарядки (итальянский)

#!!!
PRICE_ENG = 'not defined' # надпись, когда цена не определена (англйиский)
PRICE_ITA = 'non definito' # надпись, когда цена не определена (итальянский)

# headers - максимальная длина 25 символов
START_HEADER = 'Hi! / Ciao!'  # заголовок приветственного сообщения
SETTINGS_HEADER_ENG = 'Your settings have been saved'  # заголовок сообщения, появляющегося после полной инициализации пользователя (когда сохранен язык и выбрано топливо) - английский
SETTINGS_HEADER_ITA = 'Le tue impostazioni sono state salvate'  # заголовок сообщения, появляющегося после полной инициализации пользователя (когда сохранен язык и выбрано топливо) - итальянский

# footers
START_FOOTER = 'Choose your language / Scegli la tua lingua:'  # подвал приветственного сообщения

FOOTER_FUEL_ENG = 'Fuel:'  # надпись, отображающаяся в "подвале" перед сохраненным типом топлива (английский)
FOOTER_FUEL_ITA = 'Carburante:'  # надпись, отображающаяся в "подвале" перед сохраненным типом топлива (итальянский)
# !!!!
FOOTER_ELECTRIC_ENG = 'Connector:'  # надпись, отображающаяся в "подвале" перед сохраненным типом зарядки (английский)
FOOTER_ELECTRIC_ITA = 'Connettore:'  # надпись, отображающаяся в "подвале" перед сохраненным типом зарядки (итальянский)

FOOTER_LANG_ENG = 'Language:'  # надпись, отображающаяся в "подвале" перед выбранным языком (английский)
FOOTER_LANG_ITA = 'Lingua:'  # надпись, отображающаяся в "подвале" перед выбранным языком (итальянский)

# buttons - максимальная длина 20 символов
START_BUTTON = 'BUTTON'  # кнопка, появляющаяся в приветственном сообщении (необходима для отображения header и footer)

ENG_BUTTON = 'English'  # кнопка выбора английского языка
ITA_BUTTON = 'Italiana'  # кнопка выбора итальянского языка

GASOLINE_BUTTON_ENG = 'Gasoline'  # кнопка выбора бензина (англйиский)
GASOLINE_BUTTON_ITA = 'Benzina'  # кнопка выбора бензина (итальянский)
DIESEL_BUTTON_ENG = 'Diesel'  # кнопка выбора дизеля (англйиский)
DIESEL_BUTTON_ITA = 'Gasolio'  # кнопка выбора дизеля (итальянский)
GAS_BUTTON_ENG = 'Gas'  # кнопка выбора дизеля (англйиский)
GAS_BUTTON_ITA = 'Gas'  # кнопка выбора дизеля (итальянский)
#!!!!
ELECTRIC_BUTTON_ENG = 'Electric power'  # кнопка выбора электричества (англйиский)
#!!!!
ELECTRIC_BUTTON_ITA = 'Energia elettrica'  # кнопка выбора электричества (итальянский)

CHANGE_LANG_BUTTON_ENG = 'Change language'  # кнопка смены языка (англйиский)
CHANGE_LANG_BUTTON_ITA = 'Cambia lingua'  # кнопка смены языка (итальянский)
CHANGE_FUEL_BUTTON_ENG = 'Change fuel'  # кнопка смены топлива (англйиский)
CHANGE_FUEL_BUTTON_ITA = 'Cambia carburante'  # кнопка смены топлива (итальянский)

GASOLINE_TYPE_BUTTON_ENG = 'Gasoline type'  # сообщение, отображающееся на кнопке открытия списка с видами бензина (английский)
GASOLINE_TYPE_BUTTON_ITA = 'Tipo benzina'  # сообщение, отображающееся на кнопке открытия списка с видами бензина (итальянский)
DIESEL_TYPE_BUTTON_ENG = 'Diesel type'  # сообщение, отображающееся на кнопке открытия списка с видами дизеля (английский)
DIESEL_TYPE_BUTTON_ITA = 'Tipo gasolio'  # сообщение, отображающееся на кнопке открытия списка с видами дизеля (итальянский)
GAS_TYPE_BUTTON_ENG = 'Gas type'  # сообщение, отображающееся на кнопке открытия списка с видами газа (английский)
GAS_TYPE_BUTTON_ITA = 'Tipo di gas'  # сообщение, отображающееся на кнопке открытия списка с видами газа (итальянский)
# !!!!
CONNECTION_TYPE_BUTTON_ENG = 'Connection type' # сообщение, отображающееся на кнопке открытия списка с видами зарядок (английский)
# !!!!
CONNECTION_TYPE_BUTTON_ITA = 'Tipo di connessione' # сообщение, отображающееся на кнопке открытия списка с видами зарядок (английский)

# list buttons - максимум 24 символа
CHANGE_TITLE_ENG = 'Change fuel type'  # кнопка смены топлива в списке (английский)
CHANGE_TITLE_ITA = 'Cambia carburante'  # кнопка смены топлива в списке (итальянский)

# !!!! 
CHOOSE_FUEL_LIST_ENG = 'Fuel type'  # кнопка выбора типа топлива (английский)"
# !!!! 
CHOOSE_FUEL_LIST_ITA = 'Tipo di carburante'  # кнопка выбора типа топлива (итальянский)"

# list descriptions - максимальная длина 512 символов
CHANGE_DESCR_ENG = 'Press if you want to change the type of fuel'  # описание кнопки смены топлива в списке (английский)
CHANGE_DESCR_ITA = 'Premere se si desidera modificare il tipo di carburante'  # описание кнопки смены топлива в списке (итальянский)

#list titles
GASOLINE_TITLE_ENG = 'GASOLINE'  # заголовок списка с видами бензина (англйиский)
GASOLINE_TITLE_ITA = 'BENZINA'  # заголовок списка с видами бензина (итальянский)
DIESEL_TITLE_ENG = 'DIESEL'  # заголовок списка с видами дизеля (англйиский)
DIESEL_TITLE_ITA = 'GASOLIO'  # заголовок списка с видами дизеля (итальянский)
GAS_TITLE_ENG = 'GAS'  # заголовок списка с видами газа (англйиский)
GAS_TITLE_ITA = 'GAS'  # заголовок списка с видами газа (итальянский)

# !!!!
FUEL_TITLE_ENG = 'FUEL TYPE' # заголовок списка с типами топлива (английский)
# !!!!
FUEL_TITLE_ITA = 'TIPO DI CARBURANTE' # заголовок списка с типами топлива (итальянский)
# !!!
CONNECTION_TITLE_ENG = 'CONNECTION TYPE' # заголовок списка с типами зарядок (английский)
# !!!
CONNECTION_TITLE_ITA = 'TIPO DI CONNESSIONE' # заголовок списка с типами зарядок (итальянский)

#address
ADDRESS_ENG = 'Tap on the map to build a route'  # адрес, отображающийся при отправке геолокации заправки (английский)
ADDRESS_ITA = 'Tocca la mappa per creare un percorso'  # адрес, отображающийся при отправке геолокации заправки (итальянский)

PROVINCES = ['AG', 'AL', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AT', 'AV', 'BA', 'BG', 'BI', 'BL', 'BN', 'BO', 'BR', 'BS', 'BT', 'BZ', 'CA', 'CB', 'CE', 'CH', 'CL', 'CN', 'CO', 'CR', 'CS', 'CT', 'CZ', 'EN', 'FC', 'FE', 'FG', 'FI', 'FM', 'FR', 'GE', 'GO', 'GR', 'IM', 'IS', 'KR', 'LC', 'LE', 'LI', 'LO', 'LT', 'LU', 'MB', 'MC', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NA', 'NO', 'NU', 'OR', 'PA', 'PC', 'PD', 'PE', 'PG', 'PI', 'PN', 'PO', 'PR', 'PT', 'PU', 'PV', 'PZ', 'RA', 'RC', 'RE', 'RG', 'RI', 'RM', 'RN', 'RO', 'SA', 'SI', 'SO', 'SP', 'SR', 'SS', 'SU', 'SV', 'TA', 'TE', 'TN', 'TO', 'TP', 'TR', 'TS', 'TV', 'UD', 'VA', 'VB', 'VC', 'VE', 'VI', 'VR', 'VT', 'VV']