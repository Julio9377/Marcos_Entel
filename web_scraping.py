from selenium import webdriver
from bs4 import BeautifulSoup

# abrir el sitio web con Selenium
driver = webdriver.Firefox()
driver.get("https://www.entel.pe/empresas/catalogo/equipos/")

# analizar el HTML con BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

# buscar todas las etiquetas "div" con la clase "product-card"
celulares = soup.find_all("div", class_="product-card")

# imprimir los datos de cada celular
for celular in celulares:
    nombre = celular.find("h3").text
    precio = celular.find("span", class_="price").text
    print(nombre + " - " + precio)

# cerrar el sitio web con Selenium
driver.quit()
