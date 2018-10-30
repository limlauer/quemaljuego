#!/usr/bin/python3
import os
import optparse
from random import randint
from random import choice
from time import sleep
import json

personaje = {'nombre': '', 'edad': 0, 'vida': 0, 'escudo': 0, 'mana': 0, 'ataque': 0, 'defensa': 0}
enemigo = {'nombre': '', 'edad': 0, 'vida': 0, 'escudo': 0, 'mana': 0, 'ataque': 0, 'defensa': 0}
personajeTEMP = {'nombre': '', 'edad': 0, 'vida': 0, 'escudo': 0, 'mana': 0, 'ataque': 0, 'defensa': 0}
enemigoTEMP = {'nombre': '', 'edad': 0, 'vida': 0, 'escudo': 0, 'mana': 0, 'ataque': 0, 'defensa': 0}


def limpiar():
    print('\n' *100)

def estado():
    print('''{:>18} | {:<}\n-> Vida       {:>3}  |  {:<3}\n-> Escudo     {:>3}  |  {:<3}\n-> Mana       {:>3}  |  {:<3}
-> Ataque     {:>3}  |  {:<3}
-> Defensa    {:>3}  |  {:<3}'''.format(enemigoTEMP['nombre'], personajeTEMP['nombre'], enemigoTEMP['vida'],
                                                    personajeTEMP['vida'], enemigoTEMP['escudo'], personajeTEMP['escudo'],
                                                    enemigoTEMP['mana'], personajeTEMP['mana'], enemigoTEMP['ataque'],
                                                    personajeTEMP['ataque'], enemigoTEMP['defensa'], personajeTEMP['defensa']))

def estadoPersonaje(diccionario):
    print('''{}, {} años.
    -> Vida       {:>3}/100
    -> Escudo     {:>3}/100
    -> Mana       {:>3}/100
    -> Ataque     {:>3}/100
    -> Defensa    {:>3}/100'''.format(diccionario['nombre'], diccionario['edad'], diccionario['vida'], diccionario['escudo'], diccionario['mana'],
                                      diccionario['ataque'], diccionario['defensa']))

def guardar(vida, escudo, mana, ataque, defensa):
    guardado = 0
    while guardado == 0:
        guardar = input('Queres guardar este personaje? Es una mierda, te aviso (S/N): ')
        if guardar == 'S':
            print('Ahora decime...')
            nombre = input('Como mierda lo vas a llamar: ')
            edad = input('Y cuantos años va a tener: ')
            #CARGAR LA DATA AL ARCHIVO
            NuevoPers = {'nombre': str(nombre), 'edad': str(edad), 'vida': str(vida), 'escudo': str(escudo), 'mana': str(mana), 'ataque': str(ataque), 'defensa': str(defensa)}
            NPersJSON = json.dumps({str(nombre).lower(): NuevoPers}, indent=4)
            # Cambiar esto por lo del os.path.dirname
            Path = os.path.dirname(__file__) + '/personajes.json'
            fh = open(Path, "a+")
            fh.write(NPersJSON)
            fh.close

            print('Listo pibe, guardado')
            guardado = 1
        elif guardar == 'N':
            print('Bueno no lo guardo entonces, bobo')

def cargar():
    global personaje
    global personajeTEMP
    Path = os.path.dirname(__file__) + '/personajes.json'
    PersJSON = json.loads(open(Path, "r").read())
    cargado = 0
    while cargado == 0:
        print('# CARGAR PERSONAJE')
        print('Estos son los personajes que tenes:')
        for c in PersJSON:
            personaje = PersJSON.get(c)
            print("c: " + str(c))
            print(personaje["nombre"])
        cargar = input('Cual queres cargar? ')
        if cargar != '':
            print('Cargando...')
            personaje = PersJSON.get(str(cargar))
            personajeTEMP = PersJSON.get(str(cargar))
            print(type(personaje))
            print('INFO DEL PERSONAJE')
            estadoPersonaje(personajeTEMP)
            print('Listo pibe, ya cargue tu personaje choto')
            cargado = 1
        else:
            print('... dale pelotudo en serio')

def cargarEnem():
    global enemigo
    global enemigoTEMP
    Path = os.path.dirname(__file__) + '/enemigos.json'
    PersJSON = json.loads(open(Path, "r").read())
    cargado = 0
    while cargado == 0:
        print('# CARGAR ENEMIGO')
        print('Estos son los enemigos que tenes:')
        for c in PersJSON:
            enemigo = PersJSON.get(c)
            print("c: " + str(c))
            print(enemigo["nombre"])
        cargar = input('Cual queres cargar? ')
        if cargar != '':
            print('Cargando...')
            enemigo = PersJSON.get(str(cargar))
            enemigoTEMP = PersJSON.get(str(cargar))
            print(type(enemigo))
            print('INFO DEL ENEMIGO')
            estadoPersonaje(enemigoTEMP)
            print('Listo pibe, ya cargue tu enemigo')
            cargado = 1
        else:
            print('... dale pelotudo en serio')

def crear():
    global personaje
    personaje = {'nombre': '', 'edad': 0, 'vida': 0, 'escudo': 0, 'mana': 0, 'ataque': 0, 'defensa': 0}
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

#Ni puta idea de como hacer esto BRO
def borrar():
    global personaje
    global personajeTEMP
    Path = os.path.dirname(__file__) + '/personajes.json'
    PersJSON = json.loads(open(Path, "r").read())
    cargado = 0
    while cargado == 0:
        print('# BORRAR PERSONAJE')
        print('Estos son los personajes que tenes:')
        for c in PersJSON:
            personaje = PersJSON.get(c)
            print("c: " + str(c))
            print(personaje["nombre"])
        cargar = input('Cual queres borrar? ')
        for c in PersJSON:
            personaje = PersJSON.get(c)
            if personaje["nombre"] == cargar:
                personaje.pop[c]

        #BORRAR DEL ARREGLO EL PERSONAJE BRODER

            print('Listo')
        else:
            print('... dale pelotudo en serio')

'''
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
'''

def curarse():
    manaActual = int(personajeTEMP['mana'])
    vidaActual = int(personajeTEMP['vida'])
    if manaActual > 0:
        print('Aplican2 esas vendas para curarte 10 de vida...')
        sleep(1)
        manaActual -= 10
        vidaActual += 10
        personajeTEMP['mana'] = manaActual
        personajeTEMP['vida'] = vidaActual
        # MUESTRO COMO QUEDO TODO HASTA AHORA
        estado()
    else:
        print('Mana insuficiente maestro que mierda te pensas no es gratis esto')

def DifRandom(max1, max2):
    sleep(1)
    ranAtaque = randint(0, max1)
    ranAtaquePer = randint(0, max2)
    AtaqueFinal = ranAtaquePer - ranAtaque
    if AtaqueFinal < 0:  # Si es negativo lo hago 0, re triste
        AtaqueFinal = 0
    return AtaqueFinal

def atacar():
    # CALCULO EL VALOR DE MI ATAQUE
    ataqueMio = DifRandom(80, int(personajeTEMP['ataque']))
    print('Tu intento de ataque es de: {}'.format(str(ataqueMio)))

    # CALCULO EL VALOR DE LA DEFENSA DEL ENEMIGO
    defensaEnem = DifRandom(90, int(enemigoTEMP['defensa']))
    print('Defensa del enemigo: {}'.format(str(defensaEnem)))

    # CALCULO EL VALOR DEL ESCUDO DEL ENEMIGO
    escudoEnem = int(DifRandom(100, int(enemigoTEMP['escudo']))) /2
    print('Escudo del enemigo: {}'.format(str(escudoEnem)))

    # CALCULO EL ATAQUE Y MODIFICO LOS VALORES
    ataqueTotal = ataqueMio - defensaEnem - escudoEnem
    if ataqueTotal < 0:
        ataqueTotal = 0
        print('No hiciste un carajo de daño. Tu ataque total fue de 0')
    enemigoTEMP['vida'] = int(enemigoTEMP['vida']) - int(ataqueTotal)

    # MUESTRO COMO QUEDO TODO HASTA AHORA
    estado()

    # GANASTE? TERMINAR ESTO Y PROBARLO
    if int(enemigoTEMP['vida']) < 1:
        print('Le ganaste a {}, sos alto crack amigo'.format(enemigoTEMP['nombre']))
        return 1
    else:
        return 0

def magia():
    manaActual = int(personajeTEMP['mana'])
    if manaActual > 0:
        # CALCULO EL VALOR DE MI ATAQUE CON MAGIA
        ataqueMio = DifRandom(80, int(personajeTEMP['ataque'])) * 1.25
        print('Tu intento de ataque es de: {}'.format(str(ataqueMio)))
        if ataqueMio < 0:  # Si es negativo lo hago 0, re triste
            ataqueMio = 0

        # CALCULO EL VALOR DE LA DEFENSA DEL ENEMIGO
        defensaEnem = DifRandom(90, int(enemigoTEMP['defensa']))
        print('Defensa del enemigo: {}'.format(str(defensaEnem)))

        # CALCULO EL ATAQUE Y MODIFICO LOS VALORES
        ataqueTotal = ataqueMio - defensaEnem
        if ataqueTotal < 0:
            ataqueTotal = 0
            print('No hiciste un carajo de daño. Tu ataque total fue de 0, y gastaste 10 de mana al pedo.')
        enemigoTEMP['vida'] = int(enemigoTEMP['vida']) - int(ataqueTotal)
        manaActual -= 10
        personajeTEMP['mana'] = manaActual
        # MUESTRO COMO QUEDO TODO HASTA AHORA
        estado()

        if int(enemigoTEMP['vida']) < 1:
            print('Le ganaste a {}, sos alto crack amigo'.format(enemigoTEMP['nombre']))
            return 1
        else:
            return 0
    else:
        print("# No tenes mana bro")

def pelear():
    global personaje
    global personajeTEMP
    global enemigo
    global enemigoTEMP
    limpiar()
    print("# ESTAS EN UNA PELEA BRODER")
    print('# Peleando con {}. Vida {} - Escudo {} - Mana {} - Ataque {} - Defensa {}'.format(enemigo['nombre'],
           enemigo['vida'],enemigo['escudo'],enemigo['mana'],enemigo['ataque'],enemigo['defensa']))
    print(str(enemigo['nombre']).upper() + ': listo para pelear hijo de puta?')
    correr = 0
    while correr == 0:
        opcion = input('''# Que mierda queres hacer?
        - [A]tacar
        - [M]agia
        - [C]urarte
        - [R]endirte
        ''')
        if opcion not in "ACMR" or len(opcion) != 1:
            print('Imposible amigo')
        elif opcion == 'A':
            if atacar() == 1:
                correr = 1
            else:
                correr = 0
        elif opcion == 'C':
            curarse()
        elif opcion == 'M':
            if magia() == 1:
                correr = 1
            else:
                correr = 0
        elif opcion == 'R':
            print(str(enemigo['nombre']) + " dice que sos un puto porque te cagaste de pelear. Nos vemos bobo")
            correr = 1

#MAIN
#Hice un diccionario con las opciones, y ahora? xdxDdxDxD
#Opciones = {'P': pelear(), 'C': cargar(), 'E': cargarEnem(), 'B': borrar(), 'N': crear(), 'S': exit()}
salir = 0
while salir == 0:
    print('\nQue queres hacer con tu personaje?','- [P]elear', '- [C]argar', '-  Cargar [E]nemigo', '- [N]uevo personaje', '- [B]orrar', '- [S]alir')
    opcion = input()
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