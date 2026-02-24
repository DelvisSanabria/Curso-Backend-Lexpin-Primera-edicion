//Los tipos de datos en JavaScript son:

//tipos de datos primitivos

// 1. String : es una cadena de texto, se representa con comillas simples o dobles
let username = "Alejandro";
username = 'Alejandro';
username = `Alejandro`;

console.log(typeof username); // string
console.log(typeof("Alfredo")); // string

// 2. Number : es un numero, se representa sin comillas
let age = 30;
console.log(typeof age);

let price = 19.99;
console.log(typeof price); // number
console.log(typeof(3.14)); // number

// 3. Boolean : es un valor lógico que puede ser verdadero o falso, se representa con las palabras reservadas true o false
let isStudent = true;
console.log(typeof isStudent); // boolean

let isTeacher = false;
console.log(typeof isTeacher); // boolean

// 4. Null : es un valor nulo, se representa con la palabra reservada null
let emptyValue = null;
console.log(typeof emptyValue); // object (esto es un error en JavaScript, pero se mantiene por compatibilidad)

//tipos de datos no primitivos

//1. Array : es una colección de datos ordenada, se representa con corchetes []
let numbers = [1, 2, 3, 4, 5];
console.log(typeof numbers); // object

// 2. Object : es una colección de datos no ordenada, se representa con llaves {}
let person = {
    name: "Alejandro",
    age: 30,
    gender: "male"
};

console.log(typeof person); // object