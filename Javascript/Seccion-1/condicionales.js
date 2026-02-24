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

//Operador ternario (Condicional ternario) forma abreviada de escribir una expresion condicional

/* Cuya estructura es la siguiente: 
condicion ? valor si es verdadera : valor si es falsa
*/


let result = (number > number2) ? number + " es mayor que " + number2  : number + " es menor que " + number2


console.log(result);

//Switch (Seleccion) nos permoite ejecutar un bloque de codigo basandonos en casos.

/* Cuya estructura es la siguiente:
switch (expresion) {
    case valor1:
        //codigo a ejecutar si la expresion es igual al valor1
        break;  //se utiliza para salir del switch
    case valor2:                    
        //codigo a ejecutar si la expresion es igual al valor2
        break;
    default:
        //codigo a ejecutar si la expresion no es igual a ninguno de los casos anteriores
}
*/

let day = question("Ingrese un dia de la semana: ");

switch(day.toLowerCase()) {
    case "lunes":
        console.log("Hoy es lunes");
        break;
    case "martes":
        console.log("Hoy es martes");
        break;
    case "miercoles":
        console.log("Hoy es miercoles");
        break;
    case "jueves":
        console.log("Hoy es jueves");
        break;
    case "viernes":
        console.log("Hoy es viernes");
        break;
    case "sabado":
        console.log("Hoy es sabado");
        break;
    case "domingo":
        console.log("Hoy es domingo");
        break;
    default:
        console.log("No es un dia de la semana");
        break;
}