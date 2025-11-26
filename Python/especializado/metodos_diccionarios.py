#Metodos de diccionarios en Python

#un diccionario es una coleccion de pares clave-valor.

person = {
    "Nombre": "Guillermo",
    "Apellido": "Gonzalez",
    "País": "Venezuela",
    "Edad": 50,
    "Correo": "guillermo@mail.com",
    "Género": "Masculino",
    "Trabajo": "Programador",
    "Lenguajes": [["Python", "JavaScript"], "TypeScript", "CSS", "HTML", "SQL", "PHP"],
    "Hobbies": ["Leer", "Escribir", "Programar", "Ver series"],
    "Estudios": {
        "Primaria": "Escuela Jaimito",
        "Secundaria": "Liceo Pedrito",
        "Universidad": "Universidad Fulanito"
    },
    "Vehiculos": "Automovil",
    "Hijos":[
        {
            "Nombre": "Juan",
            "Edad": 10,
            "Hobbies": ["Jugar", "Dibujar", "Leer"]
        },
        {
            "Nombre": "Maria",
            "Edad": 5,
            "Hobbies": ["Cantar", "Bailar", "Jugar"]
        }
    ],
}

#get(key): Devuelve el valor de la clave especificada. Si la clave no existe, devuelve el valor por defecto.
person_name = person.get("Nombre")
print(f"Nombre: {person_name}")

person_university = person.get("Estudios").get("Universidad")
print(f"Universidad: {person_university}")

person_languages = person.get("Lenguajes")[0][1]
print(f"Segundo lenguaje: {person_languages}")

person_children = person.get("Hijos")[1].get("Nombre")
print(f"Nombre del segundo hijo: {person_children}")

#setdefault(key, valor): Devuelve el valor de la clave especificada. Si la clave no existe, la crea con el valor por defecto.

#crear una nueva clave-valor en el diccionario si no existe
person_job = person.setdefault("Trabajo", "Desarrollador")
print(f"Trabajo: {person.get('Trabajo')}")
#crear una nueva clave-valor en el diccionario si no existe
person_pet = person.setdefault("Mascota", "Perro")
print(f"Mascota: {person.get('Mascota')}")

#crear una nueva clave-valor en el diccionario
person["personalidad"] = ["Amable", "Paciente", "Creativo"]
print(f"Personalidad: {person.get('personalidad')}")
#Modificar el valor de una clave existente
person["Hijos"][0]["Edad"] = 20
print(f"Edad del primer hijo: {person.get('Hijos')[0].get('Edad')}")


#mostrar el diccionario completo
print("Diccionario completo:")
print(person)

import json

print("Diccionario completo en formato JSON:")
print(json.dumps(person, indent=3, ensure_ascii=False))

#items(): Devuelve una vista de los pares clave-valor en el diccionario.
person_items = person.items()
print(f"Pares clave-valor: {person_items}")

#keys(): Devuelve una vista de las claves en el diccionario.
person_keys = person.keys()
print(f"Claves: {person_keys}")

#values(): Devuelve una vista de los valores en el diccionario.
person_values = person.values()
print(f"Valores: {person_values}")

#pop(key): Elimina y devuelve el valor de la clave especificada.

newPerson ={
    "Nombre": "Ana",
    "Apellido": "Martinez",
    "País": "Argentina",
    "Edad": 30,
    "Correo": "ana@mail.com",
    "Género": "Femenino",
    "Trabajo": "Desarrolladora",
    "Lenguajes": [["Python", "JavaScript"], "TypeScript", "CSS", "HTML", "SQL", "PHP"],
    "Hobbies": ["Leer", "Escribir", "Programar", "Ver series"],
    "Estudios": {
        "Primaria": "Escuela Jaimito",
        "Secundaria": "Liceo Pedrito",
        "Universidad": "Universidad Fulanito"
    },
    "Vehiculos": "Automovil",
    "Hijos":[
        {
            "Nombre": "Juan",
            "Edad": 10,
            "Hobbies": ["Jugar", "Dibujar", "Leer"]
        },
        {
            "Nombre": "Maria",
            "Edad": 5,
            "Hobbies": ["Cantar", "Bailar", "Jugar"]
        }
    ],
}

newPerson.pop("Hijos")
print(json.dumps(newPerson, indent=3))

#popitem(): eliminar un valor aleatorio (clave, valor) aleatorio del diccionario
popEliminatedKey = newPerson.popitem()
print(f"La propiedad eliminada es: {popEliminatedKey}")
print(json.dumps(newPerson, indent=3))

#agregar valores

#update({other}): Actualiza el diccionario con los pares clave-valor de otro diccionario o de un iterable de pares clave-valor.
additional_info = {
    "Nacionalidad": "Venezolana",
    "Estado Civil": "Soltero",
    "Idiomas": ["Español", "Inglés", "Francés"]
}
newPerson.update(additional_info)
print(json.dumps(newPerson, indent=3, ensure_ascii=False))

newPerson.update({"Comida": ["empanadas", "Arepas"]})
print(json.dumps(newPerson, indent=3, ensure_ascii=False))

#copy(): Devuelve una copia superficial del diccionario. esta vinculada al original
personCopy = newPerson.copy()

print(f"El diccionario original es {newPerson}")
print(f"El diccionario copia es {personCopy}")

#clear(): Elimina todos los elementos de un diccionario

personCopy.clear()

print(f"El diccionario original es {newPerson}")
print(f"El diccionario copia es {personCopy}")

#Ejercicio mediano opcional

"""

Ejercicio de Complejidad Media: Sistema de Gestión de Biblioteca

Enunciado:
Crea un programa que gestione una biblioteca con las siguientes funcionalidades:

Registrar libros:

Pedir título, autor, año de publicación y género.

Almacenar los libros en una lista de diccionarios.

Validar que el año sea un número entre 1000 y 2025.

Buscar libros:

Permitir búsqueda por: título, autor o género.

Mostrar todos los libros que coincidan (aunque sea parcialmente).

Usar match-case para determinar el tipo de búsqueda.

Préstamos de libros:

Permitir "prestar" un libro cambiando su estado (agregar clave disponible: bool).

Llevar registro de libros prestados y disponibles.

No permitir préstamo si no hay ejemplares disponibles.

Estadísticas:

Mostrar:

Total de libros

Libros disponibles vs prestados

Género más popular

Usar bucles for y condicionales para calcular datos.

Menú interactivo:

Usar while para mantener el programa activo hasta que el usuario elija salir.

Mostrar opciones numeradas y manejar entradas inválidas.

"""