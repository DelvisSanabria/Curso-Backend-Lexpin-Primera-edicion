//Las promesas son un objeto que representa el resultado de una operación asincrona y puede ser resuelta con exito o rechazada.

/* 

Pueden tener 3 estados:

Pending: La promesa aun no ha sido resuelta.
Fulfilled: La promesa ha sido resuelta exitosamente.
Rejected: La promesa ha sido rechazada.

su funcionamiento es similar a un callback, pero con una sintaxis mas sencilla y mas legible.


const promise = new Promise((resolve, reject) => {
  // Código que realiza la operación asincrona
  if (operacionExitosa) {
    resolve("Operación exitosa");
  } else {
    reject("Operación fallida");
  }
});

una vez creada la promesa, se pueden suscribir a ella utilizando el metodo then(), que se ejecutara cuando la promesa se resuelva exitosamente.

.catch () que se ejecutara cuando la promesa se rechace.

.finally () que se ejecutara siempre, sea exitosamente o rechazada.
*/

import { question } from "readline-sync";

function isEven(){
  console.log('Promesa sincrona')

  let evalEven = new Promise((resolve, reject) => {
    let result = question('Ingrese un numero: ');
    if (result % 2 == 0) {
      //resolve para indicar que la promesa se ha cumplido
      resolve('El numero es par');
    } else {
      //reject para indicar que la promesa no se ha cumplido
      reject('El numero es impar');
    }
  });

  //.then si se cumple la promesa hare lo siguiente
  evalEven.then((result) => {
    console.log(result);
  //.catch si no se cumple la promesa hare lo siguiente
  }).catch((error) => {
    console.log(error);
  //.finally si se cumple o no la promesa hare lo siguiente
  }).finally(() => {
    console.log('Fin de la promesa');
  });
}

isEven();


//Promesas asincronas

function isEqual(){
  console.log('Promesa asincrona')
  console.log('Esperando 5 segundos para que la promesa se resuelva');

  let evalEqual = new Promise((resolve, reject) => {
    setTimeout(function (){
      let result = 'texto' == question('Ingrese un texto: ');
      if (result) {
        resolve('El texto es igual');
      } else {
        reject('El texto es diferente');
      }
    }, 5000);
  });

  evalEqual.then((result) => {
    console.log(result);
  }).catch((error) => {
    console.log(error);
  }).finally(() => {
    console.log('Fin de la promesa');
  });
}

isEqual();

console.log('Fin del programa');


//Ejemplo para procesar datos

function processData() {
 console.log('Procesando datos...');
 console.log('esperando 3 segundos para simular una operacion asincrona');

 let movies = [
  { id: 1, name: 'Matrix', rating: 8.7 },
  { id : 2, name: 'Avatar', rating: 8.5 },
  { id : 3, name: 'Star Wars episode IV', rating: 8.3 },
  { id : 4, name: 'Star Wars episode V', rating: 8.2 },
  { id : 5, name: 'Star Wars episode VI', rating: 8.0 }
 ];

 class Movie {
  constructor(id, name) {
    this.id = id;
    this.name = name;
  }
 }

 const movieList = new Promise((resolve, reject) => {
  setTimeout(() => {
    const processMovies = movies.map((movie) => new Movie(movie.id, movie.name));

    if (processMovies.length > 0) {
      resolve(processMovies);
    } else {
      reject('No se encontraron peliculas');
    }
  }, 3000);
 });

 movieList
  .then((movies) => {
    console.log('Peliculas procesadas:');
    movies.forEach((movie) => {
      console.log(`${movie.id}: ${movie.name}`);
    });
  })
  .catch((error) => {
    console.error(error);
  });
}

processData();