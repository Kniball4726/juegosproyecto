import os

usuario:str="Gregory"
contra:str="1234"
user:str=""
password:str=""
contador:int=0


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def iniciar_sesion():
    print("Iniciar sesión\n")
    
                


def menu():
    limpiar_pantalla()
    print("Bienvenido al sistema de Juegos desaarrollados en Python\n")
    print("1. Iniciar sesión\n2.- Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        limpiar_pantalla()
        iniciar_sesion()
    elif opcion == "2":
        print("Saliendo del sistema...")
    else:
        print("Opción no válida. Intente nuevamente.")
        menu()

menu()