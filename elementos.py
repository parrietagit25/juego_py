import pygame
import constantes
import os


class Arbol:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wood = 5

        arbol_path = os.path.join("assets", "images", "object", "arbol.png")
        self.image = pygame.image.load(arbol_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (constantes.ARBOLES, constantes.ARBOLES))
        self.size = self.image.get_width()


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
