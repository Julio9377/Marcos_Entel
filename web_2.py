from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
options = webdriver.FirefoxOptions()
options.add_argument("--disable-notifications")

# abrir el sitio web con Selenium
driver = webdriver.Firefox(options=options)
driver.get("https://www.entel.pe/empresas/catalogo/equipo/samsung-galaxy-a53/?modalidad=migra&forma_pago=contado")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))).click()

wait = WebDriverWait(driver, 10)
elemento_esperado = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "html > body > div:nth-of-type(4) > div:nth-of-type(1) > section:nth-of-type(1) > div > div:nth-of-type(3) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(4) > div > div:nth-of-type(1)")))



# analizar el HTML con BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")
elemento = BeautifulSoup(driver.page_source, "html.parser")
wait = WebDriverWait(driver, 10)

lista_precios = soup.select_one("html > body > div:nth-of-type(4) > div:nth-of-type(1) > section:nth-of-type(1) > div > div:nth-of-type(3) > div:nth-of-type(2) > div:nth-of-type(1) > form > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(1) > ul")

elemento_adicional = elemento.select_one("html > body > div:nth-of-type(4) > div:nth-of-type(1) > section:nth-of-type(1) > div > div:nth-of-type(3) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(4) > div > div:nth-of-type(1)")

# buscar todos los elementos de la lista
for elemento in lista_precios:
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/section[1]/div/div[3]/div[2]/div[1]/form/div[2]/div[2]/div/div[1]/a'))).click()
    #driver.refresh()
    print(" ".join(elemento.text.split()))
    driver.refresh()
    print("-----------")
    # imprimir el texto del elemento adicional
    time.sleep(5)
    print(" ".join(elemento_adicional.text.split()))
    print("**********")

# buscar la tabla de precios
#tabla_precios = soup.find("table", class_="table-price")


'''
# buscar todas las filas de la tabla
filas = tabla_precios.find_all("tr")

# recorrer cada fila
for fila in filas:
    # buscar las columnas de la fila
    columnas = fila.find_all("td")
    # si la fila tiene 2 columnas es un plan de contrato
    if len(columnas) == 2:
        plan = columnas[0].text
        precio = columnas[1].text
        print(plan + " - " + precio)

# cerrar el sitio web con Selenium
driver.quit()
'''