//Los metodos de array nos permiten realizar operaciones sobre los arrays, como agregar, eliminar o modificar elementos, entre otras cosas. A continuación, se presentan algunos de los metodos de array mas comunes:

let colors = ["red", "green", "blue"];


//Para mostrar valores:

console.log(colors[0]); // "red"


//Reasignar valores:

colors[1] = "yellow";
console.log(colors); // ["red", "yellow", "blue"]

//Metodos para medir el tamaño de un array: 

//length: Devuelve el numero de elementos en un array.

console.log(colors.length); // 3

//push: Agrega uno o mas elementos al final de un array y devuelve la nueva longitud del array.

colors.push("orange");
console.log(colors); // ["red", "yellow", "blue", "orange"]

//unshift: Agrega uno o mas elementos al inicio de un array y devuelve la nueva longitud del array.

colors.unshift("purple");
console.log(colors); // ["purple", "red", "yellow", "blue", "orange"]

//pop: Elimina el ultimo elemento de un array y lo devuelve.

let lastColor = colors.pop();
console.log(lastColor); // "orange"
console.log(colors); // ["purple", "red", "yellow", "blue"]


//shift: Elimina el primer elemento de un array y lo devuelve.

let firstColor = colors.shift();
console.log(firstColor); // "purple"
console.log(colors); // ["red", "yellow", "blue"]

//indexOf: Devuelve el primer indice en el que se encuentra un elemento dado en un array, o -1 si no se encuentra.

console.log(colors.indexOf("yellow"));

const element = colors.indexOf("yellow");
console.log(element); // 1

colors.splice(element, 1);
console.log(colors); // ["red", "blue"]

//Funciones de orden superior: Son funciones que toman otras funciones como argumentos o devuelven funciones como resultado. Algunos ejemplos de funciones de orden superior en JavaScript son:

//filter: Crea un nuevo array con todos los elementos que cumplan una condicion especificada por una funcion.


let numbers = [1, 2, 3, 4, 5];

function isEven(num) {
  return num % 2 === 0;
}

let evenNumbers = numbers.filter(isEven);

//Tambien se puede escribir de la siguiente manera pasandole una funcion anonima:
let evenNumbers2 = numbers.filter(function(num) {
  return num % 2 === 0;
}
);

//Tambien se puede escribir de la siguiente manera pasandole una funcion flecha:
let evenNumbers3 = numbers.filter(num => num % 2 === 0);

console.log(evenNumbers); // [2, 4]
console.log(evenNumbers2); // [2, 4]
console.log(evenNumbers3); // [2, 4]

//find: Devuelve el valor del primer elemento del array que cumple la condicion especificada por una funcion.

let namesTwo = ["Alfredo", "Alejandro", "Delvis"];

function findingName(name, findingName) {
  return name === findingName;
}

let foundName = namesTwo.find(name => findingName(name, "Alejandro"));

console.log(foundName); // "Alejandro"

//fill: Rellena todos los elementos de un array desde una posicion inicial hasta una posicion final con un valor estatico.

let fruits = ["apple", "banana", "orange"];

fruits.fill("grape", 1, 2);
console.log(fruits); // ["apple", "grape", "orange"]

//every: Devuelve true si todos los elementos del array cumplen la condicion especificada por una funcion.

let ages = [17, 11, 25];

function isAdult(age) {
  return age >= 18;
}

let allAdults = ages.every(isAdult);

//Tambien se puede escribir de la siguiente manera pasandole una funcion anonima:
let allAdults2 = ages.every(function(age) {
  return age >= 18;
}
);

//Tambien se puede escribir de la siguiente manera pasandole una funcion flecha:
let allAdults3 = ages.every(age => age >= 18);

console.log(allAdults); // false

//some: Devuelve true si al menos un elemento del array cumple la condicion especificada por una funcion.

let hasAdult = ages.some(isAdult);
console.log(hasAdult); // true

//forEach: Ejecuta una funcion para cada elemento del array.

const students = ["Jesus", "Alfredo", "Alejandro","Ivan","Andreina"];

const greetings = students.forEach(student => console.log(`Hola, ${student}!`));


//sort: Ordena los elementos de un array in situ y devuelve el array ordenado.

let numbersTwo = [3, 1, 4, 1, 5, 9];

numbersTwo.sort();
console.log(numbersTwo); // [1, 1, 3, 4, 5, 9]

//Ordernar de forma descendente:

numbersTwo.sort((a, b) => b - a);
console.log(numbersTwo); // [9, 5, 4, 3, 1, 1]

//ordenar nombres:

students.sort();  
console.log(students)

//reverse: Invierte el orden de los elementos de un array in situ y devuelve el array invertido.

students.reverse();
console.log(students); // ["Ivan", "Jesus", "Andreina", "Alfredo", "Alejandro"]

//map: Crea un nuevo array con los resultados de la ejecucion de una funcion para cada elemento del array.

function greeting(student) {
  return `Hola, ${student}!`;
}

let greetingsTwo = students.map(greeting);
console.log(greetingsTwo)

//Tambien se puede escribir de la siguiente manera pasandole una funcion anonima:
let greetingsThree = students.map(function(student) {
  return `Hola, ${student}!`;
}
);

//Tambien se puede escribir de la siguiente manera pasandole una funcion flecha:
let greetingsFour = students.map(student => `Hola, ${student}!`);