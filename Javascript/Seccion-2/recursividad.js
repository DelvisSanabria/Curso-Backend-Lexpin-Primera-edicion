//La recursividad es una técnica de programación en la que una función se llama a sí misma para resolver un problema. Es una forma elegante y eficiente de resolver problemas que pueden ser divididos en subproblemas más pequeños.

import readlineSync from 'readline-sync'

//Ejemplo de función recursiva contador hacia atrás:
function countdown(number) {
    if (number <= 0) {
        console.log("¡Despegue!");
        startTransport();
    } else {
        console.log('Contando hacia atrás, vamos por el numero:', number);
        setTimeout(() => {
          countdown(number - 1); // Llamada recursiva con un número decreciente
        }, 1000); // Espera 1 segundo antes de la siguiente llamada
    }
}

function startCountdown() {
    const startNumber = 5;
    countdown(startNumber);
}

startCountdown();

let tickets = 10;

function deduccion(){
  console.log(`\nBienvenido, su saldo actual es: ${tickets} tickets.`);
  
  if (tickets > 0){
    tickets--;
    console.log(`Viaje realizado, Viajes restantes: ${tickets}`);
    let continueWay = readlineSync.keyInYNStrict('¿Desea realizar otro viaje?');
    if (continueWay) {
      deduccion(); // Llamada recursiva para realizar otro viaje
    } else {
      console.log('Gracias por usar nuestro servicio. ¡Hasta luego!');
    }
  }else {
    let recharge = readlineSync.question(`Saldo, insuficiente, ¿Que deseas hacer?\n1. Recargar tickets\n2. comprar bono mensual\n 3. Pagar 1 viaje\n Elige una opcion:\n`);
    switch (+recharge) {
      case 1:
        rechargeTickets();
        break;
      case 2:
        rechargeBono();
        break;
      case 3:
        payViaje();
        break;
      default:
        console.log('Opción no válida. Por favor, elige una opción válida.');
        deduccion();
    }
  }
}

function rechargeTickets() {
  tickets = 10;
  console.log(`Tickets recargados. Su saldo actual es: ${tickets} tickets.`);
  deduccion(); // Llamada recursiva para continuar con la deducción
}

function rechargeBono() {
  tickets = 30;
  console.log(`Bono mensual adquirido. Su saldo actual es: ${tickets} tickets.`);
  deduccion(); // Llamada recursiva para continuar con la deducción
}

function payViaje() {
  tickets = 1;
  console.log(`Pagaste 1 viaje. Su saldo actual es: ${tickets} tickets.`);
  deduccion(); // Llamada recursiva para continuar con la deducción
}

function startTransport() {
  let start = readlineSync.keyInYNStrict('¿Desea iniciar el transporte?');
  if (start) {
    deduccion(); // Llamada recursiva para iniciar la deducción de tickets
  } else {
    console.log('Gracias por usar nuestro servicio. ¡Hasta luego!');
  }
}