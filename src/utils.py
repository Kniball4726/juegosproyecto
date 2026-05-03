import os
"""Módulo de utilidades para el proyecto de juegos. Contiene funciones auxiliares que se utilizan en diferentes partes del proyecto, como la función para borrar la pantalla. Este módulo ayuda a mantener el código organizado y reutilizable. Funciones:
- borrarPantalla: Función para borrar la pantalla de la consola, compatible con sistemas oper
ativos Windows y Unix. Esta función se utiliza para limpiar la pantalla antes de mostrar nueva información al usuario, mejorando la experiencia de usuario y la legibilidad del programa.
Variables:
- None
"""
def borrarPantalla():
    """Función para borrar la pantalla de la consola, compatible con sistemas operativos Windows y Unix. Esta función se utiliza para limpiar la pantalla antes de mostrar nueva información al usuario, mejorando la experiencia de usuario y la legibilidad del programa.
Variables:- None
    
    """
    os.system('cls' if os.name == 'nt' else 'clear')
