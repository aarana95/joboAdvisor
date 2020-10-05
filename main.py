#!C:\Users\arana\AppData\Local\Continuum\anaconda3\python.exe

import json
import utils_functions
import sqlite3
import os

#Articulo donde me inspire https://www.codementor.io/@gergelykovcs/how-and-why-i-built-a-simple-web-scrapig-script-to-notify-us-about-our-favourite-food-fcrhuhn45

dirname = os.path.dirname(__file__)
config_dir = os.path.join(dirname, 'config.json')
db_dir = os.path.join(dirname, 'espectaculos.db')

url = "https://madridcultura-jobo.shop.secutix.com/account/login"

with open(config_dir) as f:
    config = json.load(f)

driver = config['chromeDriverPath']
credentials_jobo = config['jobo']
credentials_gmail = config['senderMail']
send_to = config['send_to']


#Nos conectamos a la BBDD
conn = sqlite3.connect(db_dir)
conection_BBDD = conn.cursor()


# Acceso a la lista de espectaculos
page = utils_functions.get_events_page(url, credentials_jobo, driver)

events = utils_functions.get_events(page)

view_events = utils_functions.get_view_events(conection_BBDD)

mail_text = utils_functions.available_events(events, view_events, conection_BBDD)

if len(mail_text) > 0:

    conn.commit()
    utils_functions.send_mail(mail_text, credentials_gmail, send_to)