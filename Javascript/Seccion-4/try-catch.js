//try-catch nos ayuda a manejar errores en Javascript
/* 
la estructura de un try-catch es la siguiente:
try {
  //codigo que puede generar un error
} catch (error) {
  //codigo que se ejecutara si hay un error
} 
  
*/

const myVariable = "hola";

try {
  console.log(myVariable.toUpperCase());
} catch (error) {
  console.log(error);
}

console.log("El codigo sigue ejecutandose");

//la estructura finally nos ayuda a ejecutar codigo independiente de si hay un error o no
try {
  console.log(myVariable.toUpperCase());
} catch (error) {
  console.error( error)
} finally {
  console.log("El codigo sigue ejecutandose");
}