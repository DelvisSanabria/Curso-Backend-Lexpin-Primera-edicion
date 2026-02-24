//EL alcance de una variable es el area de nuestro programa donde esta definida, es decir, donde podemos usarla

//El scope global es el alcance que tiene una variable definida en el contexto global, es decir, fuera de cualquier función o bloque de código. Estas variables pueden ser accedidas desde cualquier parte del programa.

//El scope local es el alcance que tiene una variable definida dentro de una función o bloque de código. Estas variables pueden ser accedidas solo dentro de esa función o bloque de código.


let variableGlobal = "Soy una variable global";

function printVariableGlobal() {
    console.log(variableGlobal);
}

printVariableGlobal(); // Imprime: Soy una variable global

function printVariableLocal() {
    let variableLocal = "Soy una variable local";
    console.log(variableLocal);
}

printVariableLocal(); // Imprime: Soy una variable local

console.log(variableLocal); // Error: variableLocal is not defined