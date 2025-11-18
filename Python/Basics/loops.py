#Los loops son estructuras de control que nos permiten repetir un bloque de codigo
#un numero determinado de veces o mientras se cumpla una condicion


#While  (Mientras se cumpla)
count = 0

while count < 3:
  print(f"me ejecuto, estoy en la vuelta {count}")
  count += 1
  
print("Sali del bucle")

#Ejemplo de bucle calculador de suma

""" choise = int(input("Para iniciar escribe 1:"))

while choise == 1:
  num1 = int(input("Ingresa el primer numero a sumar: "))
  num2 = int(input("Ingresa el segundo numero a sumar: "))
  total = num1 + num2
  print(f"El resultado de tu suma fue {total}")
  choise = int(input("Para reinicar escribe el numero 1: "))
  
print("Fin del programa") """


#For (para cada elemento) nos creara un bucle que se repetira segun la cantidad de elementos

fruits = ["apple", "orange", "banana"]
print(fruits)

#for (elemento in lista): (lo que quiero hacer a cada elemento en cada vuelta (iteracion))
for fruit in fruits:
  print(fruit)
  
#Pintar una cantidad especifica de numeros segun un rango (una extesion de numeros de A a Z)

#En programacion se comienza a contar desde el 0, es decir el numero 0 es la posicion 1
for number in range(0,11):
  print(f"El numero es: {number}")
  
myList = ["Eduardo", "Jesus", "Hugo", "Delvis"]

#Break (break) nos sirve para romper un bucle
for name in myList:
  if name == "Jesus":
    break #rompe el bucle
  print(f"El nombre es: {name}")
 
#Continue (continue) nos sirve para saltar a la siguiente iteracion 
for name in myList:
  if name == "Jesus":
    continue #se salta a la siguiente iteracion
  print(f"El nombre es: {name}")
  
  
#usando ambos

fruits = ["apple", "orange", "banana", "kiwi","coco"]

for fruit in fruits:
  if fruit == "banana":
    continue
  elif fruit == "kiwi":
    print("Estoy en la fruta prohibida")
    break
  print(fruit)
  
#Enunciado de ejercicios:

# Ejercicio 1: Contador Selectivo (For + If)
# Enunciado:  
# Escribe un programa que pida al usuario un número entero positivo `n`. Luego, usando un bucle `for`, imprime todos los números del 1 al `n` que cumplan una de estas condiciones:
# 1. El número es múltiplo de 3.
# 2. El número es mayor que 10 y menor que 20.
# 3. El número es igual a 25 o 50.  
# Si el número no cumple ninguna condición, no se imprime.

n = int(input("Escribe un numero positivo:"))

for number in range(1, n + 1):
  if (10 < number < 20) or (number % 3 == 0) or (number == 25 or number == 30):
    print(f"El numero {number} cumple con aluna de las condiciones")
    
# Ejercicio 2:
#Enunciado: 
# Crea un programa que simule la validación de una contraseña:
# 1. Define una contraseña secreta (ej: `"python123"`).
# 2. Pide al usuario que ingrese una contraseña.
# 3. Usa un bucle `while` para:
#    - Permitir hasta 3 intentos.
#    - Si la contraseña es correcta, muestra "¡Acceso concedido!" y termina.
#    - Si es incorrecta, muestra "Contraseña incorrecta. Intentos restantes: X".
#    - Si se agotan los intentos, muestra "¡Cuenta bloqueada!".

password = "python123"
attents = 3

print("Bienvenido al sistema de validacion")
while attents > 0:
  userInput = input("Ingresa tu contraseña: ") # type: ignore
  if userInput == password:
    print("¡Acceso concedido!")
    break
  else:
    attents -=1
    print(f"Contraseña incorrecta. Intentos restantes: {attents}")
if attents == 0:
  print("¡Cuenta bloqueada!")

#Ejercicio 3
# Enunciado:  
# Pide al usuario 5 números enteros, usando un bucle `for` y `match-case`:
# 1. Clasifica cada número en:
#    -"Pequeño" si es menor que 10.
#    -"Mediano" si está entre 10 y 50.
#    -"Grande" si es mayor que 50.
#    -"Cero" si es 0.
# 2. Al final, muestra cuántos números hubo en cada categoría.

pequeno = mediano = grande = cero = 0
  
  
for _ in range(5):
  num = int(input("ingresa un numero: "))
  match num:
    case 0:
      cero += 1
    case n if n < 10:
      pequeno +=1
    case n if 10 <= n <=50:
      mediano +=1
    case _:
      grande +=1

print("Resultados:")
print("Pequeno: ", pequeno)
print("Mediano: ", mediano)
print("Grande: ", grande)
print("Cero: ", cero)