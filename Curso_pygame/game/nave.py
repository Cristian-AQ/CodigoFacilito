import pygame
from game import proyectil

class naveEspacial(pygame.sprite.Sprite):
    def __init__(self,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.imgNave = pygame.image.load('img/nave.jpg')
        self.imgExplosion = pygame.image.load('img/explosion.jpg')
        self.rect = self.imgNave.get_rect()#guardamos un rectangulo de la imagen
        self.rect.centerx = width/2
        self.rect.centery = height-30
        self.listaDisparo = []
        self.vida = True
        self.velocidad = 20
        self.sonidoDisparo = pygame.mixer.Sound('music/disparo.wav')
        self.sonidoExplosion = pygame.mixer.Sound('music/explosion.wav')
    
    def movDerecha(self):
        self.rect.right+=self.velocidad
        self.__movimiento()

    def movIzquierda(self):
        self.rect.left-=self.velocidad
        self.__movimiento()
    
    def __movimiento(self):#metodo privado
        if self.vida==True:
            if self.rect.left<=0:
                self.rect.left=0
            elif self.rect.right>870:
                self.rect.right=840
    
    def dispara(self,x,y):
        miProyectil = proyectil.proyectil(x,y,'img/disparoa.jpg',True)
        self.listaDisparo.append(miProyectil)
        self.sonidoDisparo.play()

    def destruccion(self):
        self.sonidoExplosion.play()
        self.vida=False
        self.velocidad=0
        self.imgNave=self.imgExplosion

    def  dibujar(self,superficie):
        superficie.blit(self.imgNave,self.rect)
    