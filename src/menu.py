"""Módulo de menú para el sistema de juegos. Este módulo contiene la función `menu()` que muestra el menú de opciones al usuario y solicita su selección. El menú incluye las siguientes opciones:
1. Cara o cruz  
2. Piedra, papel, tijera
3. Adivina el número
4. Salir
El usuario debe ingresar el número correspondiente a la opción que desea seleccionar, y la función `menu()` devolverá ese número para que el programa pueda ejecutar la función correspondiente al juego seleccionado. Si el usuario ingresa un número que no corresponde a ninguna opción del menú, se le solicitará que ingrese una opción válida.
Funciones:
- menu: Función para mostrar el menú de opciones al usuario y solicitar su selección.
Variables:
- op: Variable para almacenar la opción seleccionada por el usuario. 

"""
def menu():
    """Función para mostrar el menú de opciones al usuario y solicitar su selección. El menú incluye las siguientes opciones:
1. Cara o cruz
2. Piedra, papel, tijera
3. Adivina el número
4. Salir
El usuario debe ingresar el número correspondiente a la opción que desea seleccionar, y la función `menu()` devolverá ese número para que el programa pueda ejecutar la función correspondiente al juego seleccionado. Si el usuario ingresa un número que no corresponde a ninguna opción del menú, se le solicitará que ingrese una opción válida.        
Variables:
- op: Variable para almacenar la opción seleccionada por el usuario. 
    """
    print("\nBienvenido al sistema de juegos\n")
    print("Menú de juegos\n")
    print("1.-cara o cruz")
    print("2.-piedra, papel, tijera")
    print("3.-adivina numero")
    print("4.-salir\n")
    return int(input("Seleccione una opción:\n"))

