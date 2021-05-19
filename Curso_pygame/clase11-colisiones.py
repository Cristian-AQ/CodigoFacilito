import pygame,sys
from pygame.locals import *

color = pygame.Color(255,255,255)

pygame.init()

ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption('COLISIONES')

rectangulo1 = pygame.Rect(0,0,100,50)
rectangulo2 = pygame.Rect(0,100,100,50)
x,y=8,100
velocidad=10
der=True


while True:
    ventana.fill(color)
    pygame.draw.rect(ventana,(255,0,0),rectangulo1)
    pygame.draw.rect(ventana,(0,255,0),rectangulo2)
    #left=pos en x; top=pos en y
    rectangulo1.left,rectangulo1.top=pygame.mouse.get_pos()#hacemos q el rect se mueva 
    if rectangulo1.colliderect(rectangulo2):#para la colision
        velocidad = 0
    else:
        velocidad=10
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    if der==True:
        if x<390:
            x+=velocidad
            rectangulo2.left=x
        else:
            der=False
    else:
        if x>1:
            x-=velocidad
            rectangulo2.left=x
        else:
            der=True
    pygame.display.update()