//Hacer import es traernos el código de otro archivo, para eso se usa la palabra reservada import, seguido de lo que queremos importar y luego de donde lo queremos importar

import { greeting, greetingWithName, sum, substract, multiply, divide } from './export.js';

console.log(greeting());
console.log(greetingWithName('Andreina'));
console.log(sum(5, 3));
console.log(substract(5, 3));
console.log(multiply(5, 3));
console.log(divide(5, 3));