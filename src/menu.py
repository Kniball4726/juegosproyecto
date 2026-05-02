usuario:str="Gregory"
contra:str="1234"
user:str=""
contra:str=""

def iniciar_sesion():
    user = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    if user == usuario and password == contra:
        print("Inicio de sesión exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")
        menu()


def menu():
    print("Bienvenido al sistema de inicio de sesión")
    print("1. Iniciar sesión")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        iniciar_sesion()
    elif opcion == "2":
        print("Saliendo del sistema...")
    else:
        print("Opción no válida. Intente nuevamente.")
        menu()

