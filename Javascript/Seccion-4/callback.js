//Un callback es una funcion que se pasa como argumento a otra funcion,
//pero se ejecuta despues de que la otra funcion se haya ejecutado

const numbers = [1,2,3,4,5];
const result = numbers.map(
  function(item) {
    return item * 2;
  }
);
console.log(result);

//Ejemplo de callback personalizada

function add(myArray, data, callback) {
  //Hacemos algo
  myArray.push(data);
  //Se ejecuta el callback
  callback(myArray);
}

let names = ["Alfredo", "Jesus", "Andreina", "Alejandro"];

function showNames(array) {
  console.log("Los nombres son: ");
  console.log(array);
}

add(names, "Ivan",showNames);


//Hacer una caculadora con callbacks

function operation(num1, num2, callback) {
  console.log(callback(num1, num2));
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

operation(5, 3, sum);
operation(5, 3, substract);
operation(5, 3, multiply);
operation(5, 3, divide);


//Cuidarse del callback hell