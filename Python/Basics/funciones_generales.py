#Las funciones generales son funciones creadas dentro de python que nos permiten realizar tareas especificas sin necesidad de crear la logica desde cero.

#map(funcion, iterable): La funcion map aplica una funcion especifica a cada elemento de un iterable (como una lista o tupla) y devuelve un objeto map (que es un iterable). Podemos convertir este objeto en una lista o tupla si es necesario.

myList = [1,2,3,4,5]

def multiplyBy3(number):
  return number * 3

#aplicando la funcion multiplyBy3 a cada elemento de myList usando map
result = map(multiplyBy3,myList)
#usando lambda para hacer lo mismo en una sola linea
resultTwo = map(lambda number: number * 3, myList)

print(f"El resultado de map es: {list(result)}")
print(f"El resultado de map con lambda es: {list(resultTwo)}")

#reduce(funcion, iterable): La funcion reduce aplica una funcion de manera acumulativa a los elementos de un iterable, reduciendolo a un solo valor. Esta funcion se encuentra en el modulo functools, por lo que debemos importarla antes de usarla.

from functools import reduce

myList = [1,2,3,4,5]

def sumTwoNumbers(accumulator, number):
  return accumulator + number


totalSum = reduce(sumTwoNumbers, myList)
#como se llego al resultado:
# Paso 1: accumulator = 1, number = 2 => resultado = 3
# Paso 2: accumulator = 3, number = 3 => resultado = 6
# Paso 3: accumulator = 6, number = 4 => resultado = 10
# Paso 4: accumulator = 10, number = 5 => resultado = 15


print(f"El resultado de reduce es: {totalSum}")

myString = ["Hola ", "mi ", "nombre ", "es ", "Python"]

#utilizando una funcion
myText = reduce(sumTwoNumbers, myString)
#utilizando una funcion lambda
myText = reduce(lambda accumulator, string: accumulator + string, myString)
print(f"El resultado de reduce es: ´{myText}´")

#Ejercicio 1 

# Dado una lista de numeros, utiliza la funcion reduce para encontrar el producto de todos los numeros en la lista. Muestra el resultado por consola.

#Ejercicio 2

# Dada una lista de palabras, utiliza la funcion reduce para concatenar todas las palabras en una sola cadena separada por espacios. Muestra el resultado por consola.

#Funciones para transformar datos

#int(): Convierte un valor a un entero.
#float(): Convierte un valor a un numero de punto flotante.
#str(): Convierte un valor a una cadena de texto.
#bool(): Convierte un valor a un booleano.
#list(): Convierte un valor iterable a una lista.
#tuple(): Convierte un valor iterable a una tupla.
#dict(): Convierte un valor iterable a un diccionario.

#int

print(int("123"))

#float

print(float("3.14"))
print(float(10))

#str

print(str(100) + " es un numero")
print(str(3.14) + " es un numero de punto flotante")

#bool

print(bool(1)) # True
print(bool(0)) # False
print(bool(3)) # True
print(bool("")) # False
print(bool("papata")) # True

#list
print(list((1,2,3))) # convierte una tupla en una lista
print(list("Hola que tal")) # convierte una cadena en una lista de caracteres

#tuple
print(tuple([1,2,3])) # convierte una lista en una tupla
print(tuple("Hola que tal")) # convierte una cadena en una tupla de caracteres

#dict
print(dict([("nombre", "Juan"), ("edad", 30)])) # convierte una lista de tuplas en un diccionario
print(dict(nombre="Maria", edad=25)) # crea un diccionario a partir de pares

"""
    +------------------------------------------------------------------------------------+
    |       Tabla de funciones generales en Python para la transformación de datos       |
    +-------------------+----------------------------------------------------------------+
    | Nombre            | Descripción                                                    |
    +-------------------+----------------------------------------------------------------+
    | bool()            | Convierte un valor en booleano.                                |
    | dict()            | Crea un nuevo diccionario.                                     |
    | float()           | Convierte un número o cadena en un número de punto flotante.   |
    | str()             | Convierte un objeto en una cadena.                             |
    | int()             | Convierte un número o cadena en un entero.                     |
    | list()            | Crea una lista.                                                |
    | tuple()           | Crea una tupla.                                                |
    | float()           | Convierte un número o cadena en un número de punto flotante.   |
    +-------------------+----------------------------------------------------------------+
"""

#Funciones para encontrar elementos en una coleccion

#max(): Devuelve el elemento con el valor máximo de una colección.

print(f"El elemento con el valor maximo es: {max([1676,225,378, 224,590])}")
print(f"El elemento con el valor maximo de un string es: {max(["H", "o", "l", "a", " ", "q", "u", "e", " ", "t", "a", "l"])}") # compara los caracteres segun su valor ASCII

#min(): Devuelve el elemento con el valor mínimo de una colección.

print(f"El elemento con el valor minimo es: {min([1676,225,378, 224,590])}")
print(f"El elemento con el valor minimo de un string es: {min(["H", "o", "l", "a", " ", "q", "u", "e", " ", "t", "a", "l"])}") # compara los caracteres segun su valor ASCII

#Funciones para realizar operaciones matematicas

#sum(): Suma todos los elementos de un iterable.

print(f"La suma de los elementos de la lista es: {sum([1,2,3,4,5])}")

#round(): Redondea un número al entero más cercano o a un número especificado de decimales.

print(f"El numero redondeado es: {round(3.14)}")


#Funciones para ordenar elementos

#sorted(): Devuelve una nueva lista ordenada a partir de los elementos de un iterable.

print(f"La lista ordenada es: {sorted([5,3,6,2,10,1,4,8,7])}")
print(f"La lista ordenada de strings es: {sorted([5,3,6,2,10,1,4,8,7], reverse=True)}") # orden descendente
print(f"La lista ordenada de strings es: {sorted(['banana', 'apple', 'orange', 'kiwi'])}")

#Funciones para contar elementos

#len(): Devuelve el número de elementos en un objeto.

print(f"La longitud de la lista es: {len([1,2,3,4,5])}")
print(f"La longitud del string es: {len('Hola que tal')}")

#Funciones para saber el tipo de dato

#type(): Devuelve el tipo de dato de un objeto.

patata = 123
print(f"El tipo de dato de la variable patata es: {type(patata)}")
print(f"El tipo de dato de la lista es: {type([1,2,3,4,5])}")
print(f"El tipo de dato del string es: {type('Hola que tal')}")
print(f"El tipo de dato del diccionario es: {type({'nombre': 'Juan', 'edad': 30})}")
print(f"El tipo de dato de la tupla es: {type((1,2,3))}")
print(f"El tipo de dato del conjunto es: {type(True)}")

#Funciones para rango

#range(): Genera una secuencia de números enteros en un rango especificado.

print(f"Los numeros del 0 al 9 son: {list(range(1,11))}")
print(f"Los numeros del 1 al 10 son: {list(range(1, 11, 2))}")

#Funciones para filtrar elementos

#filter(funcion, iterable): Filtra los elementos de un iterable que cumplen una condición especificada por una función.

numbers = [1,2,3,4,5,6,7,8,9,10]

def isEven(number):
  return number % 2 == 0

evenNumbers = filter(isEven, numbers)
print(f"Los numeros pares son: {list(evenNumbers)}")

#Otras funciones generales

#abs(): Devuelve el valor absoluto de un número.

print(f"El valor absoluto de -5 es: {abs(-5)}")

#all(): Devuelve True si todos los elementos de un iterable son verdaderos.

print(f"Todos los elementos de la lista son verdaderos: {all([True, True, True])}")
print(f"Todos los elementos de la lista son verdaderos: {all([True, False, True])}")
print(f"Todos los elementos de la lista son verdaderos: {all([1, 2, 3, 4])}")
print(f"Todos los elementos de la lista son verdaderos: {all([1, 0, 3, 4])}")

#any(): Devuelve True si al menos un elemento de un iterable es verdadero.

print(f"Al menos un elemento de la lista es verdadero: {any([True, False, True])}")
print(f"Al menos un elemento de la lista es verdadero: {any([False, False, False])}")
print(f"Al menos un elemento de la lista es verdadero: {any([0, 0, 3, 0])}")
print(f"Al menos un elemento de la lista es verdadero: {any([0, 0, 0, 0])}")

#eval(): Evalua una expresion y la ejecuta como codigo Python.

expression = "3 + 5 * 2"
print(f"El resultado de la expresion '{expression}' es: {eval(expression)}")

#exec(): Ejecuta un bloque de codigo Python.

code = "x = 10"
exec(code)
print(f"El valor de x es: {x}")

#enumerate(): Devuelve un objeto enumerado que contiene pares de indice y valor de un iterable.

fruits = ["apple", "banana", "orange", "kiwi"]

enumeratedFruits = enumerate(fruits)
print(f"Lista enumerada de frutas: {list(enumeratedFruits)}")


"""
    +------------------------------------------------------------------------------------+
    |             Tabla de funciones generales en Python (Las mas comunes)               |
    +-------------------+----------------------------------------------------------------+
    | Nombre            | Descripción                                                    |
    +-------------------+----------------------------------------------------------------+
    | max()             | Devuelve el elemento más grande.                               |
    | min()             | Devuelve el elemento más pequeño.                              |
    | sum()             | Devuelve la suma de los elementos.                             |
    | round()           | Redondea un número al entero más cercano.                      |
    | sorted()          | Devuelve una lista ordenada.                                   |
    | len()             | Devuelve la longitud de un objeto.                             |
    | type()            | Devuelve el tipo de un objeto.                                 |
    | range()           | Devuelve una secuencia de números.                             |
    | map()             | Aplica una función a cada elemento de una lista.               |
    | filter()          | Crea una lista con los elementos que cumplen cierta condición. |
    | abs()             | Devuelve el valor absoluto de un número.                       |
    | all()             | Devuelve True si todos los elementos de un iterable son True.  |
    | any()             | Devuelve True si algún elemento de un iterable es True.        |
    | eval()            | Evalúa una cadena como una expresión de Python.                |
    | hex()             | Convierte un número en una cadena hexadecimal.                 |
    | enumerate()       | Devuelve un objeto iterable que produce tuplas de índice/valor |
    +-------------------+----------------------------------------------------------------+
"""