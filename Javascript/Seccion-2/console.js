//El objeto console es una herramienta de depuración que proporciona métodos para mostrar información en la consola del navegador. Aquí hay algunos ejemplos de cómo usar el objeto console:

// console.log: Nos permite mostrar un mensaje simple en la consola
console.log("Hola, muchachos!");

// console.error: Nos permite mostrar un mensaje de error en la consola
console.error("¡Ha ocurrido un error!");

// console.warn: Nos permite mostrar un mensaje de advertencia en la consola
console.warn("¡Cuidado! Esto podría causar problemas.");

//console.debug: Nos permite mostrar un mensaje de depuración en la consola
console.debug("Este es un mensaje de depuración.");


// console.assert: Nos permite mostrar un mensaje de error si una condición es falsa
console.assert(2 + 2 === 5, "¡La afirmación es falsa!");


//console.dir: Nos permite mostrar un objeto en la consola de una manera más legible
const persona = {
    nombre: "Jesus",
    edad: 30,
    ciudad: "Caracas"
};

console.dir(persona);


// console.group: Nos permite agrupar mensajes relacionados en la consola
console.group("Información de la persona");
console.log("Nombre: " + persona.nombre);
console.log("Edad: " + persona.edad);
console.log("Ciudad: " + persona.ciudad);
console.groupEnd();

// console.time y console.timeEnd: Nos permiten medir el tiempo que tarda en ejecutarse un bloque de código
console.time('Tiempo de ejecución');
// Código que se desea medir
for (let i = 0; i < 1000000; i++) {
    // Simulación de una tarea que consume tiempo
}
console.timeEnd('Tiempo de ejecución');


//console.trace: Nos permite mostrar una traza de la pila de llamadas en la consola
function funcionA() {
    funcionB();
}

function funcionB() {
    funcionC();
}

function funcionC() {
    console.trace("Traza de la pila de llamadas");
}

funcionA();

//console.table: Nos permite mostrar datos tabulares en la consola
const personas = [
    { nombre: "Jesus", edad: 30, ciudad: "Caracas" },
    { nombre: "Alejandro", edad: 25, ciudad: "Madrid" },
    { nombre: "Alfredo", edad: 35, ciudad: "Buenos Aires" }
];

console.log(personas);

console.table(personas);


//console.clear: Nos permite limpiar la consola
console.clear();