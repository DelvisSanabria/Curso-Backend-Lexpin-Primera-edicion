#los operadores logicos nos permiten combinar varias expresiones para realizar operaciones complejas

a = True
b = False
c = True

#and (&& and)

result = a and b
print("Operacion and: ", result)

result = a and c
print("Operacion and: ", result)

#or (|| or)

result = a or b
print("Operacion or: ", result)

result = a or c
print("Operacion or: ", result)

#not (!)

result = not a
print("Operacion not: ", result)

result = not b
print("Operacion not: ", result)

#ejercicios

a = 10
b = 5
c = 10
s = "hola"

""" 
Ejercicio 1: ¿Son a y c iguales, y es b menor que a?

Ejercicio 2: ¿Es a mayor que b, o es s igual a "adiós"?

Ejercicio 3: ¿Es a diferente de c?

Ejercicio 4: ¿Es a igual a c, y es a no menor que b?

Ejercicio 5 (En rango): Escribe una expresión que verifique si b está entre 0 y 10 (ambos incluidos).

  result5 = (b >= 0) and (b <= 10)
  print("Operacion and: ", result5)
"""