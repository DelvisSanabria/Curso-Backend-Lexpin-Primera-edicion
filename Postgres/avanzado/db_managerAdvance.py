#pip install psycopg2-binary
import psycopg2


class DBManagerAdvance:
  #Constructor de la clase donde se definen los parametros de conexion
  def __init__(self, db_name='Lexpin_curso_backend', user='postgres', password='Supplydepot25.', host='localhost'):
    self.db_details = {
      'dbname': db_name,
      'user': user,
      'password': password,
      'host': host
    }
    
  #Metodo para abrir la conexion
  def _get_connection(self):
    try:
      return psycopg2.connect(**self.db_details) # type: ignore
    except psycopg2.OperationalError as e:
      print("Error al conectar a la base de datos:", e)
      return None
    
  #Crear las tablas y campos necesarios para la base de datos
  def setup_database(self):
    conn = self._get_connection()
    if conn is None:
      return
    
    with conn, conn.cursor() as cursor:
      try:
        cursor.execute('''
          CREATE TABLE IF NOT EXISTS categories (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(255) UNIQUE NOT NULL
          );
        ''')
        print("Tabla categories creada correctamente.")
        
        cursor.execute('''
          CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            precio NUMERIC(10,2) NOT NULL,
            stock INTEGER NOT NULL,
            id_category INTEGER REFERENCES categories(id),
            FOREIGN KEY (id_category) REFERENCES categories(id) ON DELETE SET NULL
          );
        ''')
        print("Tabla products creada correctamente.")
        
        #Insercion de datos iniciales en categories
        self.insert_sample_data(cursor)
      except psycopg2.Error as e:
        print("Error al crear la tabla:", e)
        
  def insert_sample_data(self, cursor):
    #vamos a insertar algunas categorias iniciales y datos de productos
    
    cursor.execute('SELECT COUNT(*) FROM categories')
    if cursor.fetchone()[0] == 0:
      print("No hay categorias en la base de datos, agregando datos iniciales...")
      categories = [('Electronica',), ('Ropa',), ('Hogar',), ('Alimentos',)]
    
      cursor.executemany('INSERT INTO categories (nombre) VALUES (%s)', categories)
      print("Categorias iniciales insertadas.")
    
    #Insercion de productos iniciales
    cursor.execute('SELECT COUNT(*) FROM products')
    if cursor.fetchone()[0] == 0:
      print("No hay productos en la base de datos, agregando datos iniciales...")
      products = [
        ('Laptop', 1200.00, 10, 1),
        ('Camiseta', 20.00, 50, 2),
        ('Sofá', 500.00, 5, 3),
        ('Manzanas', 2.00, 100, 4),
        ('Televisor', 800.00, 8, 1),
        ('Pantalones', 40.00, 30, 2),
        ('Mesa de comedor', 300.00, 3, 3),
        ('Pan', 1.50, 200, 4),
        ('Celular', 1000.00, 15, 1),
        ('Camisa', 25.00, 40, 2),
        ('Cama', 600.00, 4, 3),
        ('Pera', 3.00, 150, 4),
      ]
    
      cursor.executemany('INSERT INTO products (nombre, precio, stock, id_category) VALUES (%s, %s, %s, %s)', products)
      print("Productos iniciales insertados.")
    else:
      print("La base de datos ya contiene productos, no se insertaron datos iniciales.")
      
   #Metodo para ejecutar consultas personalizadas
  
  def execute_custom_query(self, query, params=()):
    with self._get_connection() as conn, conn.cursor() as cursor: # type: ignore
      try:
        print("Ejecutando consulta personalizada:", query)
        cursor.execute(query, params)
        if query.strip().upper().startswith("SELECT"):
          results = cursor.fetchall()
          return results
        else:
          rows_affected = cursor.rowcount
          print(f"Consulta ejecutada correctamente, filas afectadas: {rows_affected}")
          return rows_affected
      except psycopg2.Error as e:
        print("Error al ejecutar la consulta personalizada:", e)
        return None
      