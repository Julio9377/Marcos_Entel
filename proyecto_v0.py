import requests
import re
from bs4 import BeautifulSoup

# URL de la página web que quieres analizar
url = "https://www.entel.pe/empresas/catalogo/equipos/"

# Realizar una petición GET a la página web
response = requests.get(url)

# Convertir el contenido HTML en un objeto BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

divs = soup.find_all('div')

grupo_div = soup.find('div',class_='e-catalog-equipment__grid__list e-box-inline-block-ts e-box-inline-block--clear-tm')

lista = []

try:
    for div in grupo_div.find_all('div', recursive=False):
        href = div.div.a['href']
        if href=='javascript:void(0);':
            href = div.div['href']
            lista.append(href)
        else:
            href = div.div['href']
            lista.append(href)
        #print(href)
except AttributeError:
    pass
print(len(lista))
print(lista)
try:
    lista.remove("javascript:void(0);")
except AttributeError:
    pass
print(lista)
print(len(lista))

















#elementos = [div.get(strip=True) for div in grupo_div.find_all('div')]
#for elemento in elementos:
#    print(elemento)

#print(soup.find("div", class_="e-catalog-equipment__box e-catalog-equipment__box--counted").decompose())
