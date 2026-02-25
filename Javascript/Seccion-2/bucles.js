//Los bucles son estructuras de control que nos permiten repetir un bloque de código varias veces, hasta que se cumpla una condición determinada. 

// En JavaScript, existen varios tipos de bucles, como el bucle for, el bucle while y el bucle do...while.


// Bucle for

/* es un bucle que se ejecuta una cantidad determinada de veces */

/* la estructura de un bucle for es la siguiente:
for (inicialización; condición; incremento) {
    // código a ejecutar
}
*/

import { question } from "readline-sync";
import readlineSync from "readline-sync";

for (let i = 1; i <= 10; i++) {
    console.log(`5 x ${i} = ${5 * i}`);
}

//Bucles anidados

/* es un bucle que se encuentra dentro de otro bucle */

for (let y = 1; y <= 10; y++) {
  for (let i=1; i <= 10; i++) {
    console.log(`${y} x ${i} = ${y * i}`);
    if (i==10){
      console.log("---------------")
    }
  }
}

//for/in: Recorre las propiedades de un objeto

/* Se usa para recorrer las propiedades de un objeto, permitiendo acceder a cada uno de sus clave valor */

/* la estructura de un bucle for/in es la siguiente:
for (variable in objeto) {
    // código a ejecutar
}
*/

let person = {
    name: "Alfredo",
    age: 30,
    city: "New York"
}

for (let key in person) {
    console.log(`${key}: ${person[key]}`);
}

//Puedo recorrer un array con un bucle for/in, pero no es recomendable, ya que el orden de los elementos no está garantizado

let names = ["Alfredo", "Juan", "Maria", "Alejandro"];

for (let index in names) {
    console.log(`${index}: ${names[index]}`);
}


//for/of: Recorre los elementos de un iterable (como un array)

/* Se usa para recorrer los elementos de un iterable, permitiendo acceder a cada uno de ellos */

/* la estructura de un bucle for/of es la siguiente:
for (variable of iterable) {
    // código a ejecutar
}
*/

for (let person of names) {
    console.log(`${person}`);
}

//Puedo recorrer un objeto con un bucle for/of, pero no es recomendable, ya que no es un iterable

for (let key of Object.keys(person)) {
    console.log(`key: ${key}`);
}

for (let value of Object.values(person)) {
    console.log(`value: ${value}`);
}


//Bucle while

/* es un bucle que se ejecuta mientras se cumpla una condición */

/* la estructura de un bucle while es la siguiente:
while (condición) {
    // código a ejecutar
}
*/

let i = 1;
while (i <= 10) {
    console.log(`5 x ${i} = ${5 * i}`);
    i++;
}

//Bucle do...while

/* es un bucle que se ejecuta al menos una vez, y luego se repite mientras se cumpla una condición */

/* la estructura de un bucle do...while es la siguiente:
do {
    // código a ejecutar
} while (condición);
*/

let answer = false;
do {
    console.log("Hola antes de bucle");
    answer = readlineSync.keyInYNStrict("Quieres continuar? (yes/no) ");
}while (answer);
