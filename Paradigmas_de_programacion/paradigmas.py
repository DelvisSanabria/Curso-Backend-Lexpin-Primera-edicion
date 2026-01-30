#Pogramacion Orientada a Objetos (POO)

#Es el paradigma de programacion que utiliza "objetos" para representar datos y metodos

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
    #Metodos (Funciones dentro de una clase)
    
  def walk(self):
    print(f"{self.name} esta caminando")
      
persona1 = Person("Alfredo", 22)
persona2 = Person("Alejandro", 25)

#Acceder a los atributos

print(persona1.name)
print(persona2.age)

#podria acceder a los metodos

persona1.walk()
persona2.walk()

#Programacion Funcional

products = [
  {"name": "Laptop", "price": 1000},
  {"name": "Phone", "price": 500},
  {"name": "Tablet", "price": 300},
]

productos_Caros = list(filter(lambda product: product["price"] > 400, products))

nombres_productos_caros = list(map(lambda product: product["name"], productos_Caros))

print(nombres_productos_caros)  # Output: ['Laptop', 'Phone']


#Programacion Reactiva

#Creamos el sujeto observable

class CeldaFuente:
  def __init__(self, valor_inicial=0):
    self._valor = valor_inicial
    self._observadores = []
    
  def suscribir(self, observador):
    self._observadores.append(observador)
    
  def notificar(self):
    for observador in self._observadores:
      observador.actualizar()
      
  @property
  def valor(self):
    return self._valor
  
  @valor.setter
  def valor(self, nuevo_valor):
    if self._valor != nuevo_valor:
      self._valor = nuevo_valor
      print(f"Valor cambiado a: {self._valor}")
      self.notificar()
      
class CeldaFormula:
  def __init__(self, celdas_observadas, funcion_Calculo):
    self.celdas_observadas = celdas_observadas
    self.funcion_Calculo = funcion_Calculo
    self.valor = 0
    
    for celda in self.celdas_observadas:
      celda.suscribir(self)
    
  def actualizar(self):
    valores_fuente = [celda.valor for celda in self.celdas_observadas]
    self.valor = self.funcion_Calculo(*valores_fuente)
    print(f"CeldaFormula Reacciono y su valor actualizado es: {self.valor}")
    
    
#Ejemplo de uso

A1 = CeldaFuente(10)
B1 = CeldaFuente(20)


C1 = CeldaFormula([A1, B1], lambda a, b: a + b)

print(f"Valor inicial de A1: {A1.valor}")
print(f"Valor inicial de B1: {B1.valor}")
print(f"Valor inicial de C1 (A1 + B1): {C1.valor}")


print("\n==========================")
print("Cambiando el valor de A1 a 15")

A1.valor = 15

print("\n==========================")
print(f"Valor final de A1: {A1.valor}")
print(f"Valor final de B1: {B1.valor}")
print(f"Valor final de C1 (A1 + B1): {C1.valor}")

#Programacion Estructurada

#1 Secuencia: Primero declaramos la variable
sum = 0

#2. Iteraccion: Usamos un bucle para recorrer los numeros del 1 al 10
for i in range(1, 11):
  #3. Seleccion: Verificamos si el numero es par
  if i % 2 == 0:  #3. Seleccion: Verificamos si el numero es par
    sum += i  # Si es par, lo sumamos a la variable sum

print(f"La suma de los numeros pares del 1 al 10 es: {sum}")


#Programacion Orientada a Aspectos (AOP)

def register_actions(function):
  def wrapper(*args, **kwargs):
    #Antes de la ejecucion de la funcion registramos la accion
    print(f"Accion registrada: {function.__name__} esta siendo llamada")
    #Ejecutamos la funcion original
    result = function(*args, **kwargs)
    #Despues de la ejecucion de la funcion registramos la accion
    print(f"Accion registrada: {function.__name__} ha finalizado")
    return result
  return wrapper

@register_actions
def aggregar_producto(producto, cantidad):
  print(f"Agregando {cantidad} unidades de {producto} al inventario.")
  return "Producto agregado exitosamente."


@register_actions
def login(usuario):
  print(f"Usuario {usuario} ha iniciado sesion.")
  return "Inicio de sesion exitoso."


login("Alfredo")
print("\n")
aggregar_producto("Laptop", 5)


""" ### 1. Programación Imperativa: La Caja Registradora

Objetivo: Simular el cobro de productos uno por uno, modificando el total en cada paso.

Ejercicio:

Escribe un programa que tenga una lista de precios, por ejemplo: [10, 25, 5, 8].

1. Crea una variable `total` y ponla en `0`.
2. Usa un bucle (`for` o `while`) para recorrer cada precio de la lista.
3. En cada paso del bucle, suma el precio actual a la variable `total`.
4. Después de cada suma, imprime un mensaje como: `Producto agregado, el total ahora es: [nuevo total]`.
5. Al final, imprime el `total` definitivo a pagar. """