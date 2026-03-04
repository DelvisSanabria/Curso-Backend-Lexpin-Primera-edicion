//Axios es una libreria de javascript que nos permite hacer peticiones HTTP de manera sencilla y eficiente

/* 

Las propiedades que retorna axios son:
config: La configuración de la solicitud.
data: Los datos de la respuesta.
headers: Los encabezados de la respuesta.
status: El estado de la respuesta.
statusText: El texto del estado de la respuesta.


Los metodos de axios son:
axios.get(url): Realiza una solicitud GET a la URL especificada.
axios.post(url, data): Realiza una solicitud POST a la URL especificada con los datos proporcionados.
axios.put(url, data): Realiza una solicitud PUT a la URL especificada con los datos proporcionados.
axios.delete(url): Realiza una solicitud DELETE a la URL especificada.
*/

import axios from "axios";

//Realizando una peticion GET
axios
  .get("https://rickandmortyapi.com/api/character")
  .then((response) => {
    response.data.results.map((character) => {
      console.log('-----------------------')
      console.log('Personaje: ', character.name)
      console.log('Especie: ', character.species)
      console.log('Genero: ', character.gender)
      console.log('Estado: ', character.status)
      console.log('-----------------------')
    })
  })
  .catch((error) => {
    console.log(error)
  });