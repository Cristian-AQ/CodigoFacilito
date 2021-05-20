import pygame,sys
from pygame.locals import *

color = (255,255,255)
aux = 1
pygame.init()

ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption('TIME')
fuente = pygame.font.SysFont('TIMES NEW ROMAN',30)

while True:
    ventana.fill(color)
    tiempo = pygame.time.get_ticks()/1000
    if aux==tiempo:
        aux+=1
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    contador = fuente.render(str(aux),0,(255,0,0))
    ventana.blit(contador,(100 ,100))
    pygame.display.update()