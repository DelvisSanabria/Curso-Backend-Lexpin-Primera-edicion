import { Schema, model } from "mongoose";

const userSchema = new Schema({
  //aqui listamos cada una de las propiedades que debe tener un usuario
  name: {
    type: String,
    required: true,
    trim: true
  },
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true
  },
  age:{
    type: Number,
    min: 18,
    max: 100
  },
  isDeleted: {
    type: Boolean,
    default: false
  },
  createdAt:{
    type: Date,
    default: Date.now
  }
})

const User = model("User", userSchema);

export default User