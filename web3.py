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

# Localizar la lista
lista = driver.find_elements(By.XPATH,'/html/body/div[4]/div[1]/section[1]/div/div[3]/div[2]/div[1]/form/div[2]/div[2]/div/div[1]/ul')



# Iterar a través de los elementos hijos de la lista
for elemento in lista:
    print(elemento.text)


    
