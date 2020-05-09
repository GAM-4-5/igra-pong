import pygame
pozadinax = (0,0,0)

# Definiranje klase 
class Reket(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(pozadinax)
        self.image.set_colorkey(pozadinax)

        # Crtanje reketa
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        
    def moveUp(self, pixels):
        self.rect.y -= pixels
        # Uvjet da reket ne ide van okvira ekrana
        if self.rect.y < 0:
          self.rect.y = 0
          
    def moveDown(self, pixels):
        self.rect.y += pixels
        # Uvjet da reket ne ide van okvira ekrana
        if self.rect.y > 800:
          self.rect.y = 800
