import {question } from "readline-sync";
import readlineSync from "readline-sync";


//funcion para pausar la ejecucion entre ejemplos
function pause(example){
  console.log("Fin del ejemplo");
  readlineSync.keyInPause("Presione enter para continuar");
  console.clear();
}

//ejemplo setTimeout
/* setTimeout es una funcion que permite ejecutar una funcion despues de un tiempo determinado

recibe como parametro la funcion a ejecutar y el tiempo en milisegundos
*/

//de forma sincrona

console.log("Numero inmediato 1");
console.log("Numero inmediato 2");

setTimeout(() => {
  console.log("Numero despues de 3 segundos");
  pause(1);
  exampleTimer();
}, 3000);


//setInterval es una funcion que permite ejecutar una funcion en intervalos de tiempo determinado

//recibe como parametro la funcion a ejecutar y el tiempo en milisegundos

function exampleTimer(){
  let count = 0;
  console.log("El contador se incrementara 5 veces, una por segundo")
  const interval = setInterval(() => {
    count++;
    console.log(`Numero despues de ${count} segundos`);
    if(count == 5){
      //clearInterval para detener el intervalo
      clearInterval(interval);
    }
    pause(1);
  }, 1000);
}