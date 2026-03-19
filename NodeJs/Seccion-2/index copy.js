import expresss from "express";

//Creamos la app o punto de entrada

const app = expresss();

//configuraciones del servidor
const port = 3000;

//vamos a convertir a JSON

app.use(expresss.json());

//Creamos nuestras rutas

app.get("/", (req, res) => {
  res.send("Hola que tal muchachos");
});

app.get("/users", (req, res) => {
  res.json({
    users: ["user1", "user2", "user3"],
  });
})

//iniciamos el servidor escuchando en el puerto 3000
app.listen(port, () => {
  console.log("Servidor escuchando en el puerto 3000");
  console.log(`http://localhost:${port}`);
});