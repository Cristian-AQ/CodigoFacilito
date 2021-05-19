import pygame, sys
from pygame.locals import *

color1 = (105,205,255)
color2 = pygame.Color(0,100,150)

pygame.init()

ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption('COLORES')

while True:
    ventana.fill(color1)#rellena la ventana
    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
