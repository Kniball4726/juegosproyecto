import random
from .utils import borrarPantalla
from .menu import menu


def juegospc(op:int):
    
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
        input("Ganaste contra la maquina")
        borrarPantalla()
    else:
        input("Perdiste contra la maquina")
        borrarPantalla()

def piedrapapeltijera():
    ganaste=0
    perdiste=0
    
    contador=0
    
    while contador<3:
        pc=random.randint(0,2)
        usuario=int(input("\n0.-pieda, 1.- papel, 2.-tijera\n"))
        print("La maquina eligio: "+str(pc))
        
        if(pc==usuario):
            print("Quedaron en empate\n")
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
        borrarPantalla()
        menu()
    elif perdiste > ganaste:
        input("Perdiste contra la maquina con desventaja de " + str(perdiste) + " a " + str(ganaste))
        borrarPantalla()
        menu()
    else:
        input("Quedaron en empate con " + str(ganaste) + " a " + str(perdiste))
        borrarPantalla()
        menu()
            
            

def adivina_el_numero():
    numeroCompu=random.randint(1,10)
    intentos=0
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
            input("presione enter para continuar")
            borrarPantalla()
            menu()
    print("\nPerdiste, el número era " + str(numeroCompu))
    input("\npresione enter para continuar")
    borrarPantalla()
    menu()


