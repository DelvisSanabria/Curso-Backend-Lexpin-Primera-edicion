//Las expresiones regulares son patrones que se utilizan para buscar y manipular texto. En JavaScript, se pueden crear expresiones regulares utilizando la sintaxis de barra (/) o el constructor RegExp.

//Ejemplo de expresión regular utilizando la sintaxis de barra
const regex1 = /\d{3}-\d{3}-\d{4}/;

//seria un formato de numero telefonico : 123-456-7890

/* 

Sintaxis de barra:
/patrón/modificadores/

modificadores: i (ignorar mayúsculas y minúsculas), g (global), m (multilínea), s (dotall), u (unicode), y (sticky)

coincidencias basicas:
. (cualquier caracter excepto nueva línea)
\d (cualquier dígito)
\D (cualquier carácter que no sea un dígito)
\w (cualquier carácter de palabra (letras, dígitos o guiones bajos))
\W (cualquier carácter que no sea de palabra)
\s (cualquier espacio en blanco)
\S (cualquier carácter que no sea un espacio en blanco)
^ (inicio de la cadena)
$ (final de la cadena)
\b (límite de palabra)
\ (carácter de escape)

cuantificadores:
*  coincide (0 o más veces)
+ coincide (1 o más veces)
? coincide (0 o 1 vez)
{n} coincide exactamente n veces
{n,} coincide al menos n veces
{n,m} coincide entre n y m veces

Conjuntos de caracteres:
[abc] coincide con cualquiera de los caracteres a, b o c
[^abc] coincide con cualquier carácter que no sea a, b o c
[a-z] coincide con cualquier letra minúscula
[A-Z] coincide con cualquier letra mayúscula
[0-9] coincide con cualquier dígito

grupos de captura:
(patrón) coincide con el patrón y lo captura para su uso posterior
(?:patrón) coincide con el patrón sin capturarlo
(?<nombre>patrón) coincide con el patrón y lo captura con un nombre específico

| (pipe) coincide con cualquier uno de los patrones a la izquierda o a la derecha

*/

import { question } from "readline-sync";
import readlineSync from "readline-sync";

const paragraph = `Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda,
y se utilizan para hacer comparaciones con texto. Se utilizan en muchos lenguajes de programación,
incluyendo JavaScript, para verificar si una cadena de texto cumple con un determinado patrón o 
para reemplazar texto por un patrón determinado. Las expresiones regulares se representan con 
una sintaxis especial que permite especificar patrones complejos y se pueden usar en una 
variedad de tareas, como validación de formularios, extracción de información de un párrafo y más

Ejemplo: 

Daniel Moran	
934 123 45 67
daniel_m@hotmail.com
www.dmoram.com

Migel Soto
934-234-56-78
miguel123@outlook.com
https://www.miguel.com.cl
http://alejandro.com.mx

Camila Duran
412 345 67 89
cami-duran@gmail.com
www.camila.shop
`;

//Ejemplo de uso de expresiones regulares para extraer números de teléfono
const phoneRegex = /\d{3}[-\s]\d{3}[-\s]\d{2}[-\s]\d{2}/gi;

console.log("Números de teléfono encontrados:");
const phoneMatches = paragraph.match(phoneRegex);
console.log(phoneMatches);

//Ejemplo de uso de expresiones regulares para extraer urls
const urlRegex = /https?:\/\/(www\.)?\w+\.\w{2,}(\.\w{2,})?/gi;

console.log("URLs encontradas:");
const urlMatches = paragraph.match(urlRegex);
console.log(urlMatches);

//Simulacion de foormulario de registro

function validateEmail(email) {
  const emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  const isValid = emailRegex.test(email);
  if (isValid) {
    console.log("Correo electrónico válido.");
    return true;
  } else {
    console.log("Correo electrónico no válido.");
    return false;
  }
}

function validateName(name) {
  const nameRegex = /^[a-zA-Z\s]{3,20}$/;
  const isValid = nameRegex.test(name);
  if (isValid) {
    console.log("Nombre válido.");
    return true;
  } else {
    console.log("Nombre no válido. Debe contener solo letras y espacios, y tener entre 3 y 20 caracteres.");
    return false;
  } 
}

function validatePhone(phone) {
  const phoneRegex = /^\d{3}[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}$/;
  const isValid = phoneRegex.test(phone); 
  if (isValid) {
    console.log("Número de teléfono válido.");  
    return true;
  } else {
    console.log("Número de teléfono no válido. Debe tener el formato 123-456-78-90 o 123 456 78 90."); 
    return false;
  }
}

function validatePassword(password) {
  const passwordRegex = /^(?=.*[A-Za-z])(?=.*[@$!%*#?&])(?=.*\d)[A-Za-z\d]{8,}$/;
  const isValid = passwordRegex.test(password); 
  if (isValid) {
    console.log("Contraseña válida.");  
    return true;
  } else {
    console.log("Contraseña no válida. Debe tener al menos 8 caracteres, incluyendo letras, números y al menos un carácter especial (@$!%*#?&)."); 
    return false;
  }
}

let formIsValid = false;

while (!formIsValid) {
  const name = question("Ingrese su nombre: ");
  let nameValid = validateName(name);
  const email = question("Ingrese su correo electrónica: ");
  let emailValid = validateEmail(email);
  const phone = question("Ingrese su número de teléfono: ");
  let phoneValid = validatePhone(phone);
  const password = question("Ingrese su contraseña: ");
  let passwordValid = validatePassword(password);
  if (nameValid && emailValid && phoneValid && passwordValid) {
    console.log("Formulario válido  .");
    formIsValid = true;
  } else {
    console.log("Hay campos inválidos.");
  }
}