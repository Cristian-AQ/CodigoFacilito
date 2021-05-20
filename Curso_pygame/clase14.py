import pygame,sys
from pygame.display import set_allow_screensaver
from pygame.locals import *
from random import randint

width=900
height=480

class naveEspacial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imgNave = pygame.image.load('img/nave.jpg')
        self.rect = self.imgNave.get_rect()#guardamos un rectangulo de la imagen
        self.rect.centerx = width/2
        self.rect.centery = height-30
        self.listaDisparo = []
        self.vida = True
        self.velocidad = 20
        self.sonidoDisparo = pygame.mixer.Sound('music/disparo.wav')
    
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
        miProyectil = proyectil(x,y,'img/disparoa.jpg',True)
        self.listaDisparo.append(miProyectil)
        self.sonidoDisparo.play()

    def  dibujar(self,superficie):
        superficie.blit(self.imgNave,self.rect)

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

class invasor(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.imgA = pygame.image.load('img/marcianoA.jpg')
        self.imgB = pygame.image.load('img/MarcianoB.jpg')
        self.listaImagenes = [self.imgA,self.imgB]
        self.posImagen = 0
        self.imagenInvasor = self.listaImagenes[self.posImagen]
        self.rect = self.imagenInvasor.get_rect()
        self.listaDisparo = []
        self.velocidad = 20
        self.rect.top = posy
        self.rect.left = posx

        self.rangoDisparo = 5
        self.tiempoCambio = 1#apoyo para recorrer las img

        #movimiento enemigo
        self.derecha = True
        self.contador = 0
        self.Maxdescenso = self.rect.top + 40

        self.sonidoDescenso = pygame.mixer.Sound('music/descenso.wav')

    def dibujar(self,superficie):
        self.imagenInvasor=self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenInvasor,self.rect)

    def comportamiento(self,tiempo):#el tiempo sera desde q se inicio el programa
        self.__movimientos()
        self.__ataque()
        if self.tiempoCambio == tiempo:
            self.posImagen+=1
            self.tiempoCambio+=1
            if self.posImagen > len(self.listaImagenes)-1:#necesario para evitar el desbordamiento y regresar
                self.posImagen=0
    
    def __ataque(self):
        if (randint(0,100)<self.rangoDisparo):
            self.__disparo()

    def __disparo(self):
        x,y = self.rect.center
        miProyectil = proyectil(x,y,'img/disparob.jpg',False)
        self.listaDisparo.append(miProyectil)
    
    def __movimientos(self):
        if self.contador < 3:
            self.__movimientoLateral()
        else:
            self.__descenso()
    
    def __descenso(self):
        if self.Maxdescenso == self.rect.top:
            self.contador = 0
            self.Maxdescenso = self.rect.top + 40
            self.sonidoDescenso.play()
        else:
            self.rect.top+=1

    def __movimientoLateral(self):
        if self.derecha == True:
            self.rect.left = self.rect.left + self.velocidad
            if self.rect.left > 800:
                self.derecha = False
                self.contador+=1
        else:
            self.rect.left=self.rect.left - self.velocidad
            if self.rect.left < 0:
                self.derecha=True

def SpaceInvader():
    pygame.init()

    ventana = pygame.display.set_mode((width,height))
    pygame.display.set_caption('INVADER')
    fondo = pygame.image.load('img/fondo.jpg')
    
    #agregango sonido
    pygame.mixer.music.load('music/intro.mp3')
    pygame.mixer.music.play()

    jugador = naveEspacial()
    enemigo = invasor(100,100)
    #el parametro es para q el proyectil se dibuje en las cc de la nave
    #Demoproyectil = proyectil(width/2,height-30)
    enJuego = True
    reloj = pygame.time.Clock()

    while True:
        reloj.tick(60)#ayuda a regular cuantos frame se ejecutan cada segundo
        tiempo = int(pygame.time.get_ticks()/1000)#necesita ser entero
        enemigo.comportamiento(tiempo)
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if enJuego == True:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == K_LEFT:
                        jugador.movIzquierda()
                    elif evento.key == K_RIGHT:
                        jugador.movDerecha()
                    elif evento.key == K_s:
                        x,y = jugador.rect.center
                        jugador.dispara(x,y)

        ventana.blit(fondo,(0,0))#img y posicion donde empieza a dibujar
        #Demoproyectil.dibujarProyectil(ventana)
        jugador.dibujar(ventana)
        enemigo.dibujar(ventana)

        if len(jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()
                if x.rect.top<-10:
                    jugador.listaDisparo.remove(x)
        
        if len(enemigo.listaDisparo)>0:
            for x in enemigo.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()
                if x.rect.top>900:
                    enemigo.listaDisparo.remove(x)
        pygame.display.update()
SpaceInvader()