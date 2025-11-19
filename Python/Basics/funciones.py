#Las funciones son bloques de codigo reutilizables, que nos permiten realizar tareas especificas


#Definir una funcion
def sayHello():
  print("Hola Mundo")
  
#llamar a una funcion
#sayHello()

#Scope

#Variable global puede ser accedida desde cualquier parte del codigo
variable = 10

#funcion sin parametros
def sayHelloAndShowVariable():
  print("Hola muchachos")
  print(variable)
  #varible local no puede ser accedida desde cualquier parte del codigo
  variableDos = 20
  print("estoy pintnando la variableDos desde dentro de la funcion", variableDos)
  
sayHelloAndShowVariable()

#print("estoy pintnando la variableDos desde fuera de la funcion", variableDos)

#funcion con parametros
def sum(num1, num2):
  print("El resultado de la suma es: ", num1 + num2)
  
sum(2,3)
sum(4,5)
sum(6,7)

#Podemos crear funciones que reciban parametros(variables) para ser usados dentro de la funcion para realizar alguna tarea estos parametros son leidos por posicion de izquierda a derecha

#la estructura de una funcion con parametros es la siguiente : def nombreFuncion(parametro1, parametro2):
def sayHelloUser(name):
  print(f"Hola {name}")
  
sayHelloUser("Delvis")
sayHelloUser("Andreina")
sayHelloUser("Eduardo")

#crear una funcion saludo que salude a una persona por su nombre y apellido y mostrar el resultado por consola

#podemos definir parametros con valores por defecto para que en caso de no recibir un valor se use el valor por defecto
def saludo(name, lastname = "", country = "Venezuela"):
  print(f"Hola {name} {lastname}, soy de {country}")
  
saludo("Delvis", "Sivira")
saludo("Andreina", "Sanabria", "Colombia")
saludo("Eduardo", "Sanabria")

def sumTwoNumbers(num1, num2):
  result = num1 + num2
  #Solo hay un return y solo se puede delvover un valor
  return result  

sumResult = sumTwoNumbers(2, 3)
print(sumResult)

#Ejercicio
# Enunciado:  
# Define una función "calculator", que reciba dos numeros, y el tipo de operacion y segun el tipo de operacion la realice y retorne el resultado. luego muestra el resultado por consola

#definimos la funcion con retorno
def calculator(num1, num2, operation):
  if operation == "+":
    return num1 + num2
  elif operation == "-":
    return num1 - num2
  elif operation == "*":
    return num1 * num2
  elif operation == "/":
    return num1 / num2
  
result = calculator(1,2,"*") # 2
print(result)

#Tipos de funciones

#Funcion lambda

#son funciones anonimas que nos permiten crear funciones en una sola linea

#estructura: variable = lambda parametros : operacion

sum = lambda num1, num2: print("El resultado de la suma es: ", num1 + num2)

sum(1,2)
  
#Ejercicio 1 (si estas viendo la grabacion has esto y envialo 🥰)
#Crear una funcion lambda que salude 

name = lambda name: print(f"Hola {name} como estas?")

#Funciones Callbacks 
#Son funciones que se pasan como parametro a otras funciones

#Ejemplo

def process(list, callback):
  """ process recibira una lista de elementos y una funcion (callback)
      para cada uno de los elementos dentro de la lista, aplicara esa funcion que le pasamos
      y asi delvolvera una nueva lista con los elementos transformados
  """
  return [callback(item) for item in list]
  """ este return nos devuelve una nueva lista que aplica un for a la lista original y transforma cada elemento con la funcion que le pasamos """

numbers = [1,2,3,4,5,6,7,8,9,10]
result = process(numbers, lambda item: item * 2)
print(result)

#Ejercicio 2
#Crear una funcion que reciba una lista de numeros y una funcion callback
#y devuelva una nueva lista con los numeros transformados divididos entre 2 y luego mostrar los primos y no primos segun la funcion callback

def primeNumbers(number):
  if number <=1:
    return f"El numero {number} no es primo"
  for i in range(2, number):
    if number % i == 0:
      return f"El numero {number} no es primo"
  return f"El numero {number} es primo"

print(primeNumbers(7))

def transformAndClasificate(list, callback):
  transformList= [int(n/2)for n in list]
  for i in transformList:
    print(callback(i))
    
listOfNumbers = [1,2,3,4,5,6,7,8,9,10]
transformAndClasificate(listOfNumbers, primeNumbers)


def primeNumbersAle(number):
  if number <=1:
    return False
  for i in range(2, number):
    if number % i == 0:
      return False
  return True

def transformAndClasificateAle(list, callback):
  
  transformList= [int(n/2)for n in list]
  prime = [n for n in transformList if callback(n)]
  notPrime = [n for n in transformList if not callback(n)]
  print(f"Los numeros primos son: {prime}")
  print(f"Los numeros no primos son: {notPrime}")
    
listOfNumbers = [1,2,3,4,5,6,7,8,9,10]
transformAndClasificateAle(listOfNumbers, primeNumbers)