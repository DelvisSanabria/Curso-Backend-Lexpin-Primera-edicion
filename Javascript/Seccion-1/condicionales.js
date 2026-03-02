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

/*
    Realiza un menu que permita elegir que clase de producto se desea comprar, y en base a la eleccion del usuario mostrar
    el producto que selecciono.

    El menu debe contener 8 productos diferentes y en caso de seleccionar un producto que no se muestre en la lista
    indicar que no se encuentra disponible.

    Utilizar: question y switch, No se deben utilizar variables.
*/


/* 
    Extension 1 del ejercicio anterior, utilizando el mismo menú mostrar 3 o 4 opciones de cada tipo de producto.
*/

/* ACTIVIDAD - Juego del semaforo.

    Crea un mensaje en pantalla que muestre 3 colores a elegir: 
    VERDE, AMARILLO, ROJO.
    Guarda la respuesta en una variable llamada color.

    Ejemplo: Elige un color para iniciar:
    1) VERDE
    2) AMARILLO
    3) ROJO
    OTRO) Opcion invalida


    Luego crea otro mensaje en pantalla que muestre una situacion con el color ingresado previamente
    y 3 opciones a elegir: Pasar normalmente, Acelerar y Esperar.
    Guarda la respuesta en una variable llamada accion.

    Ejemplo: 
        - El semaforo esta de color ROJO, ¿Que desea hacer?
        1) Pasar normalmente
        2) Acelerar
        3) Esperar
        OTRO) Opcion invalida


    Luego crea la logica con Switch-Case que evalue las respuestas ingresadas en la consola
    y en base a ello inicie un caso.


    Si la luz es VERDE evaluar:
    - Si el jugador pasa normalmente:
        mostrar un mensaje que diga: Bien hecho!, pasaste en el momento adecuado ✅, ¡Has ganado! 😁
    - Sino, Si el jugador acelera:
        mostrar un mensaje que diga: Oh no!, Aceleraste demasiado y chocaste 💥, ¡Has perdido! 😞
    - Sino, Si el jugador espera:
        mostrar un mensaje que diga: Oh no!, Creaste un bloqueo y los demas conductores estan furiosos 🤬, ¡Has Perdido! ❌
    - De lo contrario
        mostrar un mensaje que diga: Respuesta invalida.
    
    
    Si la luz es AMARILLO evaluar:
    - Si el jugador pasa normalmente:
        mostrar un mensaje que diga: Oh no!, No aceleraste lo suficiente y te han chocado 💥, ¡Has perdido! ❌
    - Sino, Si el jugador acelera:
        mostrar un mensaje que diga: Bien hecho!, pasaste en el momento justo ✅, ¡Has ganado! 😁
    - Sino, Si el jugador espera:
        mostrar un mensaje que diga: Oh no!, Creaste un bloqueo y los demas conductores estan furiosos 🤬, ¡Has Perdido! 😞
    - De lo contrario
        mostrar un mensaje que diga: Respuesta invalida.


    Si la luz es ROJO evaluar:
    - Si el jugador pasa normalmente:
        mostrar un mensaje que diga: Oh no!, Pasaste en el momento indebido ❌, ¡Has perdido! 😞
    - Sino, Si el jugador acelera:
        mostrar un mensaje que diga: Oh no!, Crusaste mientras autos en otra direccion pasaban y chocaste 💥, ¡Has Perdido! ❌
    - Sino, Si el jugador espera:
        mostrar un mensaje que diga: Bien hecho!, Esperaste en el momento adecuado ✅, ¡Has ganado! 😁
    - De lo contrario
        mostrar un mensaje que diga: Respuesta invalida.


    PISTA: en algun momento necesitaras usar if-else y el operador AND/&&
    PISTA 2: Para los mensajes de retorno puedes usar console.log()
*/