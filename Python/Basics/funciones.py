#Las funciones son bloques de codigo reutilizables, que nos permiten realizar tareas especificas


#Definir una funcion
def sayHello():
  print("Hola Mundo")
  
#llamar a una funcion
#sayHello()

#Scope

#Variable global puede ser accedida desde cualquier parte del codigo
variable = 10

def sayHelloAndShowVariable():
  print("Hola muchachos")
  print(variable)
  #varible local no puede ser accedida desde cualquier parte del codigo
  variableDos = 20
  print("estoy pintnando la variableDos desde dentro de la funcion", variableDos)
  
sayHelloAndShowVariable()

#print("estoy pintnando la variableDos desde fuera de la funcion", variableDos)

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