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
'''
WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/table/tbody/tr[4]/td/table[1]/tbody/tr/td/div/table[1]/tbody/tr[8]/td[2]/table/tbody/tr[1]/td[1]/input'))).send_keys("01012018",Keys.ENTER)
'''
#Periodo-Vigencia -->01/01/2018
'''
date =  WebDriverWait(driver, 10)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/table/tbody/tr[4]/td/table[1]/tbody/tr/td/div/table[1]/tbody/tr[8]/td[2]/table/tbody/tr[1]/td[1]/input'))).send_keys("01012018",Keys.ENTER)
'''
time.sleep(2)
#Convergente/Empaquetado --> Convergente
WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/table/tbody/tr[4]/td/table[1]/tbody/tr/td/div/div/table/tbody/tr[1]/td[2]/select/option[2]'))).click()
#Alcance --> Empresarial
WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/table/tbody/tr[4]/td/table[1]/tbody/tr/td/div/div/table/tbody/tr[4]/td[2]/select/option[2]'))).click()
#Boton Buscar
WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/table/tbody/tr[4]/td/div[1]/div[1]/img'))).click()

#Ingresando al Iframe -
print('Ingresando al iframe')
time.sleep(5)

iframe = driver.find_element(By.TAG_NAME,'iframe')
##doc = driver.execute_script("return arguments[0].contentDocument", iframe)
iframe_url = iframe.get_attribute('src')
driver.switch_to.frame(iframe)

#Asignar Tabla a Leer
WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/div[3]/div/div[5]/div/table/tbody/tr/td[2]/table/tbody/tr/td[8]/select/option[4]'))).click()
#Ordenar Iframe
WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/div[3]/div/div[3]/div[2]/div/table/thead/tr/th[15]/div'))).click()

########Ciclo comienza
Lista_Empresa = []
Lista_Nombre = []
Lista_Valor = []
Lista_Velocidad = []


table = driver.find_element(By.ID,'dataGrid')
rows = table.find_elements(By.TAG_NAME,'tr')

for row in rows:
    wait = WebDriverWait(driver,10)
    td_list = driver.find_elements(By.XPATH,'//td[@title="No"]')
    print(td_list)
    #td_list = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//td[@title="No"]')))
    #temp_list = list(td_list)
    for td in range(len(td_list)):
        print(str(range(len(td_list))))
        print(str(td).text)
        time.sleep(3)
        try:
            print(td_list[td].text)
        except StaleElementReferenceException:
            while True:
                try:
                    time.sleep(1)
                    td_list = driver.find_elements(By.XPATH,'//td[@title="No"]')
                    
                    #print(td_list[td].text)
                    #td = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//td[@title="No"]')))
                    #td = driver.find_element(By.XPATH,'//td[@title="No"]')
                    break
                except StaleElementReferenceException:
                    continue
        try:        
            td_element = driver.find_element(By.CSS_SELECTOR,'td[aria-describedby="dataGrid_Detalles"]')
            #td_element.click()
        except NoSuchElementException:
            print("No se encontro")
            time.sleep(5)
            td_element = driver.find_element(By.CSS_SELECTOR,'td[aria-describedby="dataGrid_Detalles"]')
            #td_element.click()
        
        link_element = td_element.find_element(By.CSS_SELECTOR,'a')
        link_element.click()
        #WebDriverWait(driver, 5)\
        #                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'td:nth-child(23) > a'))).click() 
        time.sleep(4)
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        '''
        Empresa = driver.find_element(By.XPATH,'/html/body/form/div[3]/table[1]/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/span')
        Lista_Empresa.append(Empresa.text)
        print(Lista_Empresa)
        Nombre = driver.find_element(By.XPATH,'/html/body/form/div[3]/table[1]/tbody/tr[6]/td[2]/table/tbody/tr/td[3]/span')
        Lista_Nombre.append(Nombre.text)
        print(Lista_Nombre)
        Valor = driver.find_element(By.XPATH,'/html/body/form/div[3]/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/span')
        Lista_Valor.append(Valor.text)
        print(Lista_Valor)
        Velocidad = driver.find_element(By.ID,'lblDVelMaxInt')
        Lista_Velocidad.append(Velocidad.text)
        print(Lista_Velocidad)
        '''
        driver.close()
        driver.switch_to.window(handles[0])
    

print('pasooo')
time.sleep(5200)
#df = pd.DataFrame(table)
#print(df.head())


