import expresss from "express";
import router from "./routes/index.routes.js";
import routerUser from "./routes/user.routes.js";
import {login, isAuth} from "./middlewares/middleware.js";
import { connectDB } from "./config/database.js";
import cors from 'cors'

//definimos las reglas de cors

const corsOptions = {
  origin: ['http://localhost:3000'],
  optionsSuccessStatus: 200, // some legacy browsers (IE11, various SmartTVs) choke on 204,
  methods: ["GET","POST","PUT","PATCH","DELETE"],
  allowedHeaders: ["Content-Type", "Authorization"]
}

//Nos conectamos a la base de datos
connectDB();

//Creamos la app o punto de entrada

const app = expresss();


//configuraciones del servidor
const port = process.env.PORT;

//vamos a convertir a JSON

app.use(expresss.json());

//vamos a usar cors
app.use(cors(corsOptions));

//vamos a usar nuestras rutas

//podemos usar el middleware de forma especifica en una ruta
app.use("/", router);
app.use("/users", routerUser);

//hagamos que pase por el middleware de forma global
//app.use(middleware);

//iniciamos el servidor escuchando en el puerto 3000
app.listen(port, () => {
  console.log("Servidor escuchando en el puerto 3000");
  console.log(`http://localhost:${port}`);
});

/* 

#Proyecto de Sección 2: "API de Tareas (En Memoria)"

- Objetivo: Construir una API REST completa con la arquitectura MVC, manejando datos temporalmente en un array (sin base de datos aún).
- *Modelo (Temporal):* Un simple array en un archivo, ej: let tasks = [];
- *Rutas y Controladores:* Crear los 5 endpoints CRUD para Tareas:
    - GET /tasks: Devuelve todas las tareas.
    - GET /tasks/:id: Devuelve una sola tarea.
    - POST /tasks: Crea una nueva tarea (recibe title y description por el body).
    - PUT /tasks/:id: Actualiza una tarea.
    - DELETE /tasks/:id: Elimina una tarea.
- *Pruebas:* Usar Insomnia para probar que todos los endpoints funcionan.

*/