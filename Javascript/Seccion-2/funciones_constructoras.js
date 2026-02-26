//Las funciones constructoras son funciones que se utilizan para crear objetos. Se utilizan con la palabra clave "new" y se escriben con la primera letra en mayúscula por convención.

import { question } from "readline-sync";


function Person(nameAtributte, ageAtributte) {
    this.name = nameAtributte;
    this.age = ageAtributte;  
    this.greet = function() {
        console.log(`Hola, mi nombre es ${this.name} y tengo ${this.age} años.`); 
    }
}

const person1 = new Person(question("Ingrese su nombre: "), question("Ingrese su edad: "));
const person2 = new Person("Jesus", 25);

person1.greet(); // Hola, mi nombre es Alejandro y tengo 30 años.
person2.greet(); // Hola, mi nombre es Jesus y tengo 25 años.