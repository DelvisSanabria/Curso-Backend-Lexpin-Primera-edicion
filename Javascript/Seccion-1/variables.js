/* Comentario de varias lineas
Este es un comentario de varias lineas
que se extiende por varias lineas
*/

// Comentario de una sola linea

// Las variables : son espacios de memoria que se utilizan para almacenar datos


//tipos de variables

// var : es una variable global que se puede reasignar y redeclarar (no se recomienda su uso deprecado)

var username = "Alejandro";
console.log(username); // Alejandro

//reasignar variable
username = "Alfredo";
console.log(username); // Alfredo

// redeclarar variable
var username = "Jesus";
console.log(username); // Jesus

// let : es una variable local (pero puede ser global segun el contexto) que se puede reasignar pero no se puede redeclarar

let age = 30;
console.log(age); // 30

//reasignar variable
age = 31;
console.log(age); // 31

// redeclarar variable (no se puede redeclarar con let, esto generará un error)

//let age = 32;

// const : es una variable local (pero puede ser global segun el contexto) no se puede reasignar ni redeclarar, debe ser inicializada al momento de su declaración.

const PI = 3.14;
console.log(PI); // 3.14

// reasignar variable (no se puede reasignar con const, esto generará un error)

//PI = 3.1416;


//Podemos pedir al usuario que ingrese un valor utilizando la función prompt() y almacenarlo en una variable

let userInput = prompt("Ingrese tu nombre:");
//la concatenación de cadenas de texto se puede hacer con el operador
console.log("Hola, " + userInput + "!");

alert("Bienvenido, " + userInput + "!");


//Podemos convertir el valor del usuario a un numero 
let num1 = +prompt("Ingrese un numero:");
let num2 = +prompt("Ingrese otro numero:");

alert("La suma de " + num1 + " y " + num2 + " es: " + (num1 + num2));