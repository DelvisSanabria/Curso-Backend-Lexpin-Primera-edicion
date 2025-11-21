#try-except 

#es una estrucutura de control de flujo que nos permite manejar errores y excepciones en nuestro código de manera elegante.

#Sintaxis básica

""" 
try:
    # Código que puede generar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    # Código para manejar la excepción
    print("No se puede dividir por cero")
"""

def divider(a, b):
    try:
      #En este bloque intentamos ejecutar el código que puede generar una excepción
        return print("El resultado es:", a / b)  # Dividimos a / b
    except ZeroDivisionError:
        return print("No se puede dividir por cero")
    except TypeError:
        return print("Los operandos deben ser números")
    finally:
        print("La funcion termino")
    
  
divider(5, 5)  # Esto generará una excepción de división por cero
divider(5, 0)  # Esto generará una excepción de división por cero
divider(5, 'a')  # Esto generará una excepción de tipo

print("El programa continúa ejecutándose después del error.")

def convert_to_int(value):
    try:
        convert = int(value)
    except ValueError:
        print(f"No se puede convertir '{value}' a entero.")
    else:
        print(f"La conversión de '{convert}' fue exitosa.")
        return convert
    finally:
        print("Intento de conversión finalizado.")
    
print(convert_to_int("123"))  # Debería imprimir 123
print(convert_to_int("ab4y55c"))  # Debería manejar el error y devolver None

#Error de indice

try: 
  listItem = [1, 2, 3]
  element = listItem[1]  # Intentamos acceder a un índice que no existe
except IndexError:
  print("Índice fuera de rango.")
else:
  print("Elemento en el índice elegido es:", element)
finally:
  print("El bloque finally se ejecuta siempre.")
  
#Ejercicio práctico

#Crea una función que tome una lista de números y devuelva la suma de todos los números en la lista.
#La función debe manejar posibles excepciones, como si la lista contiene elementos que no son números

def sum_numbers(number_list):
    total = 0
    for num in number_list:
        try:
            total += int(num)  # Intentamos convertir cada elemento a float y sumarlo
        except ValueError:
            print(f"El elemento '{num}' no es un número y será ignorado.")
    return total
  
result = sum_numbers([1, 2, 'a', 4, '5b', 6])  # Debería manejar los errores y devolver la suma de los números válidos

#Utilizar filter y reduce para filtrar y sumar los números válidos en la lista
from functools import reduce
def is_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

filtered_numbers = filter(is_number, [1, 2, 'a', 4, '5b', 6])
result = reduce(lambda x, y: x + y, filtered_numbers) # type: ignore
print("La suma de los números válidos es:", result)