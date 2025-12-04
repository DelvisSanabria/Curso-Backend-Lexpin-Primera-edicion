#Python tiene por defecto la capacidad de manejar archivos CSV (Comma Separated Values) utilizando el módulo integrado `csv`.

#tendremos varios modos para abrir un archivo CSV, entre los mas comunes tenemos:
#'r' Modo de lectura: Abre un archivo para leer su contenido. El archivo debe existir.
#'w' Modo de escritura: Abre un archivo para escribir. Si el archivo ya existe, se sobrescribe; si no, se crea uno nuevo.
#'a' Modo de anexado: Abre un archivo para agregar contenido al final. Si el archivo no existe, se crea uno nuevo.
#'x' Modo exclusivo de creación: Crea un nuevo archivo. Si el archivo ya existe, genera un error.

import csv

contacts = [
    {"name": "Alejandro Ramirez", "email": "i4I2o@example.com", "phone": "123-456-7890"},
    {"name": "Andreina Velecillos", "email": "X6tMw@example.com", "phone": "987-654-3210"},
    {"name": "Jesus doe", "email": "9EYlH@example.com", "phone": "555-555-5555"},
]

try:
  with open("Python/especializado/manejo_csv/contacts.csv", "w", newline='') as file:  # Abrir un archivo CSV en modo de escritura
    fieldnames = ["name", "email", "phone"]  # Definir los nombres de las columnas
    archive = csv.DictWriter(file, fieldnames=fieldnames)  # Crear un objeto DictWriter para escribir en el archivo CSV
    archive.writeheader()  # Escribir la fila de encabezado en el archivo CSV
    archive.writerows(contacts)  # Escribir las filas de datos en el archivo CSV
except Exception as e:
  print(f"Ocurrió un error al crear el archivo CSV: {e}")

try:
  with open("Python/especializado/manejo_csv/contacts.csv", "r") as file:  # Abrir el archivo CSV en modo de lectura
    archive = csv.DictReader(file)  # Crear un objeto DictReader para leer el archivo CSV
    for row in archive:  # Iterar sobre cada fila en el archivo CSV
      print(f"Nombre: {row['name']}, Email: {row['email']}, Teléfono: {row['phone']}")  # Imprimir los datos de cada fila """
except FileNotFoundError:
  print("El archivo CSV no fue encontrado.")  # Solicitar al usuario que ingrese una frase o recordatorio
  

#Ejercicio 1: Exportar Inventario
"""  Instrucción: Tienes una lista de diccionarios dentro de tu código con productos de una tienda (ej. `[{"id": 1, "producto": "Lápiz", "precio": 0.50}, ...]`).
    1.  Utiliza el módulo `csv` y la clase `DictWriter` para crear un archivo llamado `inventario.csv`.
    2.  Asegúrate de escribir primero los encabezados (las claves del diccionario) y luego todas las filas de datos.
    3.  Recuerda usar el parámetro `newline=''` al abrir el archivo para evitar filas en blanco en Windows. """