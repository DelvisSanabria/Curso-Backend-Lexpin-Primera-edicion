function sum (num1, num2) {
  return num1 + num2;
}

export default sum

//exportar con COMMONJS
//module.exports = {sum};


/* Proyecto de Sección 1: "Lector de Archivos"

- Objetivo: Familiarizarse con los módulos nativos `fs` y el manejo asíncrono.
- Tarea: Crear una aplicación de consola (sin servidor) que:
    1. Use el módulo `fs/promises` (la versión moderna de `fs`).
    2. Lea el contenido del archivo `package.json`.
    3. Imprima en consola el contenido del archivo.
    4. Bonus: Escriba un nuevo archivo llamado `info.txt` que contenga la información de tu sistema operativo (usando el módulo `os`). */