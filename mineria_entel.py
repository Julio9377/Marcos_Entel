from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import datetime
import time

options = Options()
options.set_preference("dom.webnotifications.enabled", False)
options.set_preference("permissions.default.desktop-notification", 2)
options = webdriver.FirefoxOptions()
options.add_argument("--disable-notifications")
# abrir el sitio web con Selenium
driver = webdriver.Firefox(options=options)
driver.get("https://www.entel.pe/empresas/catalogo/equipo/samsung-galaxy-a53/?modalidad=migra&forma_pago=contado")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))).click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/section[1]/div/div[3]/div[2]/div[1]/form/div[2]/div[2]/div/div[1]/a'))).click()

#39.9
precio_39 = driver.find_element("xpath",'/html/body/div[4]/div[1]/section[1]/div/div[3]/div[2]/div[1]/form/div[2]/div[2]/div/div[1]/ul/li[1]').text
print(precio_39)    
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/section[1]/div/div[3]/div[2]/div[1]/form/div[2]/div[2]/div/div[1]/ul/li[1]'))).click()
Equipo_39 = driver.find_element("xpath",'/html/body/div[4]/div[1]/section[1]/div/div[3]/div[2]/div[2]/div[4]/div/div[1]/div[3]/div[3]/div').text
print(Equipo_39)
resumen_39 = driver.find_element("xpath",'/html/body/div[4]/div[1]/section[1]/div/div[3]/div[2]/div[2]/div[4]/div/div[1]/div[4]').text
print(resumen_39)

#55.9
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/section[1]/div/div[3]/div[2]/div[1]/form/div[2]/div[2]/div/div[1]/ul/li[2]'))).click()

Equipo_55 = driver.find_element("xpath",'/html/body/div[4]/div[1]/section[1]/div/div[3]/div[2]/div[2]/div[4]/div/div[1]/div[3]/div[3]/div').text
print(Equipo_55)   
#74.9
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/section[1]/div/div[3]/div[2]/div[1]/form/div[2]/div[2]/div/div[1]/ul/li[3]'))).click()
#89.9
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/section[1]/div/div[3]/div[2]/div[1]/form/div[2]/div[2]/div/div[1]/ul/li[4]'))).click()