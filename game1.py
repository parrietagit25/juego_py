import pygame
import sys
import constantes
from character import Character
from world import World


# iniciamos el juego 
pygame.init()

# Configuramos la pantalla

width = 800
height = 600

ventana = pygame.display.set_mode((constantes.WIDTH, constantes.HEIGHT))
pygame.display.set_caption("Simulador")

def main():
    clock = pygame.time.Clock()
    world = World(constantes.WIDTH, constantes.HEIGHT)
    character = Character(constantes.WIDTH // 2, constantes.HEIGHT // 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character.move(-1, 0)
        if keys[pygame.K_RIGHT]:
            character.move(1, 0)
        if keys[pygame.K_UP]:
            character.move(0, -1)
        if keys[pygame.K_DOWN]:
            character.move(0, 1)
            
        world.characters = [character]
        world.draw(ventana)
        pygame.display.flip()
        clock.tick(60)
        
        
if __name__ == "__main__":
    main()