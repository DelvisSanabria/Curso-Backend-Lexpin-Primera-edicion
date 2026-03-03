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
    cronometro();
  }, 1000);
}


//Cronometro basico por consola

function cronometro(){
  console.log('Cronometro basico por consola');
  //Creamos una variable para poder detener el cronometro
  let increment;
  //Creamos una variable para almacenar el tiempo y si esta corriendo el contador
  let time = 0;
  let isRunning = false;

  console.log("controla el cronometro con los comandos 'start', 'stop', 'reset' y exit");

  while(true){
    const command = question("Comando: ");
    if(command === 'start'){
      if(!isRunning){
        console.log("Cronometro iniciado");
        isRunning = true;
        increment = setInterval(() => {
          time++;
          //procces.stdout.write para mostrar el cronometro en la consola en la misma linea
          console.log(`Tiempo: ${time} segundos`);
        }, 1000)
      }else {
        console.log("Cronometro ya esta corriendo");
      }
    } else if (command === 'stop'){
      if(isRunning){
        console.log("Cronometro detenido");
        isRunning = false;
        clearInterval(increment);
      }
    } else if (command === 'reset'){
      console.log("Cronometro reiniciado");
      time = 0;
      if(!isRunning){
        console.log(`Tiempo: ${time} segundos`);
      }
    } else if (command === 'exit'){
      if(isRunning){
        console.log("Cronometro detenido");
        clearInterval(increment);
        break;
      }
    } else {
      console.log("Comando no reconocido");
    }
  }
}