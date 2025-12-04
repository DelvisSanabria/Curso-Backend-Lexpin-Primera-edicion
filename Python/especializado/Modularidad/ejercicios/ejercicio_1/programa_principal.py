import operaciones as op

try:
  print("Bienvenido a la Caja de Herramientas Matemáticas")
  print("="*40)
  print(op.sum())
  print(op.subtract())
  print(op.square())
except ValueError:
  print("Error: Por favor ingrese un numero valido.")
finally:
  print("Gracias por usar la Caja de Herramientas Matemáticas.")