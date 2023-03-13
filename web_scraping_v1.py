from asyncio import sleep
from typing import Sized
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, TimeoutException
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

#ruta_1001 = 'D:\\4.CLARO\\0. IVR\\'+datetime.now().strftime("20%y%m%d")+'\\1001.xlsx'
#ruta_1 = 'D:\\4.CLARO\\0. IVR\\'+datetime.now().strftime("20%y%m%d")

options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disablevicibox-extensions')    

driver = webdriver.Chrome(r"D:\ChromeDriver\chromedriver.exe",chrome_options=options)

# Inicializamos el navegador
Lista = ['samsung-galaxy-a53','motorola-moto-g31','zte-blade-v30-vita','samsung-galaxy-s21-fe-128gb','oppo-a54','samsung-galaxy-a03-core']
url_base = 'https://www.entel.pe/empresas/catalogo/equipo/'
url_params = '/?modalidad=migra&forma_pago=contado'
urls=[]
for item in Lista:
    url = url_base + item + url_params
    urls.append(url)
#print(urls)

for url in urls:
    driver.get(url) # Entramos URL x URL
    uls=[]
    uls = driver.find_elements(By.CSS_SELECTOR,'#vc-view-planes > div.dropdown > ul.js-dropdown-list')
    print(uls[0].text)
    for ul in uls:
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div[1]/section[1]/div/div[3]/div[2]/div[1]/form/div[2]/div[2]/div/div[1]/a'))).click()
        ul.click()
        ActionChains(driver).move_to_element(ul).click(ul).perform()    
        Resumen = driver.find_element("xpath",'/html/body/div[4]/div[1]/section[1]/div/div[3]/div[2]/div[2]/div[4]/div/div[1]').text
        print(Resumen)
        print('ok-for_2')
    print('ok-Todo')

driver.quit()



'''
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,'/html/body/center/table[1]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/font/a')))\
    .click()
'''
#/html/body/div[4]/div[1]/section[1]/div/div[3]/div[2]/div[1]/form/div[2]/div[2]/div/div[1]/ul