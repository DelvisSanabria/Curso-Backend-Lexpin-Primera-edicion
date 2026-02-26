//las clases son plantillas que nos permiten crear objetos con sus propiedades y metodos
//las clases nos permiten crear objetos con sus propiedades y metodos

import { question } from "readline-sync";
import readlineSync from "readline-sync";

class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  //metodos
  greeting() {
    console.log(`Hola, mi nombre es ${this.name} y tengo ${this.age} años.`);
  }

  greetingWithName(name) {
    console.log(`Hola ${name}, mi nombre es ${this.name} y tengo ${this.age} años.`);
  }

  //metodo estatico que no necesita una instancia para ser llamado
  static staticGreeting() {
    console.log("Hola, soy un metodo estatico.");
  }

  //las propiedades estaticas son propiedades que no necesitan una instancia para ser accedidas
  static staticProperty = "Soy una propiedad estatica.";
}

//loop para crear personas

let answer;

do {
  const instance = new Person(question("Ingrese su nombre: "), parseInt(question("Ingrese su edad: ")));

  //mostrar los datos de la persona
  console.log(`Nombre: ${instance.name}, Edad: ${instance.age}`);
  //saludar a la persona
  instance.greeting();
  //saludar a otra persona
  instance.greetingWithName(question("Ingrese el nombre de la persona a saludar: "));

  answer = readlineSync.keyInYNStrict("¿Desea crear otra persona? (y/n): ");
} while (answer === true);