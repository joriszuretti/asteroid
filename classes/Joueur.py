import random
import pygame
from pygame.math import Vector2
pygame.init()
import core

window = pygame.display.set_mode((1200, 720))

class Joueur:
    def __init__(self, w=1200, h=720):
        self.position = Vector2(random.randint(0,w), h-20)
        self.longeur = 100
        self.hauteur = 10
        self.vitesse = 10
        self.acceleration = Vector2(0, 0)
        self.couleur = (255,255,255)

        self.maxVitesse = 50
        self.maxAcceleration = 50

        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and w > 0:
            w -= self.vitesse
        if keys[pygame.K_RIGHT] and w < 1200 - self.longeur:
            w += self.vitesse
        window.fill((0, 0, 0))
        pygame.draw.rect(window, (255, 0, 0), (w, h, self.longeur, self.hauteur))
        pygame.display.update()


    def afficher(self):
        core.Draw.rect(self.couleur, (self.position.x, self.position.y, self.longeur, self.hauteur))

    def bordure(self,fenetre):
        if self.position.y < 0:
            self.position.y = fenetre[1]

        if self.position.y > fenetre[1]:
            self.position.y = 0

        if self.position.x < 0:
            self.position.x = fenetre[0]

        if self.position.x > fenetre[0]:
            self.position.x = 0