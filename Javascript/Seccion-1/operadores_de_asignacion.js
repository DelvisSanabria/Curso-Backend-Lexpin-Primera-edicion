//los operadores de asignacion nos sirven para asignar valores a variables

//operador de asignacion basico (=) nos sirve para asignar un valor a una variable
let num1 = 10;
let num2 = 37;

//operadores de asignacion compuestos nos sirven para asignar un valor a una variable y realizar una operacion al mismo tiempo

//operador de asignacion suma (+=) nos sirve para sumar un valor a una variable y asignar el resultado a la misma variable
num1 = 5;

num1 += 10; // num1 = num1 + 10

console.log(num1); // 15

//operador de asignacion resta (-=) nos sirve para restar un valor a una variable y asignar el resultado a la misma variable
num1 -= 5; // num1 = num1 - 5
console.log(num1); // 10

//operador de asignacion multiplicacion (*=) nos sirve para multiplicar un valor a una variable y asignar el resultado a la misma variable
num1 *= 2;
console.log(num1); // 20

//operador de asignacion division (/=) nos sirve para dividir un valor a una variable y asignar el resultado a la misma variable
num1 /= 4;
console.log(num1); // 5

//operador de asignacion modulo (%=) nos sirve para obtener el resto de una division y asignar el resultado a la misma variable
num1 %= 3;
console.log(num1); // 2

//operador de asignacion exponenciacion (**=) nos sirve para elevar un valor a una variable y asignar el resultado a la misma variable
num1 **= 3;
console.log(num1); // 8

//Operador de miembro (.) nos sirve para acceder a las propiedades de un objeto
let persona = {
    nombre: "Alejandro",
    edad: 30
};

console.log(persona.nombre); // Alejandro


//Spreed operator (...) nos sirve para copiar los elementos de un array o las propiedades de un objeto a otro array u objeto y tambien para descomponer un array u objeto en elementos individuales

//copiar un array
let numeros = [1, 2, 3];
let copiaNumeros = [...numeros, 4, 5];
console.log(copiaNumeros); // [1, 2, 3, 4, 5]
console.log(...numeros); // 1 2 3