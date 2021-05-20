import pygame

class proyectil(pygame.sprite.Sprite):
    def __init__(self,posx,posy,ruta,personaje):#ruta para saber kien dispara
        pygame.sprite.Sprite.__init__(self)
        self.imgProyectil = pygame.image.load(ruta)
        self.rect = self.imgProyectil.get_rect()
        self.velocidadDisparo = 5
        self.rect.top = posy
        self.rect.left = posx
        self.disparoPersonaje = personaje
    
    def trayectoria(self):
        if self.disparoPersonaje == True:
            self.rect.top = self.rect.top - self.velocidadDisparo
        else:
            self.rect.top = self.rect.top + self.velocidadDisparo
    
    def dibujar(self,superficie):
        superficie.blit(self.imgProyectil,self.rect)