#Metodos de listas, son metodos que nos permiten interactuar con las listas en Python.

#Lista de prueba

fruits = ["apple", "banana","Banana","Banana", "cherry", "date"]
print(f"Lista inicial: {fruits}")

#len(list): Devuelve la longitud de la lista.
print(f"La longitud de la lista es: {len(fruits)}")

#agregando elementos a la lista

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

#extend(iterable): Extiende la lista agregando todos los elementos del iterable.
more_fruits = ["fig", "grape"]
fruits.extend(more_fruits)
print(f"Lista despues de extend: {fruits}")

#insert(index, item): Inserta un elemento en la posicion especificada.
names = ["Alice", "Bob", "Charlie"]
names.insert(0, "David")
print(f"Lista despues de insert: {names}")

#Borrar elementos de la lista

#remove(item): Elimina la primera ocurrencia del elemento especificado.
fruits.remove("banana")
print(f"Lista despues de remove: {fruits}")

#Buscar elementos en la lista

#index(item): Devuelve el indice de la primera ocurrencia del elemento especificado.
index_cherry = fruits.index("cherry")
print(f"El indice de 'cherry' es: {index_cherry}")

#count(item): Devuelve el numero de veces que el elemento especificado aparece en la lista.
count_banana = fruits.count("Banana")
print(f"El numero de veces que aparece 'Banana' es: {count_banana}")

#Ordenar y revertir la lista

#sort(): Ordena los elementos de la lista en orden ascendente.

numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(f"Lista despues de sort: {numbers}")
chartacters = ['d', 'a', 'c', 'b']
chartacters.sort()
print(f"Lista despues de sort: {chartacters}")
names = ['Charlie', 'Alice', 'Bob', 'david', 'Eve', 'frank', 'Amy']
names.sort()
print(f"Lista despues de sort: {names}")
names.sort(reverse=True)
print(f"Lista despues de sort reversa: {names}")

#reverse(): Revierte el orden de los elementos en la lista.
chartacters.reverse()
print(f"Lista despues de reverse: {chartacters}")

#clear(): Elimina todos los elementos de la lista.
numbers.clear()
print(f"Lista despues de clear: {numbers}")

#copy(): Devuelve una copia superficial de la lista.
fruits_copy = fruits.copy()
print(f"Lista copia: {fruits_copy}")

#pop([index]): Elimina y devuelve el elemento en la posicion especificada. Si no se especifica el indice, elimina y devuelve el ultimo elemento.
last_fruit = fruits.pop(2)
print(f"Elemento eliminado con pop: {last_fruit}")
print(f"Lista despues de pop: {fruits}")

#Ejercicio: Crear una funcion que reciba una lista de numeros y devuelva una nueva lista con los numeros ordenados de mayor a menor, sin modificar la lista original.

def sort_descending(original_list):
    if not isinstance(original_list, list):
        return "Error: El argumento debe ser una lista."
    #comprobamos que la lista sea una lista
    if type(original_list) != list:
        return "Error: La lista debe ser una lista."
    #comprobamos que todos los elementos de la lista sean numeros
    for item in original_list:
        if not isinstance(item, (int, float)):
            return "Error: Todos los elementos de la lista deben ser numeros."
    new_list = original_list.copy()
    new_list.sort(reverse=True)
    return new_list

print(sort_descending([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))