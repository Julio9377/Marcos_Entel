import requests
import re
from bs4 import BeautifulSoup

# URL de la página web que quieres analizar
url = "https://www.entel.pe/empresas/catalogo/equipos/"

# Realizar una petición GET a la página web
response = requests.get(url)

# Convertir el contenido HTML en un objeto BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar todas las etiquetas HTML en la página
div = soup.find('div', {'class': 'e-catalog-equipment__grid__list e-box-inline-block-ts e-box-inline-block--clear-tm'})

etiquetas = div.find_all()

etiquetas_lista  = []
# Imprimir las etiquetas encontradas

for etiqueta in etiquetas:
    
    etiquetas_lista.append(etiqueta)

print(len(etiquetas_lista))
##print(etiquetas_lista[1])

cadena = etiquetas_lista[1]
print(cadena)
print(type(cadena))
  
