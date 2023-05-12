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

url = "https://www.entel.pe/empresas/catalogo/equipos/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
divs = soup.find_all('div')
grupo_div = soup.find('div',class_='e-catalog-equipment__grid__list e-box-inline-block-ts e-box-inline-block--clear-tm')
lista = []
try:
    for div in grupo_div.find_all('div', recursive=False):
        href = div.div.a['href']
        if href=='javascript:void(0);':
            href = div.div['href']
            lista.append(href)
        else:
            href = div.div['href']
            lista.append(href)
except AttributeError:
    pass
print(len(lista))

options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disablevicibox-extensions')
options.add_argument("--disable-extensions")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(r"D:\ChromeDriver\chromedriver.exe",chrome_options=options)
archivo_exportado = "D:\\Marcos_Entel\\Datos_Entel.csv"
archivo_backup = "D:\\Marcos_Entel\\Datos_Entel_backup.csv"
# Inicializamos el navegador
datos = []
for url_link in lista:
    print(url_link)
    driver.get(url_link) # Entramos URL x URL

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
            #print(Resumen)
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
