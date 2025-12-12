
#JavaScript Object Notation: Es un formato de datos para representar objetos y facilidad de compartirlos entre diferentes lenguajes de programación.
json = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

#Similar a un diccionario de Python
diccionario = {
   "name": "John",
  "age": 30,
  "city": "New York"
}

#Consumiendo nuestra primera API

#Request: libreria que nos permite consumir apis de forma sencilla

import requests

#get(url): Realiza una solicitud GET a la URL especificada y devuelve una respuesta

url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(url)

if response.status_code == 200:
  data =response.json()
  print("Nombre:", data["name"].capitalize())
  print("Peso:", data["weight"])
else:
  print("Error en la solicitud:", response.status_code)
  
#como manjear respuestas JSON

json_response ={
  "name": "Alejandro",
  "lastname": "Ramirez",
  "ocupation": [
    {
      "name": "Desarrollador",
      "level": "Junior"
    } # type: ignore
    ,
    {
      "name": "Profesional",
      "level": "Senior"
    } # type: ignore
  ]
}

print(json_response["ocupation"][0]["name"])

#Obtengamos el clima con la api de openMap

api_key = "Tu_api_key_aqui"
city = "Caracas"
lat = 10.4806
lon = 66.9036
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&lang=es&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
  print("Ciudad:", city)
  temp = data["main"]["temp"]
  print("Temperatura:", temp)
  clima = data["weather"][0]["description"].capitalize()
  print("Clima:", clima)
else:
  print("Error en la solicitud:", response.status_code)
  
  
#Ejercicio 1: Mi primera llamada (JSONPlaceholder)

"""  Objetivo: Realizar una petición GET simple y acceder a claves directas de un diccionario.
 API a usar: `https://jsonplaceholder.typicode.com/users/1`
 Instrucciones:
    1.  Importa la librería `requests`.
    2.  Realiza una petición GET a la URL indicada.
    3.  Verifica si el código de estado es `200`.
    4.  Si es correcto, imprime en consola el mensaje: "El usuario [Nombre] trabaja en la compañía [Nombre de la Compañía]".
    5.  Pista: El nombre de la compañía está anidado dentro de la clave `company`. """
    

url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)

if response.status_code == 200:
  response = response.json()
  print(f"El usuario {response['name']} trabaja en la compañía {response['company']['name']}")
else:
  print("Error en la solicitud:", response.status_code)