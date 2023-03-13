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
archivo_exportado = "D:\\Marcos\\exportado2.csv"
# Inicializamos el navegador
Lista = ['oppo-a54','samsung-galaxy-s21-fe-128gb','iphone-13-pro-max-128gb','samsung-galaxy-a53']
#Lista = ['samsung-galaxy-a53','motorola-moto-g31','zte-blade-v30-vita','samsung-galaxy-s21-fe-128gb','oppo-a54','samsung-galaxy-a03-core','iphone-14-128gb','iphone-13-pro-max-128gb','vivo-v21','iphone-13-pro-128gb','vivo-y-21s','vivo-y-53s','iphone-14-256gb','iphone-14-512gb','iphone-14-plus-256gb','iphone-14-pro-256gb','xiaomi-redmi-10-2022','huawei-nova-9','zte-blade-a51','oppo-reno-7','iphone-13-512gb','iphone-13-pro-512gb','samsung-galaxy-z-fold-4-256gb','samsung-galaxy-z-flip-4-128gb','samsung-galaxy-z-flip-4-256gb','redmi-10c','redmi-note-11s','zte-blade-a31-plus-32gb','honor-x7','samsung-galaxy-s22','poco-m4-pro-128gb-5g','oppo-a77','honor-50-256gb','zte-blade-a5-2020-32gb','honor-70-128gb','samsung-galaxy-s22-ultra','samsung-galaxy-a52s','honor-x8','huawei-nova-y70','samsung-galaxy-a23','xiaomi-redmi-10a','vivo-y55','motorola-moto-g50','iphone-12-64gb','xiaomi-11-t','iphone-13-256gb','motorola-e-20','oppo-a-16','xiaomi-redmi-note-11-128gb','apple-iphone-se-2022-64gb','galaxy-a13','iphone-13-mini-128gb','honor-x9','zte-a51-lite','honor-x8-pack','samsung-galaxy-a03s','iphone-13-128gb','edge-30-fusion-audifonos','edge-30-neo','edge-30-neo-audifonos','galaxy-a04e','motorola-moto-edge-30-pro-5g','iphone-14-plus-128gb','iphone-14-pro-128gb','iphone-14-cargador','iphone-14-plus-airpods','apple-iphone-11-64gb','honor-70-256gb-earbuds-x','samsung-galaxy-s20-fe-5g','motorola-moto-g22','vivo-y22s','samsung-galaxy-a22-64','samsung-galaxy-a33','xiaomi-redmi-10c-364gb','samsung-galaxy-a04','galaxy-s22-ultra-256gb','redmi-note-11s-128gb-5g','oppo-a57-128gb','honor-x6']
url_base = 'https://www.entel.pe/empresas/catalogo/equipo/'
url_params = '/?modalidad=migra&forma_pago=contado'
urls=[]
datos = []
for item in Lista:
    url = url_base + item + url_params
    urls.append(url)
#print(urls)

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
        print('------')
        print('------')
        print('------')
        #print('Equipo Celular '+ str(item))
        time.sleep(1)
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        if element.is_displayed():
            ActionChains(driver).move_to_element(element).click(element).perform() 
        scrap = []
        scrap = driver.find_elements(By.CSS_SELECTOR,'#vc-view-forma-pago > div > div')
        print('Cuenta con '+str(len(scrap))+ ' opciones')
        for i in range(len(scrap)):
            print('------')
            try:
                scrap[i].click()
            except StaleElementReferenceException:
                while True:
                    try:
                        time.sleep(1)
                        #scrap = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#vc-view-forma-pago > div > div')))
                        scrap = driver.find_elements(By.CSS_SELECTOR,'#vc-view-forma-pago > div > div')
                        scrap[i].click()
                        break
                    except StaleElementReferenceException:
                        continue
            Resumen = driver.find_element("xpath",'/html/body/div[4]/div[1]/section[1]/div/div[3]/div[2]/div[2]/div[4]/div/div[1]').text
            Resumen2 = Resumen.replace("\n"," ").replace("\s+"," ").replace(" RESUMEN DE PEDIDO ","")\
                            .replace("Equipo: Cantidad de equipos 1","").replace(" Precio total del equipo","|CONTADO|").replace("CUOTA INICIAL:","|CUOTA|").replace("44% dto. EXCLUSIVO ONLINE","").replace("S/","").replace("Plan: Empresario Full+","*").replace(" Chip y delivery: GRATIS","")
            datos.append(Resumen2)
            print(datos)
            print('')
        ###Buscar 12 cuotas / 18 cuotas y extraer Resumen
        print('-----')
        print('-----')
        print('-----')
    print('ok-URL')

df = pd.DataFrame(datos,columns=["General"])
df["General"] = df["General"].str.replace("\s+"," ")
df = df.assign(Equipo=df.General.str.split('|').str[0],Plan=df.General.str.split('|').str[1],Tipo=df.General.str.split(' ').str[3],Modo_Cobro=df.General.str.split(' ').str[4],Contado_CuotaInicial=df.General.str.split(' ').str[5],ContadoOnline_CantidadCuota=df.General.str.split(' ').str[6])
df = df.assign(CONTADO_CUOTAS=df.Plan.str.split('*').str[0],Plan_Tarifario=df.Plan.str.split('*').str[1])
df["Plan_Tarifario"] = df["Plan_Tarifario"].str.split(" Dto.").str[0]
df["CONTADO_CUOTAS"] = df["CONTADO_CUOTAS"].str.split(" CUOTAS DE: ").str[1]
df[['Equipo','Modo_Cobro','Contado_CuotaInicial','ContadoOnline_CantidadCuota','CONTADO_CUOTAS','Plan_Tarifario']].to_csv(archivo_exportado,index=False)
print(df.head())
driver.quit()
