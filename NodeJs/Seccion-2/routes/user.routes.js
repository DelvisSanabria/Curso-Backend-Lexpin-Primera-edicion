import { Router } from "express";
import { usersController } from "../controllers/user.controller.js";
import { getUser } from "../controllers/user.controller.js";
import { createUser } from "../controllers/user.controller.js";

const routerUser = Router();

//para crear las rutas, usamos el metodo .get() y le pasamos la ruta y el controlador
routerUser.get("", usersController);
routerUser.get("/get-user", getUser);
routerUser.post("", createUser)

export default routerUser;