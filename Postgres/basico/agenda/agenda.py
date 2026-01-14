from db_manager import DBManager


#Creamos el menu de nuestra agenda

def show_menu():
  print("\n--- Agenda de Contactos ---")
  print("1.Crear Tabla de contactos si no existe")
  print("2. Agregar nuevo contacto")
  print("3. agregar varios contactos")
  print("4. ver todos los contactos")
  print("5. Buscar contactos")
  print("6. Actualizar contacto")
  print("7. Eliminar contacto")
  print("0. Salir")
  print("--"*10)
  
  
  #Funcion principal para ejecutar el menu
  
def run_app():
  #Instanciamos el manejador de la base de datos
  db_manager = DBManager()
  
  while True:
    show_menu()
    choice = input("Seleccione una opcion: ")
    
    if choice == '1':
      db_manager.create_table()
      print("Tabla de contactos creada o ya existia.")
      
    elif choice == '2':
      nombre = input("Ingrese el nombre del contacto: ")
      email = input("Ingrese el email del contacto: ")
      telefono = input("Ingrese el telefono del contacto: ")
      db_manager.insert_contact(nombre, email, telefono)
      
    elif choice == '3':
      contacts_to_add = []
      print("Ingrese los contactos a agregar (deje el nombre vacio para terminar):")
      while True:
        nombre = input("Nombre: ")
        if not nombre:
          break
        email = input("Email: ")
        telefono = input("Telefono: ")
        contacts_to_add.append((nombre, email, telefono))
      if contacts_to_add:
        db_manager.insert_multiple_contacts(contacts_to_add)
      else:
        print("No se agregaron contactos.")
    elif choice == '4':
      contacts = db_manager.get_contacts()
      if contacts:
        print("\n--- Lista de Contactos ---")
        for contact in contacts:
          print(f"ID: {contact[0]}, Nombre: {contact[1]}, Email: {contact[2]}, Telefono: {contact[3]}")
      else:
        print("No hay contactos en la agenda.")
    elif choice == '5':
      column = input("Buscar por (nombre/email/telefono): ").strip().lower()
      search_term = input(f"Ingrese el termino de busqueda a buscar en la columna {column}: ")
      results = db_manager.search_contact(column, search_term)
      if results:
        print("\n--- Resultados de la Busqueda ---")
        for contact in results:
          print(f"ID: {contact[0]}, Nombre: {contact[1]}, Email: {contact[2]}, Telefono: {contact[3]}")
      else:
        print("No se encontraron contactos que coincidan con la busqueda.")
    elif choice == '6':
      contact_id = input("Ingrese el ID del contacto a actualizar: ")
      try:
        contact_id = int(contact_id)
        new_name = input("Nuevo nombre (deje vacio para no cambiar): ")
        new_email = input("Nuevo email (deje vacio para no cambiar): ")
        new_phone = input("Nuevo telefono (deje vacio para no cambiar): ")
        db_manager.update_contact(contact_id,
                                  new_name if new_name else None, 
                                  new_email if new_email else None, 
                                  new_phone if new_phone else None)
      except ValueError:
        print("ID invalido. Debe ser un numero entero.")
    elif choice == '7':
      contact_id = input("Ingrese el ID del contacto a eliminar: ")
      try:
        contact_id = int(contact_id)
        db_manager.delete_contact(contact_id)
      except ValueError:
        print("ID invalido. Debe ser un numero entero.")
    elif choice == '0':
      print("Saliendo de la agenda. ¡Hasta luego!")
      break
    else:
      print("Opcion no valida. Por favor intente de nuevo.")
      
if __name__ == "__main__":
  run_app()