from bs4 import BeautifulSoup as bs
import requests

with open("Python/especializado/web_scrapping/html/index_semantico.html", "r") as html_file:
  soup = bs(html_file, "html.parser")
  """ .prettify nos permite formatear el html y mostrarlo por consola """
  """ print(soup.prettify()) """
  titles = soup.find_all("h2")
  
  for title in titles:
    """ .text nos permite obtener el texto de la etiqueta """
    print(title.text)
    
#scrappear una pagina web

headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...",
    "Accept-Language": "es-ES,es;q=0.9",
}

url = "https://www.amazon.com/s?k=laptops&page=2&xpid=_xtZ5Lqei2ulV&crid=2MWOYLCSD0M2F&qid=1766012267&sprefix=laptops%2Caps%2C427&ref=sr_pg_2"

response = requests.get(url, headers=headers)

soup = bs(response.text, "html.parser")

products = soup.find_all("div", {"class":"a-section"})
print(len(products))

for product in products:
  try:
    name = product.find("h2", {"class":"a-size-medium a-spacing-none a-color-base a-text-normal"}).text
    price = product.find("span", {"class":"a-offscreen"}).text
    print(f"El nombre del producto es: {name} y su precio es: {price}")
  except:
    continue


#ejercicio 

""" 
Enunciado:

scrapper titular y descripcion especificada en WhatsApp de la pagina: https://wuau.marketing/

y mostrarlo por consola
"""

url = "https://wuau.marketing/"
response = requests.get(url)
soup = bs(response.text, "html.parser")

print(soup.prettify())