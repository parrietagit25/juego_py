import pygame
import constantes
from elementos import Arbol
import random

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.characters = []
        self.arboles = [Arbol(random.randint(0, width), random.randint(0, height)) for _ in range(10)]
        
    def draw(self, screen):
        screen.fill(constantes.DARK_GRAY)
        for character in self.characters:
            character.draw(screen)
        for arbol in self.arboles:
            arbol.draw(screen)