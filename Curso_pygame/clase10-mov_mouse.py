import pygame,sys
from pygame.locals import *

color = (255,255,255)
pygame.init()

ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption('MOUSE')

imagen = pygame.image.load('img/ball.png')
x,y=8,8
velocidad=10

while True:
    ventana.fill(color)
    ventana.blit(imagen,(x,y))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == KEYDOWN:
            if evento.key == K_LEFT:
                x-=velocidad
            elif evento.key == K_RIGHT:
                x+=velocidad
    x,y=pygame.mouse.get_pos()#mover la imagen con el mouse
    pygame.display.update()