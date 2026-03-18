//Modulos nativos de NodeJS

//Htpp: permite crear servidores web basicos

//podemos importar con CommonJs 

//const http = require("http")

//ES module
import http from "http";

const server = http.createServer((req, res) =>{
  //Establecemos el status code
  res.statusCode = 200

  //Establecemos el tipo de contenido que tendra la respuesta
  res.setHeader('Content-Type', 'text/html')

  res.end('<h1>hola que tal chicos!</h1>')
})

server.listen(3000, ()=>{
  console.log('Servidor escuchando en el puerto 3000')
  console.log('http://localhost:3000')
})