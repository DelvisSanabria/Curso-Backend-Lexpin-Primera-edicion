import psycopg2

#se crea la instancia de conexion

conn = psycopg2.connect(
  dbname="Lexpin_curso_backend",
  user ="postgres",
  password="Supplydepot25.",
  host="localhost",
)

#tenemos un cursor para ejecutar las consultas

cursor = conn.cursor()

#creamos la consulta sql

client_id = 1
cursor.execute("SELECT * FROM clients WHERE id_client = %s", (client_id,))

#mostramos los resultados si los hay

if cursor.rowcount > 0:
    client = cursor.fetchone()
    print("Encontramos el cliente:", client)

#cuando haga consultar de (Update, Delete, Insert) se debe hacer commit

#conn.commit()


#traernos todos los productos

#seleccionamos todos los productos
cursor.execute("SELECT * FROM products")

#traemos todos los productos
products = cursor.fetchall()

for product in products:
    print(product)

#es buena costumbre cerrar la conexion

conn.close()