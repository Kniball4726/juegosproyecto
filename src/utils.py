import os


def borrarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
