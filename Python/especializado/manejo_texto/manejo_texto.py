#Python tiene  varias funciones integradas para el manejo de texto.

#open("ruta/del/archivo.txt", "modo") - Abre un archivo en el modo especificado (lectura, escritura, etc.)

#'r' Modo de lectura: Abre un archivo para leer su contenido. El archivo debe existir.
#'w' Modo de escritura: Abre un archivo para escribir. Si el archivo ya existe, se sobrescribe; si no, se crea uno nuevo.
#'a' Modo de anexado: Abre un archivo para agregar contenido al final. Si el archivo no existe, se crea uno nuevo.
#'x' Modo exclusivo de creación: Crea un nuevo archivo. Si el archivo ya existe, genera un error.

try:
  document = open("Python/especializado/manejo_texto/historia.txt", "r")  # Abrir un archivo en modo de lectura
  
  content = document.read()  # Leer el contenido del archivo
  print(content)  # Imprimir el contenido del archivo
  
  document.close()  # Cerrar el archivo
except FileNotFoundError:
  print("El archivo no fue encontrado.")
  
  
#Crear un archivo y escribir en él
try: 
  #Creamos un nuevo archivo en la ruta especificada y en modo de escritura
  new_document = open("Python/especializado/manejo_texto/nuevo_archivo.txt", "w")  # Abrir un archivo en modo de escritura
  
  # Solicitar al usuario que ingrese contenido para el nuevo archivo
  content = input("Escribe algo para guardar en el archivo: ")  # Solicitar al usuario que ingrese contenido
  
  #con el metodo write() escribimos el contenido en el archivo recien creado 
  new_document.write(content)  # Escribir el contenido en el archivo
  
  # Cerrar el archivo
  new_document.close()  # Cerrar el archivo
  print("Contenido guardado en 'nuevo_archivo.txt'.")
  
  #Abrimos el archivo recien creado para leer su contenido
  document = open("Python/especializado/manejo_texto/nuevo_archivo.txt", "r")  # Abrir el archivo recién creado en modo de lectura
  print("Contenido del archivo recién creado:")
  
  #con el metodo read() leemos el contenido del archivo recien creado
  print(document.read())  # Leer y mostrar el contenido del archivo recién creado
  
  #Cerramos el archivo recien creado
  document.close()  # Cerrar el archivo recién creado
except FileNotFoundError:
  print("El archivo no fue encontrado.")
  
def append_to_file(file_path, text):
  try:
    with open(file_path, "a") as file:  # Abrir el archivo en modo de anexado
      file.write("\n" + text + "\n")  # Agregar el texto al final del archivo
    print(f"Texto agregado a '{file_path}'.")
  except FileNotFoundError:
    print("El archivo no fue encontrado.")
    
append_to_file("Python/especializado/manejo_texto/nuevo_archivo.txt", "Este es un texto adicional.")

#Ejercicio 1: El Creador de Notas

"""  Instrucción: Escribe un programa que pida al usuario ingresar una frase o recordatorio. El programa debe crear un archivo llamado `mis_notas.txt` y guardar esa frase en él utilizando el modo de escritura (`'w'`). Al finalizar, debe imprimir un mensaje confirmando que el archivo fue creado exitosamente. """

try:
  document = open("Python/especializado/manejo_texto/mis_notas.txt", "w")  # Abrir un archivo en modo de escritura
  document.close()  # Cerrar el archivo para asegurarse de que esté creado

  while True:
    document = open("Python/especializado/manejo_texto/mis_notas.txt", "a")  # Abrir el archivo en modo de anexado
    note = input("Escribe una frase o recordatorio (o 'salir' para terminar): ")  # Solicitar al usuario que ingrese una frase o recordatorio
    if note.lower() == 'salir':
      document.close()  # Cerrar el archivo antes de leer
      document = open("Python/especializado/manejo_texto/mis_notas.txt", "r")  # Abrir el archivo en modo de lectura
      print(document.read())  # Leer y mostrar el contenido del archivo antes de cerrar
      document.close()  # Cerrar el archivo
      break
    document.write(note + "\n")  # Escribir la frase en el archivo con un salto de línea
except Exception as e:
  print(f"Ocurrió un error: {e}")