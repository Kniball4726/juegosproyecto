import os
import sys
from pathlib import Path

if __package__ is None:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.ingreso import ingreso
from src.menu import menu
from src.juegos import caracruz, piedrapapeltijera, adivina_el_numero
from src.utils import borrarPantalla

# Para ver la documentación de una función, se imprime su docstring desde la lista de funciones.

os.system('cls' if os.name == 'nt' else 'clear')


def documentacion():
    funciones = [ingreso, menu, caracruz, piedrapapeltijera, adivina_el_numero, borrarPantalla]
    for funcion in funciones:
        print(funcion.__doc__)


if __name__ == "__main__":
    documentacion()


"""
    Este módulo se encarga de mostrar la documentación de las funciones principales del sistema de juegos. Contiene la función `documentacion()` que imprime la documentación de cada función en el sistema, incluyendo su descripción, variables utilizadas y cualquier otra información relevante. Esta función es útil para que los usuarios puedan entender cómo funcionan las diferentes partes del sistema y cómo interactuar con ellas.
    Funciones: ingreso, menu, caracruz, piedrapapeltijera, adivina_el_numero, borrarPantalla    
    Variables: None
    
"""