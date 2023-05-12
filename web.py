from asyncio import sleep
from typing import Sized
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date
from datetime import datetime
import time
import keyword
import keyboard
import os
import shutil
from tkinter import messagebox
import pandas as pd

options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disablevicibox-extensions')
options.add_argument("--disable-extensions")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(r"D:\ChromeDriver\chromedriver.exe",chrome_options=options)
archivo_exportado = "D:\\Marcos_Entel\\Datos_Entel.csv"
archivo_backup = "D:\\Marcos_Entel\\Datos_Entel_backup.csv"
# Inicializamos el navegador
#Lista = ['samsung-galaxy-a22-64','samsung-galaxy-a33']#,'samsung-galaxy-s21-fe-128gb','iphone-13-pro-max-128gb','samsung-galaxy-a53']
Lista = ['samsung-galaxy-a53','motorola-moto-g31','zte-blade-v30-vita','samsung-galaxy-s21-fe-128gb','oppo-a54','samsung-galaxy-a03-core','iphone-14-128gb','iphone-13-pro-max-128gb','vivo-v21','iphone-13-pro-128gb','vivo-y-21s','vivo-y-53s','iphone-14-256gb','iphone-14-512gb','iphone-14-pro-256gb','xiaomi-redmi-10-2022','zte-blade-a51','oppo-reno-7','iphone-13-512gb','iphone-13-pro-512gb','redmi-10c','redmi-note-11s','zte-blade-a31-plus-32gb','honor-x7','samsung-galaxy-s22','poco-m4-pro-128gb-5g','oppo-a77','vivo-y55','motorola-moto-g50','iphone-12-64gb','xiaomi-11-t','iphone-13-256gb','motorola-e-20','oppo-a-16','xiaomi-redmi-note-11-128gb','apple-iphone-se-2022-64gb','iphone-13-128gb','edge-30-fusion-audifonos','edge-30-neo','edge-30-neo-audifonos','galaxy-a04e','motorola-moto-edge-30-pro-5g','iphone-14-plus-128gb','iphone-14-pro-128gb','iphone-14-cargador','iphone-14-plus-airpods','apple-iphone-11-64gb','honor-70-256gb-earbuds-x','samsung-galaxy-s20-fe-5g','motorola-moto-g22','vivo-y22s','samsung-galaxy-a22-64','samsung-galaxy-a33','xiaomi-redmi-10c-364gb','samsung-galaxy-a04','redmi-note-11s-128gb-5g','oppo-a57-128gb','honor-x6']
url_base = 'https://www.entel.pe/empresas/catalogo/equipo/'
url_params = '/?modalidad=migra&forma_pago=contado'
urls=[]
datos = []
for item in Lista:
    url = url_base + item + url_params
    urls.append(url)
print(item)

for url in urls:
    driver.get(url)