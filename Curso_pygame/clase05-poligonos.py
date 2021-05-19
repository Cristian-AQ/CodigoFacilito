import pygame,sys
from pygame.locals import *

color1 = (0,255,0)
pygame.init()

ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption('POLIGONOS')

#lugar,color,centro,radio,0=relleno,1=sin relleno; pdt si pones >1 aumenta grosor y parecera que se rellena
pygame.draw.circle(ventana,color1,(200,100),20,1)
pygame.draw.rect(ventana,color1,(10,20,110,120),1)
pygame.draw.polygon(ventana,color1,((200,0),(300,100),(100,100)),1)

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()