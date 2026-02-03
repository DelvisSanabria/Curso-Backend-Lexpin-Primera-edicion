#Patron Singleton es un patron de diseño que nos permite crear una instancia unica de una clase.
#Es una forma de asegurarnos de que solo exista una instancia de una clase en todo el programa

class AppSettings:
  _instance = None
  
  def __new__(cls):
    if cls._instance is None:
      print("Creando la instancia unica de AppSettings")
      cls._instance = super(AppSettings, cls).__new__(cls)
      cls._instance.config = {
        "theme": "dark",
        "language": "es",
        "version": "1.0.0"
      }
    return cls._instance
  
  def get_config(self, key):
    return self.config.get(key)
  
  
setting = AppSettings()
print(f"Tema: {setting.get_config('theme')}")

setting2 = AppSettings()
print(f"Son la misma instancia: {setting is setting2}")

setting2.config["theme"] = "light"
print(f"Tema desde setting: {setting.get_config('theme')}")

#Patron Factory es un patron de diseño que nos permite crear objetos sin exponer la logica de creacion al cliente.
#Es una forma de encapsular la logica de creacion de objetos en una clase separada.


from abc import ABC, abstractmethod

#Crear una interfaz para notificaciones
class Notificacion(ABC):
  @abstractmethod
  def enviar(self, mensaje):
    pass
  
#Implementar clases concretas para diferentes tipos de notificaciones
class EmailNotificacion(Notificacion):
  def enviar(self, mensaje):
    print(f"Enviando email con el mensaje: {mensaje}")
    
class SMSNotificacion(Notificacion):
  def enviar(self, mensaje):
    print(f"Enviando SMS con el mensaje: {mensaje}")
    
    
#Crear una fabrica para generar objetos de notificaciones

class NotificacionFactory:
  def crear_notificacion(self, tipo):
    if tipo == "email":
      return EmailNotificacion()
    elif tipo == "sms":
      return SMSNotificacion()
    else:
      raise ValueError("Tipo de notificación no soportado")
    
    
factory = NotificacionFactory()
notificacion1 = factory.crear_notificacion("email")
notificacion1.enviar("Hola via Email!")


#Patron Buidler es un patron de diseño que nos permite construir objetos complejos paso a paso.
#Es una forma de separar la construccion de un objeto de su representacion.


class Pizza:
  def __init__(self):
    self.maza = None
    self.salsa = None
    self.ingredientes = []
    
  def __str__(self):
    return f"Pizza con maza: {self.maza}, salsa: {self.salsa}, ingredientes: {', '.join(self.ingredientes)}"
  
#Crear el builder para construir la pizza paso a paso

class PizzaBuilder:
  def __init__(self):
    self.pizza = Pizza()
    
  def agregar_maza(self, tipo_maza):
    self.pizza.maza = tipo_maza
    return self
  
  def agregar_salsa(self, tipo_salsa):
    self.pizza.salsa = tipo_salsa
    return self
  
  def agregar_ingrediente(self, ingrediente):
    self.pizza.ingredientes.append(ingrediente)
    return self
  
  def construir(self):
    return self.pizza
  
#Usar el builder para crear una pizza
builder = PizzaBuilder()

#Crear una pizza hawaiana
pizza_hawaiana = builder.agregar_maza("delgada").agregar_ingrediente("piña").agregar_ingrediente("jamón").agregar_salsa("dulce").construir()

print(pizza_hawaiana)

#Patron Prototype es un patron de diseño que nos permite clonar objetos existentes sin depender de sus clases concretas.


import copy

class Enemigo:
  def __init__(self, tipo, salud, ataque, nombre):
    self.tipo = tipo
    self.salud = salud
    self.ataque = ataque
    self.nombre = nombre
    
  def __str__(self):
    return f"Enemigo de nombre: {self.nombre}, tipo: {self.tipo}, salud: {self.salud}, ataque: {self.ataque}"
  
  def clonar(self):
    return copy.deepcopy(self)
  
  
#Creamos nuestro prototipo de enemigo
enemigo_prototipo = Enemigo("Orco", 100, 15, "Gorgoth")

#Clonamos el enemigo prototipo para crear nuevos enemigos
goblin1 = enemigo_prototipo.clonar()
goblin2 = enemigo_prototipo.clonar()

goblin2.nombre = "Zug"
goblin1.nombre = "Thok"
goblin1.salud = 80

print(enemigo_prototipo)
print(goblin1)
print(goblin2)

#Patrones de diseño de Comportamiento: son patrones que se centran en la comunicación entre objetos y la asignación de responsabilidades.

#Patron Observer es un patron de diseño que define una dependencia uno a muchos entre objetos.
#Cuando un objeto cambia de estado, todos sus dependientes son notificados y actualizados automáticamente.


#Creamos la clase Observador
class Subasta:
  def __init__(self):
    self.observadores = []
    self.precio_actual = 0
    
  def registrar_observador(self, observador):
    self.observadores.append(observador)
  
  def notificar_observadores(self):
    for observador in self.observadores:
      observador.actualizar(self.precio_actual)
      
  def hacer_oferta(self, nuevo_precio):
    if nuevo_precio > self.precio_actual:
      self.precio_actual = nuevo_precio
      print(f"Nuevo precio de la subasta: {self.precio_actual}")
      self.notificar_observadores()
      
#Creamos los observadores

class Ofertante:
  def __init__(self, nombre):
    self.nombre = nombre
    
  def actualizar(self, nuevo_precio):
    print(f"{self.nombre} ha sido notificado del nuevo precio: {nuevo_precio}")
    
    
#Usamos el patron Observer
subasta = Subasta()
ofertante1 = Ofertante("Alice")
ofertante2 = Ofertante("Bob")

subasta.registrar_observador(ofertante1)
subasta.registrar_observador(ofertante2)

subasta.hacer_oferta(100)
subasta.hacer_oferta(150)

#Patron State es un patron de diseño que permite a un objeto cambiar su comportamiento cuando su estado interno cambia.
#El objeto parecerá cambiar su clase.

class EstadoReproductor(ABC):
  @abstractmethod
  def press_play(self, reproductor):
    pass
  
#Creamos los estados del reproductor

#Estado Detenido

class EstadoDetenido(EstadoReproductor):
  def press_play(self, reproductor):
    print("Reproduciendo música...")
    reproductor.estado = EstadoReproduciendo()
    
#Estado Reproduciendo

class EstadoReproduciendo(EstadoReproductor):
  def press_play(self, reproductor):
    print("Deteniendo música...")
    reproductor.estado = EstadoDetenido()
  
#Estado Pausado

class EstadoPausado(EstadoReproductor):
  def press_play(self, reproductor):
    print("Reanudando música...")
    reproductor.estado = EstadoReproduciendo()
    
#Contexto: el reproductor de música

class Reproductor:
  def __init__(self):
    self.estado = EstadoDetenido()
    
  def press_play(self):
    self.estado.press_play(self)
    
#Usamos el patron State
reproductor = Reproductor()
reproductor.press_play() # Reproduciendo musica (inicio)
reproductor.press_play() # Deteniendo musica (Pausa)
reproductor.press_play() # Reproduciendo musica (reanudar)