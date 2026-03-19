//Creamos la logica para el controlador de usuarios

export const usersController = (req, res) => {
  res.json({
    users: ["user1", "user2", "user3"],
  });
}

export const getUser = (req, res) => {
  res.json({
    user: {
      id: 1,
      name: "user1"
    }
  });
}

export const createUser = (req, res) => {
  //buscamos los valores que nos envian en el body
  const { name, email, password } = req.body;

  res.status(201).json({
    user: {
      name,
      email,
      password
    }
  });
}