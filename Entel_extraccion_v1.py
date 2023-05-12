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
import requests
import re
from bs4 import BeautifulSoup




options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disablevicibox-extensions')
options.add_argument("--disable-extensions")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(r"D:\ChromeDriver\chromedriver.exe",chrome_options=options)
archivo_exportado = "D:\\Marcos_Entel\\Datos_Entel.csv"
archivo_backup = "D:\\Marcos_Entel\\Datos_Entel_backup.csv"
# Inicializamos el navegador

Lista = ['oppo-reno-7-oppo-enco-air-2','iphone-14-pro-128gb-cargador-apple-20w','xiaomi-redmi-note-12-buds-essential','oppo-a77-neckband','oppo-reno-6-lite-neckband','honor-magic-5-lite-bindu-audifonos','iphone-14-plus-512gb','samsung-galaxy-s21-fe-128gb','iphone-14-128gb','vivo-v21','iphone-13-pro-256gb','iphone-14-512gb','iphone-14-plus-256gb','iphone-14-pro-256gb','iphone-14-pro-max-256gb','iphone-14-pro-max-512gb','motorola-moto-e22i','honor-70-256gb','oppo-reno-7','motorola-moto-g23','samsung-galaxy-z-flip-4-128gb','samsung-galaxy-z-flip-4-256gb','oppo-a77','xiaomi-redmi-a2','samsung-galaxy-s23-128gb','samsung-galaxy-a23','vivo-y55','honor-magic-5-lite','oppo-reno-6-lite','honor-x9','samsung-galaxy-s23-256gb','samsung-galaxy-s23-plus-512gb','samsung-galaxy-s23-ultra-512gb','zte-a51-lite','samsung-galaxy-s23-plus-256gb','samsung-galaxy-s23-ultra-256gb','iphone-13-128gb','edge-30-fusion-audifonos','edge-30-neo','edge-30-neo-audifonos','galaxy-a04e','iphone-14-plus-128gb','iphone-14-pro-128gb','iphone-14-pro-max-128gb','zte-blade-vita-v40','apple-iphone-11-64gb','honor-70-256gb-earbuds-x','samsung-galaxy-s20-fe-5g','motorola-moto-g22','honor-x8a','motorola-moto-g53','vivo-y22s','samsung-galaxy-a33','xiaomi-redmi-10c-364gb','samsung-galaxy-a04','redmi-note-11s-128gb-5g','oppo-a57-128gb','honor-x6','oppo-a17','honor-x7a','samsung-galaxy-a14','xiaomi-redmi-note-12','redmi-note-11-128gb-buds-essential','xiaomi-redmi-12c','zte-blade-a53-plus','xiaomi-redmi-a1','samsung-galaxy-a53','motorola-moto-g31','zte-blade-v30-vita','xiaomi-redmi-note-10-pro','oppo-a54','samsung-galaxy-a03-core','iphone-13-pro-max-128gb','iphone-13-pro-128gb','iphone-14-256gb','xiaomi-redmi-10-2022','iphone-14-pro-512gb','iphone-13-512gb','iphone-13-pro-512gb','samsung-galaxy-z-fold-4-256gb','samsung-galaxy-z-fold-4-512gb','redmi-10c','redmi-note-11s','honor-x7','samsung-galaxy-s22','honor-50-256gb','huawei-nova-9-se','zte-blade-a5-2020-32gb','honor-70-128gb','samsung-galaxy-s22-plus','samsung-galaxy-s22-ultra','samsung-galaxy-a52s','honor-x8','huawei-nova-y70','xiaomi-redmi-10a','xiaomi-12','motorola-moto-g50','iphone-13-256gb','xiaomi-redmi-note-11-128gb','iphone-13-mini-256gb','apple-iphone-se-2022-64gb','iphone-se-2022-256gb','iphone-13-pro-max-256gb','samsung-galaxy-a22','galaxy-a13','iphone-13-mini-128gb','honor-x8-pack','huawei-nova-9-band','samsung-galaxy-a03s','xiaomi-redmi-9c','motorola-moto-edge-30-pro-5g','iphone-14-cargador','iphone-14-plus-airpods','xiaomi-redmi-note-11-pro-128gb','apple-iphone-12-128gb','xiaomi-redmi-10-5g','motorola-moto-e32','motorola-moto-edge-20-lite','samsung-galaxy-a22-64','iphone-se-2022-128gb']


url_base = 'https://www.entel.pe/empresas/catalogo/equipo/'
url_params = '/?modalidad=migra&forma_pago=contado'
urls=[]
datos = []
for item in Lista:
    url = url_base + item + url_params
    urls.append(url)
print(item)

for url in urls:
    driver.get(url) # Entramos URL x URL

    try:
        accept_cookies_button = driver.find_element(By.XPATH,"//button[text()='Aceptar']")
        accept_cookies_button.click()
    except:
        pass

    WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div[1]/section[1]/div/div[3]/div[2]/div[1]/form/div[2]/div[2]/div/div[1]/a'))).click()
    elements = []
    elements = driver.find_elements(By.CSS_SELECTOR,'#vc-view-planes > div.dropdown > ul > li')
    time.sleep(1)
    for element in elements:
        time.sleep(1)
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        if element.is_displayed():
            ActionChains(driver).move_to_element(element).click(element).perform() 
        scrap = []
        scrap = driver.find_elements(By.CSS_SELECTOR,'#vc-view-forma-pago > div > div')
        for i in range(len(scrap)):
            try:
                time.sleep(1)
                scrap[i].click()
            except StaleElementReferenceException:
                while True:
                    try:
                        time.sleep(1)
                        scrap = driver.find_elements(By.CSS_SELECTOR,'#vc-view-forma-pago > div > div')
                        scrap[i].click()
                        break
                    except StaleElementReferenceException:
                        continue
            Resumen = driver.find_element("xpath",'/html/body/div[4]/div[1]/section[1]/div/div[3]/div[2]/div[2]/div[4]/div/div[1]').text
            print(Resumen)
            Resumen2 = Resumen.replace("\n"," ").replace("\s+"," ").replace("Resumen de pedido ","")\
                            .replace(" Equipo: Cantidad de equipos 1 Precio total del equipo ","|CONTADO|")\
                            .replace(" Equipo: Cantidad de equipos 1 CUOTA INICIAL: ","|CUOTA|").replace("S/ ","").replace(" Plan: Empresa Pro ","|").replace(" Chip y delivery: Gratis","")
            datos.append(Resumen2)
    print('ok-URL')

df = pd.DataFrame(datos,columns=["General"])
df.to_csv(archivo_backup,index=False)
df["General"] = df["General"].str.replace("\s+"," ")
df['General'] = df['General'].astype('str')
#df['Plan_Tarifario'] = df['Plan_Tarifario'].astype('str')
df = df.assign(Equipo=df.General.str.split('|').str[0],Plan=df.General.str.split('|').str[1],Precio_Equipo=df.General.str.split('|').str[2],Tipo=df.General.str.split('|').str[3])#,Modo_Cobro=df.General.str.split('|').str[4],Contado_CuotaInicial=df.General.str.split('|').str[5],)
#df = df.assign(CONTADO_CUOTAS=df.Plan.str.split('*').str[0],Plan_Tarifario=df.Plan.str.split('*').str[1])
df["Plan_Tarifario"] = df["Tipo"].str.split(" Dto.").str[0]
df["Precio_Equipo_v1"] = df["Precio_Equipo"].str.split("% dto. EXCLUSIVO ONLINE ").str[1]
df["PRECIO_CONTADO_EQUIPO"] = df["Precio_Equipo_v1"].str.split(" ").str[0]
df["PRECIO_ONLINE_EQUIPO"] = df["Precio_Equipo_v1"].str.split(" ").str[1]
df["Precio_Equipo_v2"] = df["Precio_Equipo"].str.split(" CUOTAS DE:").str[0]
df["PRECIO_CUOTA"] = df["Precio_Equipo"].str.split(" CUOTAS DE:").str[1]
df["CUOTA_INICIAL"] = df["Precio_Equipo_v2"].str.split(" ").str[0]
df["CANTIDAD_CUOTA"] = df["Precio_Equipo_v2"].str.split(" ").str[1]
df[['Equipo','Plan','Plan_Tarifario','PRECIO_CONTADO_EQUIPO','PRECIO_ONLINE_EQUIPO','CANTIDAD_CUOTA','CUOTA_INICIAL','PRECIO_CUOTA']].to_csv(archivo_exportado,index=False)
print(df.head())
driver.quit()
