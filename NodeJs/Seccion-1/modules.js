//Modulos nativos de NodeJS

//os: nos va a permitir obtener informacion del sistema operativo

import os from "node:os";


//Informacion del sistema operativo

console.log('Informacion del sistema operativo: ', os.userInfo());

console.log('Nuestro nombre es: ', os.hostname());

console.log('Nuestro sistema operativo es: ', os.platform());

console.log('Nuestra arquitectura es:', os.arch());

console.log('Nuestra version es: ', os.release());

console.log('Nuestra memoria total es: ', os.totalmem() /1024/1024/1024, 'GB');

console.log('Nuestra memoria libre es: ', os.freemem() /1024/1024/1024, 'GB');

console.log('nuestra cpu es' , os.cpus());


//fs: nos va a permitir interactuar con el sistema de archivos

import fs from "node:fs/promises";

async function checkFileStats() {
  try{
    const stats = await fs.stat("./historia.txt");
    console.log("El archivo existe:", stats.isFile());
    console.log("El archivo es un directorio:", stats.isDirectory());
    console.log("El archivo es un enlace simbolico:", stats.isSymbolicLink());

    //Puedo saber el tamaño del archivo
    console.log("El tamaño del archivo es:", stats.size); //Nos dice el tamano en bytes
  } catch (error) {
    console.error(error);
  }
}

checkFileStats();

Promise.all([
  fs.readFile("./historia.txt", "utf-8"), 
  fs.readFile("./historia2.txt", "utf-8")
]).then(([text1, text2]) => {
  console.log('El contenido del archivo es: ',text1);
  console.log('El contenido del archivo es: ',text2);
}).catch(error => {
  console.error(error);
});

//Escritura de archivos

//writeFile - nos permite escribir en un archivo

fs.writeFile("./nuevo_archivo.txt", "Que tal todo").then(() => {
  console.log("Archivo creado con exito");
}).catch(error => {
  console.error(error);
});

fs.writeFile('./historia2.txt', 'Esto fue sobre escrito').then(() => {
  console.log('Archivo modificado con exito');
}).catch(error => {
  console.error(error);
});


//appendFile - nos permite anexar contenido a un archivo

fs.appendFile('./historia2.txt', ' Esto fue anexado').then(() => {
  console.log('Archivo modificado con exito');
}).catch(error => {
  console.error(error);
});

//rm - nos permite eliminar un archivo

fs.rm('./nuevo_archivo.txt').then(() => {
  console.log('Archivo eliminado con exito');
}).catch(error => {
  console.error(error);
});

//Usamos los modulos que importamos

import sum from "./export.js";

console.log(sum(5, 3));