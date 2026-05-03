import sys
from .utils import borrarPantalla
from .juegos import juegospc



def ingreso():
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