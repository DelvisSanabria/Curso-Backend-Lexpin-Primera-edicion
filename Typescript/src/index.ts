//El tipado estatico se refiere a que cada variable debe tener un tipo de dato especifico.

//tipado de datos primitivos

//tipo de dato number
let age: number = 30
console.log(age);

//tipo de dato string
let username: string = "Alejandro"
console.log(username);

//tipo de dato boolean
let isStudent: boolean = true
console.log(isStudent);

isStudent = false
console.log(isStudent);

//tipo de dato any
let anyValue: any = "Alfredo"
console.log(anyValue);

//tipo de dato null
let nullValue: null = null
console.log(nullValue);


//tipo de dato undefined
let undefinedValue: undefined = undefined
console.log(undefinedValue);

//tipado de datos complejos

//tipo de dato array
let numbers: number[] = [1, 2, 3, 4, 5]

let names: [string, string, number] = ["Alejandro", "Alfredo", 30]

console.log(numbers);
console.log(names);

//tipo de dato objeto
let person: {name: string, age: number} = {name: "Alejandro", age: 30}

console.log(person);

//los enums son una manera de crear un tipo de dato personalizado que puede tener varios valores.
enum namesTwo {
  "Alejandro",
  "Alfredo",
  "Jesus",
  "Andreina"
}

let color: namesTwo = namesTwo.Andreina
console.log(color);


//tipo de dato void
function printMessage(message: string): void {
  console.log(message);
}

printMessage("Hola muchachos!");


//inferencia de tipos

let papata = "Alfredo"
papata = "Alejandro"
console.log(papata);


//Union de tipos
let Data: string | number = "Alfredo"
Data = 30
console.log(Data);


//Tipos literales

let colorTwo: "red" | "blue" | "green" = "red"
colorTwo = "blue"
console.log(colorTwo);


//Interfaces : Son un contrato que define las propiedades y los metodos que debe tener un objeto.

interface Person {
  name: string;
  age: number;
}

let person1: Person = {name: "Jesus", age: 30}
console.log(person1);

//Tipos de intercepcion

interface HaveName {
  name: string;
}

interface HaveAge {
  age: number;
}

//Para crear tipos se utiliza la palabra reservada "type"
type PersonTwo = HaveName & HaveAge

let contact : PersonTwo = {name: "Jesus", age: 30}
console.log(contact);

function sayHello(person: PersonTwo) {
  console.log(`Hello, ${person.name}! You are ${person.age} years old.`);
}

sayHello({name: "Jesus", age: 30})


//Propiedades opcionales y solo lectura de las interfaces

interface PersonThree {
  name: string;
  age?: number; //indica que la propiedad es opcional
  readonly isStudent: boolean; //indica que la propiedad es solo lectura
}

let person3: PersonThree = {name: "Jesus", isStudent: true}
console.log(person3);

//Tipos de funciones

function add(a: number, b: number): number {
  return a + b;
}

console.log(add(1, 2));

//puedo definir la firma de una funcion

type operation = (a: number, b: number) => number

let sum: operation = (a, b) => a + b

let sum2: operation = function(a, b) {
  return a + b
}
console.log(sum(1, 2));

//Los genericos son una manera de crear tipos que pueden ser usados en cualquier parte del codigo.

function identity<T>(value: T): T {
  return value;
}

let identityOne = identity<string>("Hello");
let identityTwo = identity<number>(1);
let identityThree = identity(true);
console.log(identityOne);
console.log(identityTwo);
console.log(identityThree);

//Utilidades de tipos

interface User {
  id: number;
  name: string;
  email: string
  password?: string
}

//Partial: crea un tipo que contiene todas las propiedades de otro tipo, pero las propiedades son opcionales
type UserPartial = Partial<User>

function updateUser(id: number, updates: UserPartial) {
  return {
    id,
    ...updates
  }
}

//Pick: crea un tipo que contiene solo las propiedades de otro tipo
type UserPick = Pick<User, "id" | "name">

const perfil: UserPick = {
  id: 1,
  name: "Alejandro"
}

console.log(perfil);

//Omit: crea un tipo que contiene todas las propiedades de otro tipo, pero excluye las propiedades especificadas
type UserOmit = Omit<User, "password">

const user: UserOmit = {
  id: 1,
  name: "Alejandro",
  email: "hWf0K@example.com"
}

//readonly: crea un tipo que contiene todas las propiedades de otro tipo, pero las propiedades son solo lectura
type UserReadonly = Readonly<User>

const userReadonly: UserReadonly = {
  id: 1,
  name: "Alejandro",
  email: "hWf0K@example.com"
}

console.log(userReadonly);

//Record: crea un tipo que contiene un conjunto de pares clave-valor
type UserRecord = Record<"name" | "email", string>

const userRecord: UserRecord = {
  name: "Alejandro",
  email: "hWf0K@example.com"
}

console.log(userRecord);

type embajadores = Record<string, User>

const embajadores: embajadores = {
  "Alejandro": {
    id: 1,
    name: "Alejandro",
    email: "hWf0K@example.com"
  },
  "Andreina": {
    id: 2,
    name: "Pablo",
    email: "hWf0K@example.com"
  }
}

/* 

Ejercicio para práctica en clase: "El Sistema de Biblioteca"

Objetivo: Aplicar interfaces, uniones y tipos literales.

1. Crea una interfaz `Libro` con las propiedades: `id` (string o número), `titulo` (string), `autor` (string) y `estado` (un tipo literal: `"disponible"` o `"prestado"`).
2. Crea una interfaz `Usuario` con: `nombre` (string) y un arreglo opcional de `Libros` prestados.
3. Crea una función llamada `prestarLibro` que reciba un `Libro` y un `Usuario`.
    - La función debe cambiar el estado del libro a `"prestado"`.
    - Debe agregar el libro al arreglo del usuario.
    - Debe retornar un mensaje confirmando la acción.
4. Añade una propiedad `readonly` al `id` del libro para que nadie pueda cambiarlo accidentalmente.

Tip: Recuerda inicializar el arreglo de libros del usuario si este no existe al momento de prestarle uno.

*/