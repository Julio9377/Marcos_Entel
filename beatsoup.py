import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
url = 'https://serviciosweb.osiptel.gob.pe/ConsultaSIRT/Buscar/frmConsultaTar.aspx'
driver.get(url)

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

print('Ingresando al iframe')
iframe = driver.find_element(By.TAG_NAME,'iframe')
iframe_url = iframe.get_attribute('src')
driver.switch_to.frame(iframe)
#Asignar Tabla a Leer
time.sleep(10)
WebDriverWait(driver, 25)\
.until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/div[3]/div/div[5]/div/table/tbody/tr/td[2]/table/tbody/tr/td[8]/select/option[4]'))).click()
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')

#iframe = soup.find("iframe")["src"]
#iframe_response = requests.get(iframe)
#iframe_soup = BeautifulSoup(iframe_url.content, "html.parser")

table = soup.find("table")
print(table)
print("-----")
rows = []
rows = table.find_all("tr")
filas = []
print(rows)
for row in rows:
    cells = row.find_all("td")
    celdas = []
    for cell in cells:
        celdas.append(cell.text)
    filas.append(celdas)
    print(filas)
for fila in filas:
    for celda in fila:
        print(celda)
print("what")
