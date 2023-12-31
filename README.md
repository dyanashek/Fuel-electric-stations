# Fuel / electric stations
## Change language: [English](README.en.md)
***
Двуязычный Whatsapp бот, определяющий самые дешевые заправки и электростанции с выбранным топливом в заданном радиусе (Италия).
## [DEMO](README.demo.md)
## [LIVE](https://wa.me/+393516886218)
## Функционал:
1. Выбор языка (запоминается для каждого пользователя)
2. Выбор интересующего вида топлива (запоминается для каждого пользователя)
3. Определение заправочных/электрических станций в заданном от пользователя радиусе с минимальными ценами на выбранный тип топлива
## Установка и использование:
- Создайте файл .env, содержащий следующие переменные:
> файл создается в корневой папке проекта

**PHONE_ID** (ID телефона на Facebook)\
**FB_TOKEN** (Токен Facebook)\
**VERIFY_TOKEN** (Кодовое слово, придумывается самостоятельно, указывается при создании Webhook)\
**RADIUS** (радиус поиска заправок)\
**ELECTRIC_RADIUS** (радиус поиска электрических зарядок)\
**KEY_ELECTRIC** (ключ для поиска электрических зарядок)\
**URL_ELECTRIC** (url - https://api.openchargemap.io/v3/poi)
- В профиле Facebook, в разделе webhook, указать адрес сервера, на котором размещен бот
- Установить виртуальное окружение и активировать его (при необходимости):
> Установка и активация в корневой папке проекта
```sh
python3 -m venv venv
source venv/bin/activate # for macOS
source venv/Scripts/activate # for Windows
```
- Установить зависимости:
```sh
pip install -r requirements.txt
```
- Запустить проект:
```sh
python3 main.py
```
