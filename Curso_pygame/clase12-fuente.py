import pygame,sys
from pygame.locals import *

pygame.init()

ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption('FUENTES')

fuente1 = pygame.font.Font(None,30)#fuente por defaul
texto1 = fuente1.render('HOLA',0,(255,0,0))

fuente2 = pygame.font.SysFont('TIMES NEW ROMAN',30)#tomamos fuente del sistema
#mensaje,0,color
texto2 = fuente2.render('HOLA',0,(0,255,0))

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    ventana.blit(texto1,(100,100))
    ventana.blit(texto2,(0,0))
    pygame.display.update()