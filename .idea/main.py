import os
from random import randint
from random import choice
from time import sleep

personaje = {'nombre': '', 'edad': 0, 'vida': 0, 'escudo': 0, 'mana': 0, 'ataque': 0, 'defensa': 0}
enemigo = {'nombre': 'un pibe de dynamo', 'edad': 17, 'vida': 40, 'escudo': 10, 'mana': 0, 'ataque': 20, 'defensa': 30}
personajeTEMP = {'nombre': '', 'edad': 0, 'vida': 0, 'escudo': 0, 'mana': 0, 'ataque': 0, 'defensa': 0}
enemigoTEMP = {'nombre': 'un pibe de dynamo', 'edad': 17, 'vida': 40, 'escudo': 10, 'mana': 0, 'ataque': 20, 'defensa': 30}


def limpiar():
    print('\n' *100)

def guardar(vida, escudo, mana, ataque, defensa):
    guardado = 0
    while guardado == 0:
        guardar = input('Queres guardar este personaje? Es una mierda, te aviso (S/N): ')
        if guardar == 'S':
            print('Ahora decime...')
            nombre = input('Como mierda lo vas a llamar: ')
            edad = input('Y cuantos años va a tener: ')
            path = os.path.dirname(__file__) + '/personajes/{}'.format(nombre.lower())
            archivo = open(path, 'w+')
            archivo.write(str(nombre)+'\n'+str(edad)+'\n'+str(vida)+'\n'+str(escudo)+'\n'+str(mana)+'\n'+str(ataque)+'\n'+str(defensa))
            archivo.close()
            print('Listo pibe, guardado')
            guardado = 1
        elif guardar == 'N':
            print('Bueno no lo guardo entonces, bobo')

def cargar():
    global personaje
    cargado = 0
    while cargado == 0:
        limpiar()
        print('Estos son los personajes que tenes:')
        print(os.listdir(os.path.dirname(__file__) + '/personajes/'))
        cargar = input('Cual queres cargar? ')
        if cargar != '':
            print('Cargando...')
            path = os.path.dirname(__file__) + '/personajes/{}'.format(cargar)
            archivo = open(path, 'r')
            print('INFO DEL PERSONAJE')
            lineas = archivo.readlines()
            #Cargo el personaje original
            personaje['nombre'] = lineas[0].rstrip('\n')
            personaje['edad'] = lineas[1].rstrip('\n')
            personaje['vida'] = lineas[2].rstrip('\n')
            personaje['escudo'] = lineas[3].rstrip('\n')
            personaje['mana'] = lineas[4].rstrip('\n')
            personaje['ataque'] = lineas[5].rstrip('\n')
            personaje['defensa'] = lineas[6].rstrip('\n')
            #Cargo el temporal por si se modifica algo en la pelea
            personajeTEMP['nombre'] = lineas[0].rstrip('\n')
            personajeTEMP['edad'] = lineas[1].rstrip('\n')
            personajeTEMP['vida'] = lineas[2].rstrip('\n')
            personajeTEMP['escudo'] = lineas[3].rstrip('\n')
            personajeTEMP['mana'] = lineas[4].rstrip('\n')
            personajeTEMP['ataque'] = lineas[5].rstrip('\n')
            personajeTEMP['defensa'] = lineas[6].rstrip('\n')

            print('Nombre: ' + personaje['nombre'] + '\nEdad: ' + personaje['edad'] + '\nVida: ' + personaje['vida'] + '\nEscudo: ' + personaje['escudo'] + '\nMana: ' + personaje['mana'] + '\nAtaque: ' + personaje['ataque'] + '\nDefensa: ' + personaje['defensa'])
            archivo.close()
            print('Listo pibe, ya cargue tu personaje choto')
            cargado = 1
        else:
            print('... dale pelotudo en serio')

def cargarEnem():
    global enemigo
    cargado = 0
    while cargado == 0:
        limpiar()
        print('Estos son los enemigos que hay:')
        print(os.listdir(os.path.dirname(__file__) + '/enemigos/'))
        cargar = input('Cual enemigo queres cargar? ')
        if cargar != '':
            print('Cargando...')
            path = os.path.dirname(__file__) + '/enemigos/{}'.format(cargar)
            archivo = open(path, 'r')
            print('INFO DEL ENEMIGO')
            lineas = archivo.readlines()
            #Cargo el personaje original
            enemigo['nombre'] = lineas[0].rstrip('\n')
            enemigo['edad'] = lineas[1].rstrip('\n')
            enemigo['vida'] = lineas[2].rstrip('\n')
            enemigo['escudo'] = lineas[3].rstrip('\n')
            enemigo['mana'] = lineas[4].rstrip('\n')
            enemigo['ataque'] = lineas[5].rstrip('\n')
            enemigo['defensa'] = lineas[6].rstrip('\n')
            #Cargo el temporal por si se modifica algo en la pelea
            enemigoTEMP['nombre'] = lineas[0].rstrip('\n')
            enemigoTEMP['edad'] = lineas[1].rstrip('\n')
            enemigoTEMP['vida'] = lineas[2].rstrip('\n')
            enemigoTEMP['escudo'] = lineas[3].rstrip('\n')
            enemigoTEMP['mana'] = lineas[4].rstrip('\n')
            enemigoTEMP['ataque'] = lineas[5].rstrip('\n')
            enemigoTEMP['defensa'] = lineas[6].rstrip('\n')

            print('Nombre: ' + enemigo['nombre'] + '\nEdad: ' + enemigo['edad'] + '\nVida: ' + enemigo['vida'] + '\nEscudo: ' + enemigo['escudo'] + '\nMana: ' + enemigo['mana'] + '\nAtaque: ' + enemigo['ataque'] + '\nDefensa: ' + enemigo['defensa'])
            archivo.close()
            print('Listo pibe, ya cargue tu enemigo')
            cargado = 1
        else:
            print('... no pude cargar el enemigo bro')

def crear():
    global personaje
    personaje['nombre'] = ''
    personaje['edad'] = 0
    personaje['vida'] = 0
    personaje['escudo'] = 0
    personaje['mana'] = 0
    personaje['ataque'] = 0
    personaje['defensa'] = 0
    puntos = 20
    while puntos > 0:
        limpiar()
        aumentar = input('''Tenes que asignar puntos a tu personaje, tenes {} disponibles.
        Opciones: [V]ida {} - [E]scudo {} - [M]ana {} - [A]taque {} - [D]efensa {}
        Escribi una de las letras para aumentarlo: '''.format(puntos, personaje['vida'], personaje['escudo'], personaje['mana'], personaje['ataque'], personaje['defensa']))

        if aumentar not in "VEMAD" or len(aumentar) != 1:
            print('Que decis capo? Na que ve')
        elif aumentar == 'V':
            personaje['vida'] = int(personaje['vida']) + 10
            puntos -= 1
        elif aumentar == 'E':
            personaje['escudo'] = int(personaje['escudo']) + 10
            puntos -= 1
        elif aumentar == 'M':
            personaje['mana'] = int(personaje['mana']) + 10
            puntos -= 1
        elif aumentar == 'A':
            personaje['ataque'] = int(personaje['ataque']) + 10
            puntos -= 1
        elif aumentar == 'D':
            personaje['defensa'] = int(personaje['defensa']) + 10
            puntos -= 1

    limpiar()
    print('Ya terminaste de asignar los puntos, quedaron así:')
    vida = personaje['vida']
    escudo = personaje['escudo']
    mana = personaje['mana']
    ataque = personaje['ataque']
    defensa = personaje['defensa']
    print('[V]ida {} - [E]scudo {} - [M]ana {} - [A]taque {} - [D]efensa {}'.format(vida, escudo, mana, ataque, defensa))
    guardar(vida, escudo, mana, ataque, defensa)

def borrar():
    cancelar = 0
    while cancelar == 0:
        print('Estos son los personajes que tenes:')
        print(os.listdir(os.path.dirname(__file__) + '/personajes/'))
        borrar = input("Cual queres borrar? Sino pone C para cancelar: ")
        path = os.path.dirname(__file__) + '/personajes/{}'.format(borrar.lower())
        if borrar == "C":
            cancelar = 1
        else:
            if os.path.exists(path) == 1:
                seguro = input("Seguro? S/N: ")
                if seguro == "S":
                    os.remove(path)
                    cancelar = 1
                    print("Borrado pibe, de nada")
                else:
                    cancelar = 1
                    print("Bueno no lo borro entonces...")
            else:
                print(path)
                print('No existe ese personaje, capo')

def pelear():
    global personaje
    global personajeTEMP
    global enemigo
    global enemigoTEMP
    limpiar()
    print("ESTAS EN UNA PELEA BRODER")
    print("*************************")
    print('**Estas peleando con {}. Vida {} - Escudo {} - Mana {} - Ataque {} - Defensa {}'.format(enemigo['nombre'],
           enemigo['vida'],enemigo['escudo'],enemigo['mana'],enemigo['ataque'],enemigo['defensa']))
    print("*************************")
    print(str(enemigo['nombre']).upper() + ': listo para pelear hijo de puta?')
    print("")
    correr = 0
    while correr == 0:
        opcion = input('''Que mierda queres hacer?
        - [A]tacar
        - [C]urarte
        - [R]endirte
           ''')
        if opcion not in "ACR" or len(opcion) != 1:
            print('Imposible amigo')
        elif opcion == 'A':
            #CALCULO EL VALOR DE MI ATAQUE
            print('Calculando tu ataque...')
            sleep(1)
            ranAtaque = randint(0, 100)
            ranAtaquePer = randint(0, int(personajeTEMP['ataque']))
            AtaqueFinal = ranAtaquePer - ranAtaque
            if AtaqueFinal < 0: #Si es negativo lo hago 0, re triste
                AtaqueFinal = 0
            print('Tu intento de ataque es de: {}'.format(str(AtaqueFinal)))

            #CALCULO EL VALOR DE LA DEFENSA DEL ENEMIGO
            ranDefensa = randint(0,100)
            ranDefensaEne = randint(0, int(enemigoTEMP['defensa']))
            DefensaFinal = ranDefensaEne - ranDefensa
            if DefensaFinal < 0:
                DefensaFinal = 0
            print('La defensa del enemigo es de: {}'.format(str(DefensaFinal)))
            #CALCULO EL VALOR DEL ESCUDO DEL ENEMIGO
            ranEscudo = randint(0,100)
            ranEscudoEne = randint(0, int(enemigoTEMP['escudo']))
            EscudoFinal = (ranEscudoEne - ranEscudo) / 2
            if EscudoFinal < 0:
                EscudoFinal = 0
            print('El escudo del enemigo es de: {}'.format(str(EscudoFinal)))
            #CALCULO EL ATAQUE Y MODIFICO LOS VALORES
            ataqueTotal = AtaqueFinal - DefensaFinal - EscudoFinal
            if ataqueTotal < 0:
                ataqueTotal = 0
                print('No hiciste un carajo de daño. Tu ataque total fue de 0')
            enemigoTEMP['vida'] = int(enemigoTEMP['vida']) - int(ataqueTotal)
            #MUESTRO COMO QUEDO TODO HASTA AHORA
            print('Info de {}.\n Vida {} - Escudo {} - Mana {} - Ataque {} - Defensa {}'.format(
                enemigoTEMP['nombre'],
                enemigoTEMP['vida'], enemigoTEMP['escudo'], enemigoTEMP['mana'], enemigoTEMP['ataque'], enemigoTEMP['defensa']))
            print('Info de {}.\n Vida {} - Escudo {} - Mana {} - Ataque {} - Defensa {}'.format(
                personajeTEMP['nombre'],
                personajeTEMP['vida'], personajeTEMP['escudo'], personajeTEMP['mana'], personajeTEMP['ataque'],
                personajeTEMP['defensa']))

            #GANASTE? TERMINAR ESTO Y PROBARLO
            print('vida del chabon {}'.format(str(enemigoTEMP['vida'])))
            if int(enemigoTEMP['vida']) < 1:
                print('Le ganaste a {}, sos alto crack amigo'.format(enemigoTEMP['nombre']))
                correr = 1
            #HASTA ACA

        elif opcion == 'C':
            cargar()
        elif opcion == 'R':
            print(str(enemigo['nombre']) + " dice que sos un puto porque te cagaste de pelear. Nos vemos bobo")
            correr = 1

#MAIN
salir = 0
while salir == 0:
    print("")
    print("*****")
    opcion = input('''Que queres hacer con tu personaje?
    - [P]elear
    - [C]argar
    -  Cargar [E]nemigo
    - [N]uevo personaje
    - [B]orrar
    - [S]alir
       ''')

    if opcion not in "PCENBS" or len(opcion) != 1:
        print('Imposible amigo')
    elif opcion == 'E':
        cargarEnem()
    elif opcion == 'P':
        pelear()
    elif opcion == 'C':
        cargar()
    elif opcion == 'B':
        borrar()
    elif opcion == 'N':
        crear()
    elif opcion == 'S':
        print("No vemo gato")
        salir = 1