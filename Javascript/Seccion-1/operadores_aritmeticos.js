//Son los operadores que nos permiten realizar operaciones matematicas con los valores de las variables

let num1 = 10;
let num2 = 5;

// Suma : se representa con el operador +
let sum = num1 + num2;
console.log("La suma es: " + sum); // La suma es: 15
console.log("Esto" + " es" + " una" + " concatenación"); // Esto es una concatenación

// Resta : se representa con el operador -
let difference = num1 - num2;
console.log("La resta es: " + difference); // La resta es: 5

// Multiplicación : se representa con el operador *
let product = num1 * num2;
console.log("La multiplicación es: " + product); // La multiplicación es: 50

// División : se representa con el operador /
let quotient = num1 / num2;
console.log("La división es: " + quotient); // La división es: 2

// Módulo : se representa con el operador % y nos devuelve el residuo de la división
let remainder = num1 % num2;
console.log("El residuo es: " + remainder); // El residuo es: 0

//Tendremos tambien los operadores de incremento y decremento

// Incremento : se representa con el operador ++ y nos incrementa el valor de la variable en 1
num1++;
console.log("El valor de num1 después del incremento es: " + num1); // El valor de num1 después del incremento es: 11

// Decremento : se representa con el operador -- y nos decrementa el valor de la variable en 1
num2--;
console.log("El valor de num2 después del decremento es: " + num2); // El valor de num2 después del decremento es: 4

//Negacion unitaria : se representa con el operador - y nos devuelve el valor negativo de la variable
let negativeNum1 = -num1;
console.log("El valor negativo de num1 es: " + negativeNum1); // El valor negativo de num1 es: -11

//Exponente : se representa con el operador ** y nos devuelve el valor de la variable elevado a la potencia de la segunda variable
let power = num1 ** num2;
console.log("El valor de num1 elevado a la potencia de num2 es: " + power); // El valor de num1 elevado a la potencia de num2 es: 14641