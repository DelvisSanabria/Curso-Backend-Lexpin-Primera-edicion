import mongoose from "mongoose";

//creamos la URL de nuestra base de datos
const dbUrl = `${process.env.DB_URL}`;


//establecemos una nueva conexion

export const connectDB = async () => {
  try {
    await mongoose.connect(dbUrl);
    console.log("Conectado a la base de datos");
  } catch (error) {
    console.error(error);
    //salimos del proceso
    process.exit(1);
  }
};