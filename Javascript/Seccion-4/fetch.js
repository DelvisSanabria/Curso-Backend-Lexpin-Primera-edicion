//Fetch es una api de javascript para realizar peticiones HTTP y obtener informacion de un servidor

/* 

metodos
fetch(url, options): Realiza una peticion HTTP y devuelve una promesa que se resuelve con la respuesta del servidor.

then(): Se utiliza para manejar la respuesta de la peticion.

catch(): Se utiliza para manejar errores en la peticion.

finally(): Se utiliza para ejecutar codigo independiente de si la peticion fue exitosa o no.

*/

function getCharacters(){
  console.log('Iniciando la peticion a la API')

  const response = fetch('https://rickandmortyapi.com/api/character')

  //podemos ver que la promesa se encuentra pendiente
  console.log(response)

  response.then((result) => {
    return result.json()
  }).then((data) => {
    data.results.map((character) => {
      console.log('-----------------------')
      console.log('Personaje: ', character.name)
      console.log('Especie: ', character.species)
      console.log('Genero: ', character.gender)
      console.log('Estado: ', character.status)
      console.log('-----------------------')
      
  })
  }).catch((error) => {
    console.log(error)
  }).finally(() => {
    console.log('Finalizo la peticion')
  })
}

getCharacters()