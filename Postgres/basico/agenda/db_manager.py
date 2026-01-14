import psycopg2
from psycopg2 import sql


#Crear nuestra clase para manejar la base de datos

class DBManager:
  
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
    
  #Metodo para crear una tabla
  def create_table(self):
    conn = self._get_connection()
    if conn is None:
      return
    
    with conn, conn.cursor() as cursor:
      try:
        cursor.execute('''
          CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            telefono VARCHAR(25) UNIQUE NOT NULL
          )
        ''')
      except psycopg2.Error as e:
        print("Error al crear la tabla:", e)
        
  #Realizar metodos para nuestras operaciones CRUD (Create, Read, Update, Delete)
  
  #Metodos para crear un contacto
  
  def insert_contact(self, nombre, email, telefono):
    sql_query = 'INSERT INTO contacts (nombre, email, telefono) VALUES (%s, %s, %s)'
    
    with self._get_connection() as conn, conn.cursor() as cursor: # type: ignore
      try:
        cursor.execute(sql_query, (nombre, email, telefono))
        print("Contacto de nombre ", nombre, " insertado correctamente.")
        return True
      except psycopg2.IntegrityError as e:
        print("Error de integridad al insertar el contacto el correo o el telefono ya existen:", e)
        return False
      except psycopg2.Error as e:
        print("Error al insertar el contacto:", e)
        return False
      
  #Metodo para insertar varios contactos
  def insert_multiple_contacts(self, list_of_contacts):
    sql_query = 'INSERT INTO contacts (nombre, email, telefono) VALUES (%s, %s, %s)'
    
    with self._get_connection() as conn, conn.cursor() as cursor: # type: ignore
      try:
        cursor.executemany(sql_query, list_of_contacts)
        print(f"{cursor.rowcount} contactos insertados correctamente.")
        return True
      except psycopg2.IntegrityError as e:
        print("Error de integridad al insertar los contactos, alguno de los correos o telefonos ya existen:", e)
        return False
      except psycopg2.Error as e:
        print("Error al insertar los contactos:", e)
        return False
    
  #Metodos de lectura de contactos (Read)
  
  def get_contacts(self):
    with self._get_connection() as conn, conn.cursor() as cursor: # type: ignore
      try:
        cursor.execute('SELECT * FROM contacts ORDER BY id')
        return cursor.fetchall()
      except psycopg2.Error as e:
        print("Error al obtener los contactos:", e)
        return []
      
  def search_contact(self, columna, valor):
    if columna not in ['id', 'nombre', 'email', 'telefono']:
      print("Columna no valida para la busqueda.")
      return []
    
    query = sql.SQL("SELECT * FROM contacts WHERE {} LIKE %s").format(sql.Identifier(columna))
    
    with self._get_connection() as conn, conn.cursor() as cursor: # type: ignore
      try:
        cursor.execute(query, (f"%{valor}%",))
        return cursor.fetchall()
      except psycopg2.Error as e:
        print("Error al buscar el contacto:", e)
        return []
      
  #Metodo para actualizar un contacto (Update)
  def update_contact(self, contact_id, nombre=None, email=None, telefono=None):
    
    #Creamos una variable para establecer la Query
    
    query_parts = []
    values = []
    
    if nombre:
      query_parts.append(sql.SQL("nombre = %s"))
      values.append(nombre)
    if email:
      query_parts.append(sql.SQL("email = %s"))
      values.append(email)
    if telefono:
      query_parts.append(sql.SQL("telefono = %s"))
      values.append(telefono)
      
    if not query_parts:
      print("No hay campos para actualizar.")
      return False
    
    #le agregamos el id al final de los valores
    values.append(contact_id)
    
    #Construimos la consulta final
    
    query = sql.SQL("UPDATE contacts SET {} WHERE id = %s").format(sql.SQL(", ").join(query_parts))
    
    with self._get_connection() as conn, conn.cursor() as cursor: # type: ignore
      try:
        cursor.execute(query, tuple(values))
        if cursor.rowcount > 0:
          print("Contacto con id", contact_id, " actualizado correctamente.")
        return True
      except psycopg2.IntegrityError as e:
        print("Error de integridad al actualizar el contacto:", e)
        return False
      except psycopg2.Error as e:
        print("Error al actualizar el contacto:", e)
        return False
      
  #Metodo para eliminar un contacto (Delete)
  def delete_contact(self, contact_id):
    with self._get_connection() as conn, conn.cursor() as cursor: # type: ignore
      try:
        cursor.execute('DELETE FROM contacts WHERE id = %s', (contact_id,))
        if cursor.rowcount > 0:
          print("Contacto con id", contact_id, " eliminado correctamente.")
          return True
        else:
          print("No se encontro ningun contacto con id", contact_id)
          return False
      except psycopg2.Error as e:
        print("Error al eliminar el contacto:", e)
        return False
      
  #Metodo para ejecutar consultas personalizadas
  
  def execute_custom_query(self, query, params=()):
    with self._get_connection() as conn, conn.cursor() as cursor: # type: ignore
      try:
        print("Ejecutando consulta personalizada:", query)
        cursor.execute(query, params)
        if query.strip().upper().startswith("SELECT"):
          results = cursor.fetchall()
          print("Resultados obtenidos:", results)
          return results
        else:
          rows_affected = cursor.rowcount
          print(f"Consulta ejecutada correctamente, filas afectadas: {rows_affected}")
          return rows_affected
      except psycopg2.Error as e:
        print("Error al ejecutar la consulta personalizada:", e)
        return None