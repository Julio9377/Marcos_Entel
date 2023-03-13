import pandas as pd
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

options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disablevicibox-extensions')
options.add_argument("--disable-extensions")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(r"D:\ChromeDriver\chromedriver.exe",chrome_options=options)

df = pd.read_excel('D:\Marcos\\osiptel.xlsm',skiprows=1,header=0)

#print(df.head())

df_filtrado = df[df['CESE'] == "No"]

columna = df_filtrado['LINKS'].tolist()

Lista_Codigo = []
Lista_Empresa = []
Lista_Nombre = []
Lista_Valor = []
Lista_Velocidad = []
#columna = ['https://serviciosweb.osiptel.gob.pe/ConsultaSIRT/Buscar/FrmVerTarifa.aspx?pTarifa=218867']
for url in columna:
    driver.get(url)
    Codigo = driver.find_element(By.XPATH,'/html/body/form/div[3]/table[1]/tbody/tr[5]/td[2]/table/tbody/tr/td[3]/span')
    Lista_Codigo.append(Codigo.text)
    #print(Lista_Codigo)
    Empresa = driver.find_element(By.XPATH,'/html/body/form/div[3]/table[1]/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/span')
    Lista_Empresa.append(Empresa.text)
    #print(Lista_Empresa)
    Nombre = driver.find_element(By.XPATH,'/html/body/form/div[3]/table[1]/tbody/tr[6]/td[2]/table/tbody/tr/td[3]/span')
    Lista_Nombre.append(Nombre.text)
    #print(Lista_Nombre)
    try:
        Valor = driver.find_element(By.XPATH,'/html/body/form/div[3]/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/span')
        Lista_Valor.append(Valor.text)
        #print(Lista_Valor)
    except NoSuchElementException:
        #Valor = str('')
        Lista_Valor.append('')
        #print(Lista_Valor)
    #Valor = driver.find_element(By.XPATH,'/html/body/form/div[3]/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/span')
    #Lista_Valor.append(Valor.text)
    #print(Lista_Valor)
    try:
        Velocidad = driver.find_element(By.ID,'lblDVelMaxInt')
        Lista_Velocidad.append(Velocidad.text)
        #print(Lista_Velocidad)
    except NoSuchElementException:
        #Velocidad = str('')
        Lista_Velocidad.append('')
        #print(Lista_Velocidad)
    #print(Lista_Velocidad)
#print(df.head())
#print(columna)
df0 = pd.DataFrame(Lista_Codigo,columns=["Codigo"])
df1 = pd.DataFrame(Lista_Empresa,columns=["Nombre Empresa"])
df2 = pd.DataFrame(Lista_Nombre,columns=["Nombre"])
df3 = pd.DataFrame(Lista_Valor,columns=["Monto"])
df4 = pd.DataFrame(Lista_Velocidad,columns=["Velocidad"])

df_unido = pd.concat([df0,df1,df2,df3,df4],axis=1)
df_unido.to_excel('D:\Marcos\\osiptel_resultado.xlsx',index=False)
#print(df_unido.head())