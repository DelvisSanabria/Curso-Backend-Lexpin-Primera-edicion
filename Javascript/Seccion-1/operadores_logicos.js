//Los operadores logicos son utilizados para combinar o modificar expresiones booleanas. Los operadores lógicos más comunes son:

//AND (&&): Devuelve true si ambas expresiones son verdaderas. Ejemplo: true && true devuelve true, pero true && false devuelve false.

console.log(true && true) // Devuelve true
console.log(true && false) // Devuelve false
console.log(0 && "hola") // Devuelve 0, porque el operador AND devuelve el primer valor falso que encuentra o el último valor si todos son verdaderos.

console.log((5 > 3) && (7 < 4)) 
// Devuelve false, porque aunque 5 > 3 es true, 7 < 4 es false, y el operador AND requiere que ambas expresiones sean verdaderas para devolver true.

//OR (||): Devuelve true si al menos una de las expresiones es verdadera. Ejemplo: true || false devuelve true, pero false || false devuelve false.

console.log(true || false) // Devuelve true
console.log((5 > 3) || (7 < 4))

//NOT (!): Devuelve el valor opuesto de la expresión. Ejemplo: !true devuelve false, y !false devuelve true.

console.log(!true) // Devuelve false
console.log((!(5 > 3) && (2 < 4))) // Devuelve false, porque 5 > 3 es true, y el operador NOT invierte ese valor a false.

// (Facil)
let uno = !true || false;
let dos = false && !false;
let tres = true && !false;

//(Medio)
let cuatro = (5 === 5) || (!true);
let cinco = (!0) || (5 < 0);
let seis = (3 > 4) && (!0);   

//Avanzado
let siete = ( ((false || true) && (!false && true) )) || (true && false)
let ocho = (6 === 3+3) && (9/3 >= 3);
let nueve = (!(!false) || ( ("1" == 1)) && (!false === true) ); 

//Hardcore
let diez = !(!true) === !( !( 5 >= 5 ) );
let once = !( true && (!true === !( !(8 === 4*2) )) );

//Ultra-Hardcore
let doce = !( true && (!true === !( !(16 === (4*2) + 8))) ) !== (false);

//Leyenda
let trece = !(((!(!(10 / 5 == "2") === false) != false) === ((5 * 5) <= (100 / 4))) && (!((1 + 1) !== (10 / 5)) !== (true)));


// Roto
let catorce = !(!(!(1)) && (50 * "0" === 0) !== (false) || !(("20"+24) === (4028/2)));