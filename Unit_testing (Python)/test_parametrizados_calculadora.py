from calculadora import sum, subtract, multiply, divide
import pytest

@pytest.mark.parametrize("num1, num2, expected_result", [
  (2,3,5), #test 1 : positivos
  (-2, -3, -5), #test negativos
  (100, 200, 300), #test numeros grandes
  (-10, 5, -5), #test suma a cero
])

def test_parametrized_sum(num1, num2, expected_result):
  assert sum(num1, num2) == expected_result
  
@pytest.mark.parametrize("num1, num2, expected_result, raises_exception",[
    (10, 2, 5.0, False), #Division normal
    (7,2, 3.5, False), #Division con float
    (10, 0, None, True), #Division con 0
])

def test_parametrized_divide(num1, num2, expected_result, raises_exception):
  if raises_exception:
    with pytest.raises(ValueError):
      divide(num1, num2)
  else:
    assert divide(num1, num2) == expected_result
    
    
#Ejercicios

""" 

Ejercicio 1: El Contador de Vocales
 Contexto: Necesitamos una función que analice textos para lingüística básica.
 Instrucciones:
    1.  Crea un archivo llamado `analizador_texto.py`.
    2.  Dentro, escribe una función llamada `contar_vocales(cadena)` que reciba un texto y devuelva la cantidad total de vocales (a, e, i, o, u) que contiene. Nota: Debe funcionar con mayúsculas y minúsculas.
    3.  Crea un archivo de pruebas llamado `test_analizador.py`.
    4.  Escribe tres casos de prueba individuales:
        * Una palabra simple (ej: "casa" -> 2).
        * Una palabra sin vocales (ej: "fly" -> 0).
        * Una palabra con mayúsculas y minúsculas mezcladas (ej: "AvIOn" -> 3).
    5.  Ejecuta `pytest` y asegúrate de que todos pasen.
"""

def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string.lower():
      if char in vowels:
        count += 1
    return count

def test_count_vowels():
  assert count_vowels("casa") == 2

def test_count_vowels_no_vowels():
  assert count_vowels("fly") == 0

def test_count_vowels_mixed_case():
  assert count_vowels("AvIOn") == 3

""" 

Ejercicio 2: Gestor de Inventario
 Contexto: Una tienda necesita saber si tiene productos en stock.
 Instrucciones:
    1.  Crea un archivo `inventario.py` con una función `hay_stock(lista_productos, producto_buscado)` que devuelva `True` si el producto está en la lista y `False` si no.
    2.  Crea el archivo `test_inventario.py`.
    3.  Escribe un test que verifique que encuentra un producto existente.
    4.  Escribe un test que verifique que devuelve `False` para un producto que no existe.
    5.  Reto de fallo: Introduce un error intencional en tu lógica (por ejemplo, que siempre devuelva `True`) y ejecuta `pytest` para ver cómo se ve el reporte de error en la consola. Luego corrígelo.

"""

def stock(list, search_product):
  return search_product in list

def test_product_in():
  inventory = ["manzana", "peras", "bananas"]
  assert stock(inventory, "peras") == True
  
def test_without_product():
  inventory = ["manzana", "peras", "bananas"]
  assert stock(inventory, "sandia") == False