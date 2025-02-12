import pygame
import constantes


class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.invetory = {"wood" : 0}
        
        
    def draw(self, screen):
        pygame.draw.rect(screen, constantes.BLUE, (self.x, self.y, self.size, self.size))
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.x = max(0, min(self.x, constantes.WIDTH - self.size))
        self.y = max(0, min(self.y, constantes.HEIGHT - self.size))