//La desectruturación es una forma de extraer valores de objetos o arreglos y asignarlos a variables de manera más concisa.

//Desectruturación de arrays

const numbers = [1, 2, 3, 4, 5];

const one = numbers[0];
const two = numbers[1];
const three = numbers[2];

console.log(one, two, three); // Output: 1 2 3

//Con desectruturación

const [first, second, third] = numbers;

console.log(first, second, third); // Output: 1 2 3


//Desectruturación de objetos

const person = {
    name: 'John',
    age: 30,
    city: 'New York',
    directions: {
        street: '123 Main St',
        zip: '10001'
    }
};

//Sin desectruturación

const names = person.name;
const age = person.age;
const city = person.city;
const street = person.directions.street;

console.log(names, age, city); // Output: John 30 New York

//Con desectruturación

const { name: namesTwo, age: ageTwo, city: cityTwo, directions: { street: streetTwo } } = person;

console.log(namesTwo, ageTwo, cityTwo, streetTwo); // Output: John 30 New York 123 Main St