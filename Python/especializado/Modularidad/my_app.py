from calculadora import sum_numbers, subtract_numbers

while True:
    print("Seleccione una operacion:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")

    choice = input("Ingrese su opcion (1/2/3): ")

    if choice == '3':
        print("Saliendo de la aplicacion.")
        break

    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))

    if choice == '1':
        result = sum_numbers(num1, num2)
        print(f"La suma de {num1} y {num2} es: {result}")
    elif choice == '2':
        result = subtract_numbers(num1, num2)
        print(f"La resta de {num1} y {num2} es: {result}")
    else:
        print("Opcion invalida. Por favor intente de nuevo.")
        
