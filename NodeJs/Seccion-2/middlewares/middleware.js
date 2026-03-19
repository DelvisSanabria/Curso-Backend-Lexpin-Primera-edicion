export const middleware = (req, res, next) => {
  console.log("Paso por el middleware")
  next()
}