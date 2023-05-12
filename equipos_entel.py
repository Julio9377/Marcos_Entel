import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página web que quieres analizar
url = "https://www.entel.pe/empresas/catalogo/equipos/"

# Realizar una petición GET a la página web
response = requests.get(url)

# Convertir el contenido HTML en un objeto BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
print("**********")
#rint(soup.body.string)
print(soup.body.decompose())
#print(len(soup.body.contents))
#print((soup.body.contents[0].string))
#print((soup.body.contents[1].string))
tag = soup.find_all(attrs={"data-marca":"Samsung"},limit=1)
#print(len(soup.find_all(attrs={"data-marca":"Samsung"})))
#tag_2 = soup.div
#print(tag)
#print(tag_2)
print("**********")
#soup.find_all
#print(soup.find_all(attrs={"data-marca":"Samsung"},limit=1))

#print((soup.body.name))
#print(soup.body.div)
print("**********")
#texto = soup.find(id="e-empresas e-page-main e-empresas__catalog e-catalog-equipment e-empresas__page-data--js")
#lista = []
#xd = texto.get_text()#.replace("\n"," ").replace("\t\t","").replace("Lanzamiento     ","\n").replace("Exclusivo online     ","\n")

#lista.append(xd)
#df = pd.DataFrame(lista,columns=["General"])
#df.to_csv("D:\\Datos_Entel.txt",index=False)
#print(texto)
#print(type(texto))