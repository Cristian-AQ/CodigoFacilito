import pygame,sys
from pygame.locals import *

color = pygame.Color(255,255,255)

pygame.init()

ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption('ANIMACION')

imagen = pygame.image.load('img/ball.png')
x,y=8,8
velocidad=100
der=True

while True:
    ventana.fill(color)
    ventana.blit(imagen,(x,y))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    if der==True:
        if(x<400):
            x+=velocidad
        else:
            der=False
            color=pygame.Color(255,0,0)
    else:
        if x>1:
            x-=velocidad
        else:
            der=True
            color=pygame.Color(0,255,0)
    pygame.display.update()