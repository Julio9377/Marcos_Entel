import requests
from bs4 import BeautifulSoup

# URL de la página web que quieres analizar
url = "https://www.entel.pe/empresas/catalogo/equipos/"

# Realizar una petición GET a la página web
response = requests.get(url)

# Convertir el contenido HTML en un objeto BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar todas las etiquetas HTML en la página
divs = soup.find_all('div', {'class': 'e-catalog-equipment__box e-catalog-equipment__box--counted'})

contenido_divs  = []
# Imprimir las etiquetas encontradas

for div in divs:
    
    contenido_divs.append(div)

print(len(contenido_divs))
print(contenido_divs[1])
