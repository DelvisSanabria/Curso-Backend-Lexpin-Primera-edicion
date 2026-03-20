//Creamos la logica para el controlador de usuarios

import mongoose from "mongoose";
import User from "../models/user.model.js";

export const usersController = async (req, res) => {
  try{
    const users = await User.find({isDeleted: false});
    res.status(200).json({
      users
    });
  }catch (error) {
    res.status(500).json({
      message: error.message
    })
  }
}

export const getUser = (req, res) => {
  res.json({
    user: {
      id: 1,
      name: "user1"
    }
  });
}

export const createUser = async (req, res) => {
  //buscamos los valores que nos envian en el body
  try {
    //creamos un nuevo usuario por medio del modelo
    const newUser = new User(req.body);
    //guardamos el nuevo usuario
    await newUser.save();
    //enviamos la respuesta
    res.status(201).json({
      user: newUser
    });
  }catch (error) {
    res.status(500).json({
      message: error.message
    });
  }
}

export const updateUser = async (req, res) => {
 try{
  //extraigo el ID de los parametros
  const user = new mongoose.Types.ObjectId(req.params.id);
  //creo una variable para buscar y actualizar el usuario
  const updateUser = await User.findOneAndUpdate(user, req.body, {
    new: true
  });

  if(!updateUser) return res.status(404).json({
    message: "Usuario no encontrado"
  })
  res.status(200).json({
    user: updateUser
  });
 }
 catch (error) {
  res.status(500).json({
    message: error.message
  });
 }
}

/* export const deleteUser = async (req, res) => {
  try {
    const user = new mongoose.Types.ObjectId(req.params.id);
    const deletedUser = await User.findOneAndDelete(user);
    if(!deletedUser) return res.status(404).json({
      message: "Usuario no encontrado"
    })
    res.status(200).json({
      user: deletedUser
    });
  } catch (error) {
    res.status(500).json({
      message: error.message
    });
  }
} */

export const deleteUser = async (req, res) => {
  try {
    const user = new mongoose.Types.ObjectId(req.params.id);
    const updateUser = await User.findOneAndUpdate(user, req.body, {
    new: true
  });

  if(!updateUser) return res.status(404).json({
    message: "Usuario no encontrado"
  })
  res.status(201).json({
    user: updateUser
  });
  } catch (error) {
    res.status(500).json({
      message: error.message
    });
  }
}

import {faker} from "@faker-js/faker";

export const generateUsers = async (req, res) => {
  try {
    const users = [];
    for (let i = 0; i < 100; i++) {
      const user = new User({
        name: faker.person.fullName(),
        email: faker.internet.email(),
        age: faker.number.int({min: 18, max: 100}),
      });
      users.push(user);
    }
    await User.insertMany(users);
    res.status(201).json({
      users
    });
  } catch (error) {
    res.status(500).json({
      message: error.message
    });
  }
}
