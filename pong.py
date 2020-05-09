import pygame
from reket import Reket
from loptica import Loptica
pygame.init()

# Određivanje potrebnih boja
lzelena = (120,255,135)
bijela = (255,255,255)
zuta = (255,255,0)
crvena = (255,0,0)
plava = (0,10,255)

# Otvaranje prozora 
size = (1400, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Igra Pong")
 
reket1 = Reket(crvena, 20, 200)
reket1.rect.x = 40
reket1.rect.y = 400
 
reket2 = Reket(plava, 20, 200)
reket2.rect.x = 1340
reket2.rect.y = 400
 
loptica = Loptica(zuta,30,30)
loptica.rect.x = 690
loptica.rect.y = 390
 

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(reket1)
all_sprites_list.add(reket2)
all_sprites_list.add(loptica)
 
carryOn = True
clock = pygame.time.Clock()
 
team1 = 0
team2 = 0
 
# Glavni dio programa
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              carryOn = False
              
    # Kontrola reketa
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        reket1.moveUp(5)
    if keys[pygame.K_s]:
        reket1.moveDown(5)
    if keys[pygame.K_UP]:
        reket2.moveUp(5)
    if keys[pygame.K_DOWN]:
        reket2.moveDown(5)    
 
    all_sprites_list.update()
    
    # Kretanje loptice
    if loptica.rect.x>=1380:
        team1+=1
        loptica.velocity[0] = -loptica.velocity[0]
    if loptica.rect.x<=0:
        team2+=1
        loptica.velocity[0] = -loptica.velocity[0]
    if loptica.rect.y>980:
        loptica.velocity[1] = -loptica.velocity[1]
    if loptica.rect.y<0:
        loptica.velocity[1] = -loptica.velocity[1]     
 
    if pygame.sprite.collide_mask(loptica, reket1) or pygame.sprite.collide_mask(loptica, reket2):
      loptica.bounce()
    
    # Određivanje pozadine, mreže i rezultata
    screen.fill(lzelena)
    pygame.draw.line(screen, bijela, [700, 0], [700, 1000], 15)
    
    all_sprites_list.draw(screen) 
 
    font = pygame.font.Font(None, 140)
    text = font.render(str(team1), 1, crvena)
    screen.blit(text, (500,20))
    text = font.render(str(team2), 1, plava)
    screen.blit(text, (840,20))
 
    pygame.display.flip()
    clock.tick(60) 

pygame.quit()
