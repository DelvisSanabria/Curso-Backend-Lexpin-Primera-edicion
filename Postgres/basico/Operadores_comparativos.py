#Los operadores comparativos en PostgreSQL se utilizan para comparar dos valores y devolver un resultado booleano (verdadero o falso) basado en la comparación.

#Son usados con frecuencia en cláusulas WHERE para filtrar registros en consultas SQL.

from agenda.db_manager import DBManager

db_manager = DBManager()

#1. Igual a (=)

#Selecciona registros donde el valor de una columna es igual a un valor específico.

results_equal = db_manager.execute_custom_query("SELECT * FROM contacts WHERE nombre = %s", ('Delvis',))

#2. Diferente de (<> o !=)

#Selecciona registros donde el valor de una columna no es igual a un valor específico.

results_not_equal = db_manager.execute_custom_query("SELECT * FROM contacts WHERE nombre != %s", ('Delvis',))

#3. Mayor que (>)

#Selecciona registros donde el valor de una columna es mayor que un valor específico.

results_greater_than = db_manager.execute_custom_query("SELECT * FROM contacts WHERE id > %s", (3,))

#4. Mayor o igual que (>=)

#Selecciona registros donde el valor de una columna es mayor o igual que un valor específico.

results_greater_than_or_equal = db_manager.execute_custom_query("SELECT * FROM contacts WHERE id >= %s", (3,))

#5. Menor que (<)

#Selecciona registros donde el valor de una columna es menor que un valor específico.

results_less_than = db_manager.execute_custom_query("SELECT * FROM contacts WHERE id < %s", (3,))

#6. Menor o igual que (<=)

#Selecciona registros donde el valor de una columna es menor o igual que un valor específico.

results_less_than_or_equal = db_manager.execute_custom_query("SELECT * FROM contacts WHERE id <= %s", (3,))

#7. Like (%)

#Selecciona registros donde el valor de una columna coincide con un patrón específico.

#El símbolo % representa cero o más caracteres.

#El simbolo _ representa un solo carácter.

results_like = db_manager.execute_custom_query("SELECT * FROM contacts WHERE nombre LIKE %s", ('%lv%',))

results_like = db_manager.execute_custom_query("SELECT * FROM contacts WHERE nombre LIKE '______'")