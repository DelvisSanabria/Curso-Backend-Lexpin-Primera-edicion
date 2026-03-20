import { Router } from "express";
import { usersController } from "../controllers/user.controller.js";
import { getUser } from "../controllers/user.controller.js";
import { createUser,updateUser,deleteUser,generateUsers } from "../controllers/user.controller.js";
import { login, isAuth } from "../middlewares/middleware.js";

const routerUser = Router();

//para crear las rutas, usamos el metodo .get() y le pasamos la ruta y el controlador
routerUser.get("", isAuth, usersController);
routerUser.get("/login", login);
routerUser.get("/get-user", getUser);
routerUser.post("", createUser)
routerUser.patch("/update/:id", updateUser)
routerUser.patch("/delete/:id", deleteUser)
routerUser.post("/generate", generateUsers);

export default routerUser;