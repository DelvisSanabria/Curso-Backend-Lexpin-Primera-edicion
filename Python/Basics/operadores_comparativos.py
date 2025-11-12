#Operadores Comparativos

""" Son simbolos que nos permiten realizar operaciones de comparacion
    para comprobar si, un valor y otro son iguales, diferentes o si uno es mayor o menor que otro
"""
num1 = 10
num2 = 10

#Igual a (==)

result = num1 == num2
print("Operacion de igualdad: ", result)

userPassword = "delvis"
passwordDB = "delvis"

passwordResult = userPassword == passwordDB
print("Operacion de igualdad: ", passwordResult)

#Diferente a (!=)

result = num1 != num2
print("Operacion de desigualdad: ", result)

userAge = 18
permitedAge = 18

ageResult = userAge != permitedAge
print("Operacion de desigualdad: ", ageResult)

#Menor que (<)

userAge = 18
permitedAge = 18

ageResult = userAge < permitedAge
print("Operacion de menor que: ", ageResult)

#Menor o igual que (<=)

userAge = 18
permitedAge = 18

ageResult = userAge <= permitedAge
print("Operacion de menor o igual que: ", ageResult)

#Mayor que (>)

userAge = 18
permitedAge = 21

ageResult = userAge > permitedAge
print("Operacion de mayor que: ", ageResult)

#Mayor o igual que (>=)

userAge = 18
permitedAge = 21

ageResult = userAge >= permitedAge
print("Operacion de mayor o igual que: ", ageResult)