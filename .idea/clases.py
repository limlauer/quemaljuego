#!/usr/bin/python3
import os
import optparse
from random import randint
from random import choice
from time import sleep
import json


class Personaje(object):
    def __init__(self, personaje):
        self.personaje = personaje

    def Opciones(self):
        print('[P]elear, [C]argar, [N]uevo personaje, [B]orrar, [S]alir')

    def ListarPersonajes(self):
        self.names = json.loads(open('personajes.json').read())['personajes']
        print(self.names)
        for name in self.names:
            print("+ {}".format(name["name"]))

    def C(self):
        print('Ingrese el personaje:')
        self.personaje = input()
        for name in self.names:
            if name["name"] == self.personaje:
                data = name
                self.vida = data["vida"]
                self.escudo = data["escudo"]
                self.mana = data["mana"]
                self.ataque = data["ataque"]
                self.defensa = data["defensa"]
                print(name)
        print("Cargado!")

    def P(self):
        print('Pelear')

    def B(self):
        print('Borrar')

    def N(self):
        print('Crear')

    def notAfun(self):
        print('No existe esa accion')

    def Acciones(self, accion):
        {'P': self.P,
         'C': self.C,
         'B': self.B,
         'N': self.N}.get(accion, self.notAfun)()