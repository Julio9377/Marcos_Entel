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
import re

options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disablevicibox-extensions')
options.add_argument("--disable-extensions")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(r"D:\ChromeDriver\chromedriver.exe",chrome_options=options)
url= 'https://serviciosweb.osiptel.gob.pe/ConsultaSIRT/Buscar/frmConsultaTar.aspx'
driver.get(url) # Entramos URL x URL

WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div/button'))).click()

#Busqueda Avanzadas
time.sleep(1)
WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/table/tbody/tr[4]/td/table[1]/tbody/tr/td/div/table[2]/tbody/tr/td[3]/div/div/input'))).click()
#Tipo Tarifa --> Establecidas
time.sleep(1)
WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/table/tbody/tr[4]/td/table[1]/tbody/tr/td/div/table[1]/tbody/tr[4]/td[2]/select/option[2]'))).click()
#Vigencia -->Vigentes
time.sleep(1)
WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/table/tbody/tr[4]/td/table[1]/tbody/tr/td/div/table[1]/tbody/tr[5]/td[2]/select/option[2]'))).click()
#Servicio -->Internet
time.sleep(1)
WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/table/tbody/tr[4]/td/table[1]/tbody/tr/td/div/table[1]/tbody/tr[6]/td[2]/table/tbody/tr/td/select/option[5]'))).click()

while True:
    try:
        date_input = driver.find_element(By.ID,'txtFechaIniVig')
        time.sleep(2)
        date_input.clear()
        time.sleep(2)
        date_input.send_keys("01/01/2018")
        break
    except StaleElementReferenceException:
        continue


time.sleep(2)
#Convergente/Empaquetado --> Convergente
WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/table/tbody/tr[4]/td/table[1]/tbody/tr/td/div/div/table/tbody/tr[1]/td[2]/select/option[2]'))).click()
#Alcance --> Empresarial
WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/table/tbody/tr[4]/td/table[1]/tbody/tr/td/div/div/table/tbody/tr[4]/td[2]/select/option[2]'))).click()
#Boton Buscar
WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/table/tbody/tr[4]/td/div[1]/div[4]/input'))).click()

time.sleep(20)
driver.quit()
#Tratamiento al excel
'''
df = pd.read_excel('D:\Marcos\\sirt.xlsx',skiprows=1,header=0)


####
def extraer_url(celda):
    if celda.has_attr('hyperlink'):
        return celda['hyperlink']
    else:
        return None
df['url'] = df['DETALLE FICHA INFORMATIVA'].apply(extraer_url)
####

df["nueva_columna"] = None
for i,valor in enumerate(df["DETALLE FICHA INFORMATIVA"]):

    try:
        #vinculo = serie.iloc[0]
        url = valor.get("href")
        df.at[i,"nueva_columna"] = url
    except AttributeError:
        df.at[i,"nueva_columna"] = valor

#def extract_link(cell):
#    return cell.get('href')

#df['link_column'] = df['DETALLE FICHA INFORMATIVA'].apply(extract_link)
print(df.head())
ruta_archivo = 'C:\\Users\\Julio-Gamer\\Downloads\\Busqueda_real_v2.xlsx'
df.to_excel(ruta_archivo,index=False)
'''