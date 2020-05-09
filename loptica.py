import pygame
from random import randint
 
pozadinax = (0, 0, 0)

# Definiranje klase
class Loptica(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(pozadinax)
        self.image.set_colorkey(pozadinax)
        
        # Crtanje loptice 
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.velocity = [randint(6,10),randint(-12,12)]
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
          
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)
