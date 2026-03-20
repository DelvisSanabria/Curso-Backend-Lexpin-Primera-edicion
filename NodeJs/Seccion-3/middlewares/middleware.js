import jswebtoken from "jsonwebtoken";

export const generateToken = (user) => {
  return jswebtoken.sign({
    user: user
  },
  process.env.SECRET,
  {
    expiresIn: "2h"
  })
}

export const login = (req, res, next) => {
  const token = generateToken(req.user);
  res.json({
    token
  });
  next();
}

export const isAuth = (req, res, next) => {
  const authorization = req.headers.authorization;
  if(!authorization) return res.status(401).json({
    message: "No estas autorizado"
  })
  const token = authorization.slice(7, authorization.length);
  try {
    const user = jswebtoken.verify(token, process.env.SECRET);
    req.user = user.user;
    next();
  } catch (error) {
    res.status(401).json({
  })}
}