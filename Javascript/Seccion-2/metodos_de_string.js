//los metodos de string son funciones que se pueden aplicar a los strings para realizar diferentes operaciones, como buscar, reemplazar, dividir, manipular, etc.

let str = "Hola que tal muchachos";


//metodo length: devuelve la longitud de un string

console.log(str.length); // 24

//metodo toUpperCase: convierte un string a mayusculas

console.log(str.toUpperCase()); // HOLA QUE TAL MUCHACHOS

//metodo toLowerCase: convierte un string a minusculas

console.log(str.toLowerCase()); // hola que tal muchachos

//metodo indexOf: devuelve la posicion de la primera ocurrencia de un substring en un string, o -1 si no se encuentra

console.log(str.indexOf("a")); // 3

//metodo lastIndexOf: devuelve la posicion de la ultima ocurrencia de un substring en un string, o -1 si no se encuentra

console.log(str.lastIndexOf("a")); // 21

//metodo slice: devuelve una parte de un string entre dos indices recibe dos parametros, el indice de inicio y el indice de fin (opcional)

console.log(str.slice(5, 8)); // que

//replace: reemplaza un substring por otro en un string, recibe dos parametros, el substring a reemplazar y el substring de reemplazo

console.log(str.replace("muchachos", "amigos")); // Hola que tal amigos


//concat: concatena dos o mas strings, recibe como parametro los strings a concatenar

let str2 = "bienvenidos a la clase de Javascript";
console.log(str.concat(" ", str2)); // Hola que tal muchachos Bienvenidos a la clase de Javascript

//split: divide un string en un array de substrings, recibe como parametro el separador

console.log(str.split(" ")); // ["Hola", "que", "tal", "muchachos"]

//join: une los elementos de un array en un string, recibe como parametro el separador

let arr = ["Hola", "que", "tal", "muchachos"];
console.log(arr.join(" ")); // Hola que tal muchachos

//trim: elimina los espacios en blanco al inicio y al final de un string

let str3 = "   Hola que tal muchachos   ";
console.log(str3.trim()); // Hola que tal muchachos


//startsWith: devuelve true si un string comienza con un substring, o false si no
console.log(str.startsWith("Hola")); // true
console.log(str.startsWith("hola")); // false

//endsWith: devuelve true si un string termina con un substring, o false si no
console.log(str.endsWith("muchachos")); // true
console.log(str.endsWith("Muchachos")); // false