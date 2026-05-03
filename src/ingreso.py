import sys
from .utils import borrarPantalla
from .juegos import juegospc

"""
    Este módulo se encarga de la función de ingreso al sistema, solicitando al usuario su nombre de usuario y contraseña para acceder a los juegos disponibles. Si el usuario ingresa las credenciales correctas, se le dará acceso a los juegos. Si el usuario ingresa una contraseña incorrecta tres veces, se le negará el acceso al sistema.
    Funciones:
    - ingreso: Función principal para gestionar el proceso de ingreso al sistema.
    Variables:
    - usuario: Nombre de usuario ingresado por el usuario.
    - contra: Contraseña ingresada por el usuario.
    - usuReal: Nombre de usuario real.
    - contraReal: Contraseña real.
    - contador: Número de intentos de inicio de sesión incorrectos. 
"""

def ingreso():
    """Función principal para gestionar el proceso de ingreso al sistema.
    Solicita al usuario su nombre de usuario y contraseña, y verifica si son correctos. Si el usuario ingresa las credenciales correctas, se le dará acceso a los juegos. Si el usuario ingresa una contraseña incorrecta tres veces, se le negará el acceso al sistema.
    
    Variables:
    - usuario: Nombre de usuario ingresado por el usuario.
    - contra: Contraseña ingresada por el usuario.
    - usuReal: Nombre de usuario real.
    - contraReal: Contraseña real.
    - contador: Número de intentos de inicio de sesión incorrectos. """
    usuario:str=""
    contra:str=""
    usuReal:str="Gregory"
    contraReal:str="1234"
    contador:int=0

    borrarPantalla()
    print("Bienvenido al sistema de juegos\n")
    print("Ingrese sus credenciales para acceder al sistema\n")

    while(usuReal!=usuario):
        usuario=input("Indique usuario:\n")
    
    while(contador<3 and contra!=contraReal):
        contra=input("Indique contraseña\n")
        contador+=1

    borrarPantalla()
    if(contador<3):
        juegospc(1)
    else:
        print("contraseña incorrecta")
        input("presione enter para salir")
        sys.exit()
        borrarPantalla()