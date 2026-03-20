import { Router } from "express";
import { indexController } from "../controllers/index.controller.js";

const router = Router();

//para crear las rutas, usamos el metodo .get() y le pasamos la ruta y el controlador
router.get("", indexController);

export default router;