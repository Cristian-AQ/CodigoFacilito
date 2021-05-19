import pygame,sys
from pygame.locals import *

color1 = (255,255,255)
color2 = (0,255,0)

pygame.init()

ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption('LINEAS')

while True:
    ventana.fill(color1)
    #lugar,color,origen,fin,grosor(opcional)
    pygame.draw.line(ventana,color2,(100,100),(200,200),4)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()