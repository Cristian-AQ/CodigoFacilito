import pygame, sys
from pygame.locals import *

color = (255,255,255)

pygame.init()

ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption('IMAGENES')

#la img no tiene q ser mas grande que la ventana
imagen = pygame.image.load('img/ball.png')
x,y=100,100

while True:
    ventana.fill(color)
    #parametros:ventana,posicion
    ventana.blit(imagen,(x,y))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()