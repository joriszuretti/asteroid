import pygame
import random
pygame.init()

import core

from classes.Joueur import Joueur
from classes.Asteroid import Asteroid


def setup():
    print('SetUp :')
    core.WINDOW_SIZE=[1200,720]
    core.fps=60

    core.memory("asteroid",[])
    core.memory("joueur", [])

    core.memory("nbasteroid", 10)
    core.memory("nbjoueur", 1)

    for i in range(0,core.memory("nbasteroid")):
        core.memory("asteroid").append(Asteroid())

    for i in range(0,core.memory("nbjoueur")):
        core.memory("joueur").append(Joueur())



def run():
    core.cleanScreen()

    #CONTROL
    if core.getKeyPressList("q"):
        pygame.quit()
    if core.getKeyPressList("r"):
        core.memory("asteroid", [])
        for i in range(0, core.memory("nbasteroid")):
            core.memory("asteroid").append(Asteroid())

    #AFFICHAGE
    for p in core.memory("asteroid"):
        p.afficher()
    for p in core.memory("joueur"):
        p.afficher()


    #MISE A JOUR DES POSITIONS
    for p in core.memory("asteroid"):
        p.deplacement()
        p.bordure(core.WINDOW_SIZE)
        '''
    for p in core.memory("joueur"):
        p.deplacement()
        p.bordure(core.WINDOW_SIZE)
        '''
core.main(setup,run)