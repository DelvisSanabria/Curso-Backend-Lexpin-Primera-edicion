//Las funciones son bloques de código reutilizables que realizan una tarea específica. Se pueden definir con la palabra clave "function" seguida del nombre de la función y un conjunto de paréntesis que pueden contener parámetros.


/* Cuya sintaxis es la siguiente:
function nombreDeLaFuncion(parametro1, parametro2, ...) {
    // Código a ejecutar
}
*/

import { question } from "readline-sync";

//Funciones declarativas 

function greeting(){
  console.log("¡Hola, bienvenido a mi programa!");
}

greeting();


//Funciones con retorno explicito y parametros

function sum(a, b){
  return a + b;
}

const resultado = sum(5, 3);

console.log("El resultado de la suma es: " + resultado);


//Funciones de expresion o anonimas

let multiply = function(a, b){
  return a * b;
}

console.log("El resultado de la multiplicación es: " + multiply(4, 6));


//Hoisting: Las funciones declarativas se elevan al inicio del ámbito, lo que significa que pueden ser llamadas antes de su declaración en el código. Sin embargo, las funciones de expresión no se elevan, por lo que deben ser definidas antes de ser utilizadas.

//Llamos primero a la funcion declarativa antes de su definicion
console.log("El resultado de la division es: " + divide(10, 2));


function divide(a, b){
  return a / b;
}

//Funciones flecha: Son una forma más concisa de escribir funciones en JavaScript. Se introdujeron en ES6 y utilizan la sintaxis de flecha (=>) para definir funciones. Las funciones flecha no tienen su propio contexto "this" y no pueden ser utilizadas como constructores.

/* cuya sintaxis es la siguiente:
const nombreDeLaFuncion = (parametro1, parametro2, ...) => {
    // Código a ejecutar
}

*/

//Cuando yo no tengo llaves y solo tengo una linea de codigo, puedo omitir las llaves y el return, quedando de la siguiente manera y el retorno es implicito:
const subtract = (a, b) =>  a - b;

//Si tuviera mas de una linea de codigo, entonces si debo usar las llaves y el return explicito, quedando de la siguiente manera:
const subtractWithBraces = (a, b) => {
  const result = a - b;
  return result;
}

console.log("El resultado de la resta es: " + subtract(10, 4));
  
const cochinada = () => sum(2,3);