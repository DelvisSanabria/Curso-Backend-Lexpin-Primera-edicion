#Una clase: es un molde para crear objetos

class Personaje:
  #Atributos: son las características del objeto
  #Constructor: es un método especial para inicializar los atributos
  def __init__(self, nombre,tipo) -> None:
    self.nombre = nombre
    self.tipo = tipo
    self.habilidades = []
    
  #Métodos: son las acciones que el objeto puede realizar
  def agregar_habilidad(self, habilidad):
    self.habilidades.append(habilidad)
    print(f"Habilidad {habilidad} aprendida por {self.nombre}")
    
#Crear objetos: instancias de la clase

personaje1 = Personaje("Aragorn", "Guerrero")
personaje2 = Personaje("Gandalf", "Mago")

#Usar métodos de los objetos
personaje1.agregar_habilidad("Espada")
personaje2.agregar_habilidad("Magia")

#Las interfaces : son un contrato que las clases se comprometen a cumplir
from abc import ABC, abstractmethod

#Definir una interfaz es decir el contrato a cumplir
class Combatiente(ABC):
  #Metodo abstracto : si o si debe ser implementado por las clases que hereden de esta interfaz
  @abstractmethod
  def atacar(self):
    pass
  
  @abstractmethod
  def defender(self):
    pass
  
  
#Implementar la interfaz en una clase concreta

class Heroe(Combatiente):
  def __init__(self, nombre):
    self.nombre = nombre
    
  def atacar(self):
    print(f"{self.nombre} ataca con valentía!")
    
  def defender(self):
    print(f"{self.nombre} se defiende con escudo!")
    
  def saludar(self):
    print(f"{self.nombre} saluda a la multitud!")
    
class Superheroe(Heroe):
  def __init__(self, nombre, poder):
    super().__init__(nombre)
    self.poder = poder
  def volar(self):
    print(f"{self.nombre} está volando por los cielos!")
    
    
class Villano(Combatiente):
  def __init__(self, nombre):
    self.nombre = nombre
    
  def atacar(self):
    print(f"{self.nombre} ataca con maldad!")
    
  def defender(self):
    print(f"{self.nombre} se defiende con astucia!")
    
#Crear instancias de las clases que implementan la interfaz

superman = Heroe("Superman")
aquaman = Heroe("Aquaman")
villano = Villano("Lex Luthor")
spiderman = Superheroe("Spiderman", "Telarañas")

superman.atacar()
villano.defender()
spiderman.volar()