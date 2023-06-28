# Fuel / electric stations
## Change language: [English](README.en.md)
***
Bilingual Whatsapp bot that determines the cheapest gas stations and electric charges with the selected fuel type within a given radius (Italy).
## [DEMO](README.demo.md)
## [LIVE](https://wa.me/+393516886218)
## Functionality:
1. Language selection (remembered for each user)
2. Selection of the type of fuel of interest (remembered for each user)
3. Determination of gas stations / electric stations within a radius specified by the user with minimum prices for the selected type of fuel
## Installation and use:
- Create an .env file containing the following variables:
> the file is created in the root folder of the project

**PHONE_ID** (phone ID on Facebook)\
**FB_TOKEN** (Facebook Token)\
**VERIFY_TOKEN** (Code word, invented by yourself, specified when creating a Webhook)\
**RADIUS** (refueling search radius)\
**ELECTRIC_RADIUS** (electric charge search radius)\
**KEY_ELECTRIC** (key to search for electric chargers)\
**URL_ELECTRIC** (url - https://api.openchargemap.io/v3/poi)
- In the Facebook profile, in the webhook section, specify the address of the server hosting the bot
- Install the virtual environment and activate it (if necessary):
> Installation and activation in the root folder of the project
```sh
python3 -m venv venv
source venv/bin/activate # for macOS
source venv/Scripts/activate # for Windows
```
- Install dependencies:
```sh
pip install -r requirements.txt
```
- Run project:
```sh
python3 main.py
```