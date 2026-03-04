//async-await es una forma de manejar asincronismo en Javascript convierto funciones en promesas y manejo las respuestas con then y catch


//Ejemplo 1


let users = [
  { id: 1, name: "John", lastname: "Doe", gender: "male", age: 25, picture: "https://randomuser.me/api/portraits/men/1.jpg" },
  {id: 2, name: "Jane", lastname: "Doe", gender: "female", age: 30, picture: "https://randomuser.me/api/portraits/women/1.jpg" },
  {id: 3, name: "Bob", lastname: "Smith", gender: "male", age: 40, picture: "https://randomuser.me/api/portraits/men/2.jpg" },
  {id: 4, name: "Alice", lastname: "Johnson", gender: "female", age: 35, picture: "https://randomuser.me/api/portraits/women/2.jpg" },
  {id: 5, name: "Charlie", lastname: "Williams", gender: "male", age: 45, picture: "https://randomuser.me/api/portraits/men/3.jpg" },
  {id: 6, name: "Emily", lastname: "Brown", gender: "female", age: 50, picture: "https://randomuser.me/api/portraits/women/3.jpg" },
];


const getUsers = ()=>{
  let data = []
  return new Promise((resolve, reject)=>{
   if (users.length < 11) {
    setTimeout(() => {
      users.map((user)=>{
        let {name, lastname, gender, picture} = user;
        data.push({name: name, lastname: lastname, gender : gender, picture : picture});
      })
      resolve(data);
    },2500);
   } else {
    reject("No hay la cantidad de usuarios requerida");
   }
  })
}

//async nos ayuda a manejar asincronismo en Javascript
async function main(){
  //await nos dice que espere a que la promesa se resuelva
  const users = await getUsers();
  console.log("Usuarios obtenidos");
  console.log(users);
}

main();