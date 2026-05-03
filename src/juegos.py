import random
from .utils import borrarPantalla
from .menu import menu

"""
    Este módulo se encarga de la función de los juegos disponibles en el sistema. Contiene las funciones para cada juego, así como la función principal para gestionar la selección de juegos por parte del usuario.
    Funciones:
    - juegospc: Función principal para gestionar la selección de juegos por parte del usuario.
    - caracruz: Función para el juego de cara o cruz.
    - piedrapapeltijera: Función para el juego de piedra, papel, tijera.
    - adivina_el_numero: Función para el juego de adivina el número.
    Variables:
    - lista: Lista para almacenar los nombres de los jugadores.
    - correcto: Número de veces que el usuario acierta en el juego de cara o cruz.
    - incorrecto: Número de veces que el usuario falla en el juego de cara o cruz.
    - ganaste: Número de veces que el usuario gana en el juego de piedra, papel, tijera.
    - perdiste: Número de veces que el usuario pierde en el juego de piedra, papel, tijera.
    - contador: Número de rondas jugadas.
    - numeroCompu: Número generado por la computadora en el juego de adivina el número.
    - numeroUsuario: Número ingresado por el usuario en el juego de adivina el número.
    - intentos: Número de intentos realizados por el usuario en el juego de adivina el número."""

def juegospc(op:int):
    """Función principal para gestionar la selección de juegos por parte del usuario. Recibe como parámetro la opción seleccionada por el usuario en el menú, y ejecuta la función correspondiente al juego seleccionado.
    
    Variables:
    - op: Opción seleccionada por el usuario en el menú. 
    - lista: Lista para almacenar los nombres de los jugadores.
    - correcto: Número de veces que el usuario acierta en el juego de cara o cruz.
    - incorrecto: Número de veces que el usuario falla en el juego de cara o cruz.
    - ganaste: Número de veces que el usuario gana en el juego de piedra, papel, tijera.
    - perdiste: Número de veces que el usuario pierde en el juego de piedra, papel, tijera.
    - contador: Número de rondas jugadas.
    - numeroCompu: Número generado por la computadora en el juego de adivina el número.
    - numeroUsuario: Número ingresado por el usuario en el juego de adivina el número.
    - intentos: Número de intentos realizados por el usuario en el juego de adivina el número.
    """
    
    while op != 4:
        op = menu()
        borrarPantalla()
        print("Bienvenido, ha seleccionado la opción " + str(op) + "\n")

        match op:
            case 1:
                caracruz()
            case 2:
                piedrapapeltijera()
            case 3:
                adivina_el_numero()
            case 4:
                print("Saliendo ...\n")
            case _:
                print("\nIndique una opción correcta del menú\n")
                input("presione enter para continuar")
                borrarPantalla()
                menu()




def caracruz():
    """Función para el juego de cara o cruz. El usuario debe elegir entre cara (0) o cruz (1), y la computadora generará aleatoriamente su elección. El juego se juega en tres rondas, y el usuario gana si acierta al menos dos veces contra la computadora.   
    Variables:
    - lista: Lista para almacenar los nombres de los jugadores.
    - contador: Número de rondas jugadas.
    - correcto: Número de veces que el usuario acierta en el juego de cara o cruz.
    - incorrecto: Número de veces que el usuario falla en el juego de cara o cruz.
    
    """
    
    lista=[]
    contador=0      
    correcto=0
    incorrecto=0
    while(contador<3):
        eleccionComputadora=random.randint(0, 1)
        eleccionUsuario=int(input("0.- cara , 1.- cruz: "))
        print("Salio "+ str(eleccionComputadora))
        if(eleccionComputadora==eleccionUsuario):
            print("Correcto")
            correcto+=1
            contador+=1
        else:
            print("incorrecto ")
            incorrecto+=1
            contador+=1
    if contador >= 2 and correcto > incorrecto:
        print("Ganaste contra la maquina\n")
        lista.append(input("Indique su nombre para el ranking\n"))
        print("Ranking de jugadores\n")
        for i in lista:
            print(i)
        input("presione enter para continuar")
        borrarPantalla()

        menu()
    else:
        print("Perdiste contra la maquina\n")
        lista.append(input("Indique su nombre para el ranking\n"))
        print("Ranking de jugadores\n")
        for i in lista:
            print(i)
        input("presione enter para continuar")
        borrarPantalla()
        menu()
    

def piedrapapeltijera():
    """Función para el juego de piedra, papel, tijera. El usuario debe elegir entre piedra (0), papel (1) o tijera (2), y la computadora generará aleatoriamente su elección. El juego se juega en tres rondas, y el usuario gana si gana al menos dos veces contra la computadora.
    Variables:
    - lista: Lista para almacenar los nombres de los jugadores.
    - ganaste: Número de veces que el usuario gana en el juego de piedra, papel, tijera.
    - perdiste: Número de veces que el usuario pierde en el juego de piedra, papel, tijera.
    - contador: Número de rondas jugadas.
    
    """
    lista=[]
    ganaste=0
    perdiste=0
    contador=0
    
    while contador<3:
        pc=random.randint(0,2)
        usuario=int(input("\n0.-pieda, 1.- papel, 2.-tijera\n"))
        print("La maquina eligio: "+str(pc))
        if(pc==usuario):
            input("Quedaron en empate\n")
            contador+=1
        elif(usuario==0 and pc==2):
            input("Ganaste contra la maquina\n")
            ganaste+=1
            contador+=1
        elif(usuario==1 and pc==0):
            input("Ganaste contra la maquina\n")
            ganaste+=1
            contador+=1
        elif(usuario==2 and pc==1):
            input("Ganaste contra la maquina\n  ")
            ganaste+=1 
            contador+=1
        elif(usuario==0 and pc==1):
            input("Perdiste contra la maquina\n")
            perdiste+=1
            contador+=1
        elif(usuario==1 and pc==2):
            input("Perdiste contra la maquina\n")
            perdiste+=1
            contador+=1    
        elif(usuario==2 and pc==0):
            input("Perdiste contra la maquina")
            perdiste+=1
            contador+=1
        else:
            print("Indique una opción correcta del menú\n")
            input("presione enter para continuar")
            borrarPantalla()
            menu()
    if ganaste > perdiste:
        input("Ganaste contra la maquina con ventaja de " + str(ganaste) + " a " + str(perdiste))
        lista.append(input("Indique su nombre para el ranking\n"))
        print("Ranking de jugadores\n")
        for i in lista:
            print(i)
        borrarPantalla()
        menu()
    elif perdiste > ganaste:
        input("Perdiste contra la maquina con desventaja de " + str(perdiste) + " a " + str(ganaste))
        lista.append(input("Indique su nombre para el ranking\n"))
        print("Ranking de jugadores\n")
        for i in lista:
            print(i)
        borrarPantalla()
        menu()
    else:
        input("Quedaron en empate con " + str(ganaste) + " a " + str(perdiste))
        borrarPantalla()
        menu()
            
            

def adivina_el_numero():
    """Función para el juego de adivina el número. La computadora generará aleatoriamente un número entre 1 y 10, y el usuario debe adivinarlo. El usuario tiene tres intentos para adivinar el número, y la computadora le dará pistas si el número ingresado es mayor o menor que el número generado. El usuario gana si adivina el número dentro de los tres intentos.
    Variables:
    - lista: Lista para almacenar los nombres de los jugadores.
    - intentos: Número de intentos realizados por el usuario.
    - numeroCompu: Número generado aleatoriamente por la computadora.

    - numeroUsuario: Número ingresado por el usuario.
    
    """

    lista=[]
    intentos=0
    numeroCompu=random.randint(1,10)
    
    while(intentos<3):
        numeroUsuario=int(input("Adivina el número del 1 al 10\n"))
        if(numeroUsuario!=numeroCompu):
            if(numeroUsuario>numeroCompu):
                print("Es más pequeño\n")
                intentos+=1
            else:
                print("Es más grande\n")
                intentos+=1
        else:
            print("GANASTE! Adivinaste el número!\n")
            lista.append(input("Indique su nombre para el ranking\n"))
            print("Ranking de jugadores\n")
            for i in lista:
                print(i)
            input("presione enter para continuar")
            borrarPantalla()
            menu()
    print("\nPerdiste, el número era " + str(numeroCompu))
    lista.append(input("Indique su nombre para el ranking\n"))
    print("Ranking de jugadores\n")
    for i in lista:
        print(i)
    input("\npresione enter para continuar")
    borrarPantalla()
    menu()


