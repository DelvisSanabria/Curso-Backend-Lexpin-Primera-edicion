from db_managerAdvance import DBManagerAdvance

def show_results(results, mensaje="Resultados de la consulta: "):
  if results is not None:
    print(mensaje)
    if results:
      for row in results:
        print(row)
    else:
      print("No se encontraron resultados.")
  else:
    print("No se pudieron obtener resultados. de la consulta: ", mensaje)
    

def main():
  db = DBManagerAdvance()
  
  #Necesitamos crear las tablas y datos iniciales
  db.setup_database()
  
  print("\n -- Inciando consultas avanzadas de Postgres SQL -- \n")
  
  #Consulta avanzada 1: Consultas con JOIN 
  
  #Join nos permite combinar datos de dos o mas tablas basandonos en una relacion entre ellas
  
  #Inner Join: Devuelve filas cuando hay una coincidencia en ambas tablas
  
  query_inner_join = '''
    SELECT p.nombre AS Producto, p.precio, c.nombre AS Categoria
    FROM products AS p
    INNER JOIN categories AS c ON p.id_category = c.id
  '''
  
  results_inner_join = db.execute_custom_query(query_inner_join)
  show_results(results_inner_join, "Resultados de Inner Join entre products y categories:")
  
  #Left Join: Devuelve todas las filas de la tabla izquierda y las filas coincidentes de la tabla derecha
  
  query_left_join = '''
    SELECT p.nombre AS Producto, p.precio, c.nombre AS Categoria
    FROM products AS p
    LEFT JOIN categories AS c ON p.id_category = c.id
  '''
  
  results_left_join = db.execute_custom_query(query_left_join)
  show_results(results_left_join, "Resultados de Left Join entre products y categories:")
  
  #Rigth Join nos devuelve todas las filas de la tabla derecha y las filas coincidentes de la tabla izquierda
  
  query_rigth_join = '''
    SELECT p.nombre AS Producto, c.nombre AS Categoria, c.id
    FROM products AS p
    RIGHT JOIN categories AS c ON p.id_category = c.id
  '''
  
  results_rigth_join = db.execute_custom_query(query_rigth_join)
  show_results(results_rigth_join, "Resultados de Rigth Join entre products y categories:")

 #Full outer Join: Devuelve filas cuando hay una coincidencia en una de las tablas, si no hay coincidencia, rellena con NULL
  
  query_full_outer_join = '''
    SELECT p.nombre AS Producto, c.nombre AS Categoria
    FROM products AS p
    FULL OUTER JOIN categories AS c ON p.id_category = c.id
  '''
  
  results_full_outer_join = db.execute_custom_query(query_full_outer_join)
  show_results(results_full_outer_join, "Resultados de Full Outer Join entre products y categories:")
  
  #Cross Join: Devuelve una combinacion cartesiana de ambas tablas, es decir, todas las combinaciones posibles entre las filas de ambas tablas.
  
  query_cross_join = '''
    SELECT p.nombre AS Producto, c.nombre AS Categoria
    FROM products AS p
    CROSS JOIN categories AS c
  '''
  
  results_cross_join = db.execute_custom_query(query_cross_join)
  show_results(results_cross_join, "Resultados de Cross Join entre products y categories:")
  
  #2 Ordenamiento y Agrupamiento avanzado 
  
  #ORDER BY multiple columns
  print("\n-- Ordenamiento por multiples columnas --\n")
  
  query_order_asc = '''
    SELECT nombre, precio, stock
    FROM products
    ORDER BY precio ASC, stock DESC
  '''
  
  results_order_asc = db.execute_custom_query(query_order_asc)
  show_results(results_order_asc, "Productos ordenados por precio ascendente y stock descendente:")
  
  query_order_desc = '''
    SELECT nombre, precio, stock
    FROM products
    ORDER BY precio DESC, stock ASC
  '''
  
  results_order_desc = db.execute_custom_query(query_order_desc)
  show_results(results_order_desc, "Productos ordenados por precio descendente y stock ascendente:")
  
  #Filtros con where
  print("\n-- Filtros avanzados con WHERE --\n")
  
  query_where = '''
    SELECT *
    FROM products
    WHERE precio > 100 AND stock > 10
  '''
  
  results_where = db.execute_custom_query(query_where)
  show_results(results_where, "Productos con precio mayor a 100 y stock mayor a 10:")
  
  query_where_and = '''
  SELECT p.nombre, p.stock, c.nombre
  FROM products AS p INNER JOIN categories AS c ON p.id_category = c.id
  WHERE c.nombre = %s AND p.stock < %s
  '''
  
  results_where_and = db.execute_custom_query(query_where_and, ('Electronica', 50))
  show_results(results_where_and, "Productos de la categoria Electronica con stock menor a 50:")
  
  query_where_in = '''
    SELECT p.nombre, c.nombre
    FROM products AS p INNER JOIN categories AS c ON p.id_category = c.id
    WHERE c.nombre IN %s
  '''
  results_where_in = db.execute_custom_query(query_where_in, (('Ropa', 'Hogar'),))
  show_results(results_where_in, "Productos en las categorias Ropa y Hogar:")
  
  query_where_is_null = '''
    SELECT p.nombre, c.nombre
    FROM products AS p LEFT JOIN categories AS c ON p.id_category = c.id
    WHERE p.id_category IS NULL
  '''
  results_where_is_null = db.execute_custom_query(query_where_is_null)
  show_results(results_where_is_null, "Productos sin categoria asignada (id_category es NULL):")
  
if __name__ == "__main__":
  main()