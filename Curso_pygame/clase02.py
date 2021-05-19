import pygame, sys
from pygame.locals import *

pygame.init()

ventana = pygame.display.set_mode((400,300))#tamaño ventana
pygame.display.set_caption('MI VENTANA')#nombre ventana

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()#cierra ventana
    pygame.display.update()#actualiza la ventana