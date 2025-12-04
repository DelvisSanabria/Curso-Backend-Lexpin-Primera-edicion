from conversor_texto import convertToUppercase, countWords as contador

try:
    frase = "Hola mundo desde Python"
    frase_mayusculas = convertToUppercase(frase)
    numero_de_palabras = contador(frase)

    print(f"Frase original: {frase}")
    print(f"Frase en mayúsculas: {frase_mayusculas}")
    print(f"Número de palabras: {numero_de_palabras}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
