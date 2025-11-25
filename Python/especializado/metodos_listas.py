#Metodos de listas, son metodos que nos permiten interactuar con las listas en Python.

#Lista de prueba

fruits = ["apple", "banana", "cherry", "date"]
print(f"Lista inicial: {fruits}")

#len(list): Devuelve la longitud de la lista.
print(f"La longitud de la lista es: {len(fruits)}")

#append(item): Agrega un elemento al final de la lista.
fruits.append("elderberry")
print(f"Lista despues de append: {fruits}")

#Ejercicio: Crear una funcion que reciba una cadena de texto y devuelva la misma cadena con la primera letra de cada palabra en mayuscula. (usando append for)

def capitalize_words(text):
    words = text.split()
    capitalized_words = []
    for word in words:
        capitalized_words.append(word.capitalize())
    return ' '.join(capitalized_words)
  
print(capitalize_words("Que tal estan muchachos?"))