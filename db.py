import sqlite3
import logging

database = sqlite3.connect("energy.db")
cursor = database.cursor()

try:
    # creates table with fuel stations
    cursor.execute('''CREATE TABLE fuel_stations (
        unique_id INTEGER UNIQUE,
        manager VARCHAR,
        brand VARCHAR (30),
        name TEXT,
        address TEXT,
        province VARCHAR (10),
        lat REAL,
        long REAL,
        gasoline_self REAL,
        gasoline_service REAL,
        diesel_self REAL,
        diesel_service REAL,
        gnl_self REAL,
        gnl_service REAL,
        gpl_self REAL,
        gpl_service REAL,
        gnc_self REAL,
        gnc_service REAL,
        metan_self REAL,
        metan_service REAL,
        updated BOOLEAN DEFAULT True 
    )''')
except:
    logging.error('Fuel_stations table already exists.')

try:
    # creates table with users
    cursor.execute('''CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        number VARCHAR (20),
        language VARCHAR (10),
        fuel VARCHAR(30)
    )''')
except:
    logging.error('Users table already exists.')


# cursor.execute("DELETE FROM products WHERE unique_id=2")
# database.commit()