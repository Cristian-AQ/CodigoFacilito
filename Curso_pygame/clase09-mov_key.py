import pygame,sys
from pygame.locals import *

color = (255,255,255)

pygame.init()

ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption('MOVIMIENTO')
imagen = pygame.image.load('img/ball.png')
x,y=8,8
velocidad=5

while True:
    ventana.fill(color)
    ventana.blit(imagen,(x,y))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:#verifica si se presiono una tecla
            if evento.key == K_LEFT:
                x-=velocidad
            elif evento.key == K_RIGHT:
                x+=velocidad
        #elif evento.type == pygame.KEYUP:#verifica si se solto la tecla
    pygame.display.update()