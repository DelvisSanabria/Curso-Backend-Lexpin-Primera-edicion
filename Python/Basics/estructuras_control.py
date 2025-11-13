#la estructuras condicionales, nos permiten controlar el flujo de nuestro programa segun una condicion

age = -18

#if (si) estructura if(si) (condicion): (lo que quiero hacer si se cumple la condicion)
if age >=18:
  print("Puedes pasar eres mayor")
#sino si (condicion): (lo que quiero hacer si se cumple la condicion)
elif age < 18 and age > 0:
  print("Eres menor no puedes pasar")
#Sino (Sino se cumple lo anterior has esto:)
else:
  print("No es una edad valida")
  
#Operador ternario: nos sirve para comprobar condicionales en una sola linea cuando se hace una sola comprobacion

# (lo que quiero hacer) if (lo que voy a comprobar ) else (Lo que pasa si no se cumple lo que comprobe)

message = "Puedes pasar eres mayor de edad" if age >=18 else "No puedes pasar, eres un bebe"

print(message)

#Match case: es una estructura de control que nos permite comparar un valor con multiples casos
# Ejecutar un bloque de codigo segun coincida

print("Selecciona un idioma, con su numero respectivo: 1. Espanol, 2. Ingles, 3. Frances")
answer = input()
#input() recibe un string

match answer:
  case "1":
    print("Elegiste el idioma Espanol")
  case "2":
    print("Elegiste el idioma Ingles")
  case "3":
    print("Elegiste el idioma Frances")
  case _:
    print("Idioma no valido")