import pygame
import constantes
from elementos import Arbol
import random
import os

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.characters = []
        self.arboles = [Arbol(random.randint(0, width), 
                              random.randint(0, height)) for _ in range(10)]
        
        pasto_path = os.path.join("assets", "images", "object", "pasto.png")
        self.pasto = pygame.image.load(pasto_path).convert()
        self.pasto = pygame.transform.scale(self.pasto, 
                                            (constantes.PASTO, constantes.PASTO))
        
    def draw(self, screen):

        for x in range(0, self.width, constantes.PASTO):
            for y in range(0, self.height, constantes.PASTO):
                screen.blit(self.pasto, (x, y))

        for arbol in self.arboles:
            arbol.draw(screen)

        for character in getattr(self, "characters", []):
            character.draw(screen)