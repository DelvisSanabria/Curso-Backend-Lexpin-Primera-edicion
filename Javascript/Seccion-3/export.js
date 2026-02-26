//exportar es compartir código con otros archivos, para eso se usa la palabra reservada export, seguido de lo que queremos exportar

export function greeting() {
    return 'Hola a todos';
}

function greetingWithName(name) {
    return `Hola ${name}`;
}

function sum(a, b) {
    return a + b;
}

function substract(a, b) {
    return a - b;
}

function multiply(a, b) {
    return a * b;
}
function divide(a, b) {
    return a / b;
}

//Tenemos otra forma de exportar, que es exportar todo el código al final del archivo, para eso se usa la palabra reservada export seguida de llaves y dentro de las llaves el código que queremos exportar

export { greetingWithName, sum, substract, multiply, divide };