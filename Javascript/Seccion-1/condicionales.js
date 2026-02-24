//Una expresion condicional es una expresion que se evalua y devuelve un valor dependiendo de si la condicion es verdadera o falsa

import { question } from "readline-sync";

// condicional if (Si)

/* Cuya estructura es la siguiente:
if (condicion) {
    //codigo a ejecutar si la condicion es verdadera
}
*/

if(4 > 2) {
    console.log("4 es mayor que 2");
}

//else (Si no)
else {
    console.log("4 no es mayor que 2");
}

// if else (Si... Si no)

/* Cuya estructura es la siguiente: 
if (condicion) {
    //codigo a ejecutar si la condicion es verdadera
} else {
    //codigo a ejecutar si la condicion es falsa
}
*/

if(7 < 2) {
    console.log("7 es mayor que 2");
} else {
    console.log("7 no es mayor que 2");
}

// else if (Si... Si no... Si no)

/* Cuya estructura es la siguiente: 
if (condicion) {
    //codigo a ejecutar si la condicion es verdadera
} else if (condicion) {
    //codigo a ejecutar si la condicion es verdadera
} else {
    //codigo a ejecutar si la condicion es falsa
}
*/

let number = +question("Ingrese un numero: ");
let number2 = +question("Ingrese otro numero: ");



if (number > number2) {
    console.log(number + " es mayor que " + number2);
} else if (number < number2) {
    console.log(number + " es menor que " + number2);
} else {
    console.log(number + " es igual que " + number2);
}