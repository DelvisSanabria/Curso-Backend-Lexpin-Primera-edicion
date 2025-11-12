## Comentarios de una sola linea

"""

Hola
este es un comentario de varias
lineas

"""

# Variables Estructura : Nombre = Valor

""" En python tendremos los tipos de datos mas basicos que podemos guardar
    estos son datos primitivos
    String, Int, Float, Boolean
"""

name = "delvis" # String
precioTotal = 100 # Int
costo = 50.5 # Float
estaDespierto = True # Boolean

#Tipos de datos

#String - Texto sirven para guardar cadenas de texto
nameTwo = "Ivan"
nameThree = 'Sofia'

#Para mostrar por consola usaremos la funcion (Metodo) print
print("Variables de texto:")
print(type(nameTwo))
print(type(nameThree))


#Int - Numeros enteros Nos sirven para guardar numeros enteros

num1 = 10
num2 = -20
num3 = 0
print("Variables de enteros:")
print(type(num1))
print(type(num2))
print(type(num3))

#Float - Numeros reales Nos sirven para guardar numeros reales
num4 = 10.5
num5 = -20.5
num6 = 0.0
print("Variables de reales:")
print(type(num4))
print(type(num5))
print(type(num6))

#Bool - Booleanos Nos sirven para guardar verdadero o falso
estaDespierto = True
estaDormido = False
print("Variables de booleanos:")
print(type(estaDespierto))
print(type(estaDormido))

#List - Listas Nos sirven para guardar una coleccion de datos
lista = [1, 2, 3, 4, 5, [1, 2, 3, 4, 5]]
names = ["delvis", "Ivan", "Sofia","Andreina"]
print("Variables de listas:")
print(type(lista))
print(type(names))
print(names)

#tuple - Tuplas Nos sirven para guardar una coleccion de datos
tupla = (1, 2, 3, 4, {"name": "delvis", "age": 20, "city": "Css"}, [1, 2, 3, 4, 5]) # Las tuplas son inmutables
print("Variables de tuplas:")
print(type(tupla))

#dict - Diccionarios Nos sirven para guardar una coleccion de datos
diccionario = {"name": "delvis", "age": 20, "city": "Css"}
print("Variables de diccionarios:")
print(type(diccionario))

#Ejercicio


#Crear una variable de apellido con un valor
lastname = "Sanabria"

#Crear una variable de nombres con un valor
names = ["Delvis", "Hugo", "Jesus", "Alejandro"]

#Crear una variable de edad con un valor
age = 24

#Crear una variable de ciudad con un valor
city = "Css"

#Crear una variable de pais con un valor
country = "Venezuela"

#Crear una variable de ciudades con varios valores 
cities = ["Css", "Valencia", "Maracaibo"]

#Crear una variable de paises con varios valores
countries = ["Venezuela", "Colombia", "Brasil"]

#Crear una variable de colores con varios valores
colors = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}

#Crear una variable de ciudades y paises con varios valores
citiesAndCountries = {"Venezuela": "Caracas", "España": "Barcelona", "Colombia ": "Bogota"}
citiesAndCountries = [
    {"country": "Venezuela", "city": "Caracas"},
    {"country": "España", "city": "Barcelona"},
    {"country": "Colombia", "city": "Bogota"},
]

#Crear una variable de colores con nombre y tonalidad

colors = {"red":"tone: #FF0000","green":"tone: #00FF00","blue":"tone: #0000FF"}
