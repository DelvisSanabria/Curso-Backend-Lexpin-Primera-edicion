#Los operadores logicos en PostgreSQL se utilizan para combinar múltiples condiciones lógicas y devolver un resultado booleano (verdadero o falso) basado en la evaluación de esas condiciones.

#1. AND (Y)

#El operador AND devuelve verdadero si ambas condiciones son verdaderas.

from agenda.db_manager import DBManager

db_manager = DBManager()

results_and = db_manager.execute_custom_query("SELECT * FROM contacts WHERE nombre = %s AND email = %s", ('Delvis', 'delvis@gmail.com'))


#2. OR (O)

#El operador OR devuelve verdadero si al menos una de las condiciones es verdadera.

results_or = db_manager.execute_custom_query("SELECT * FROM contacts WHERE nombre = %s OR email = %s", ('Delvis', 'delvis9@gmail.com'))

#3. NOT (NO)

#El operador NOT devuelve verdadero si la condición es falsa. Se utiliza para negar una condición.

results_not = db_manager.execute_custom_query("SELECT * FROM contacts WHERE NOT nombre = %s", ('Delvis',))