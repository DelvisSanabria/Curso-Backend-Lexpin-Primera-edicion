#Metodos de String

""" Los metodos son funciones que se pueden utilizar en una cadena de texto
  para manipularla o obtener informacion de ella. Algunos de los metodos mas comunes son:"""
  

#len(string): Devuelve la longitud de la cadena de texto.

stringChange = "Mi cadena de texto"
print(f"La longitud de la cadena es: {len(stringChange)}")

#count(substring): Cuenta cuantas veces aparece una subcadena en la cadena de texto.
print(f"La subcadena 'cadena' aparece: {stringChange.count('cadena de')} veces.")
print(f"Muy bien, no usaste la palabra cadena" if stringChange.count('cadena de') == 0 else "Usaste la palabra cadena")

#upper(): Convierte la cadena de texto a mayusculas.
username = "impeRIOus"
print(username.upper())

#lower(): Convierte la cadena de texto a minusculas.
print(username.lower())

#capitalize(): Convierte el primer caracter de la cadena de texto a mayuscula.
print(username.capitalize())

#replace(old, new): Reemplaza una subcadena por otra en la cadena de texto.
userStatus = "Usuario no autorizado"
print(userStatus.replace("no autorizado", "autorizado"))

#split(separator): Divide la cadena de texto en una lista de subcadenas utilizando un separador.

testText = "Este es un texto de prueba"
textList = testText.split(" ")
print(textList[1])
token = "Barear eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
tokenParts = token.split(" ")
print(tokenParts[1])

#Ejercicio: Crear una funcion que reciba una cadena de texto y devuelva la misma cadena con la primera letra de cada palabra en mayuscula.

def capitalize_words(text):
    words = text.split(" ") #["esto", "es", "una", "prueba"]
    capitalized_words = [word.capitalize() for word in words] #["Esto", "Es", "Una", "Prueba"]
    return " ".join(capitalized_words)
  
print(capitalize_words("esto es una prueba"))

#Otra forma de hacerlo es usando el metodo title() que convierte la primera letra de cada palabra en mayuscula.
def capitalize_words_v2(text):
  return text.title()

print(capitalize_words_v2("esto es otra prueba"))

#"separator".join(iterable): Une una lista de cadenas de texto en una sola cadena utilizando un separador.
wordsList = ["Esto", "es", "una", "prueba"]
joinedText = " ".join(wordsList)
print(joinedText)

#strip("characters"): Elimina los espacios en blanco o caracteres especiales al inicio y al final de la cadena de texto.
textToClean = "-------Esto es un texto con espacios al inicio y al final.------"
cleanText = textToClean.strip("-")
print(cleanText)

#startswith(prefix): Devuelve True si la cadena de texto comienza con el prefijo especificado.
url = "https://www.ejemplo.com"
print(url.startswith("https://"))  # True
print(url.startswith("http://"))   # False

userAccesToken = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

if userAccesToken.startswith("Bearer "):
    token = userAccesToken.split(" ")[1]
    print(f"El token es: {token}")

#endswith(suffix): Devuelve True si la cadena de texto termina con el sufijo especificado.
print(url.endswith(".com"))  # True
print(url.endswith(".org"))  # False

 