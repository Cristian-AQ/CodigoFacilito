import pygame,sys
from pygame.locals import *
from game import nave
from game import invasor as Enemigo

width=900
height=480
listaEnemigo=[]

def detenerTodo():
    for enemigo in listaEnemigo:
        for disparo in enemigo.listaDisparo:
            enemigo.listaDisparo.remove(disparo)
        
        enemigo.conquista = True

def cargarEnemigos():
    posx=100
    for x in range(1,5):
        enemigo = Enemigo.invasor(posx,100,40,'img/marcianoa.jpg','img/marcianob.jpg')
        listaEnemigo.append(enemigo)
        posx=posx+200
    posx=100
    for x in range(1,5):
        enemigo = Enemigo.invasor(posx,0,40,'img/marciano2a.jpg','img/marciano2b.jpg')
        listaEnemigo.append(enemigo)
        posx=posx+200
    posx=100
    for x in range(1,5):
        enemigo = Enemigo.invasor(posx,-100,40,'img/marciano3a.jpg','img/marciano3b.jpg')
        listaEnemigo.append(enemigo)
        posx=posx+200

def SpaceInvader():
    pygame.init()

    ventana = pygame.display.set_mode((width,height))
    pygame.display.set_caption('SPACE INVADER')
    fondo = pygame.image.load('img/fondo.jpg')
    
    #agregango sonido
    pygame.mixer.music.load('music/intro.mp3')
    pygame.mixer.music.play()

    fuente = pygame.font.SysFont('TIMES NEW ROMAN',30)
    texto = fuente.render('GAME OVER',0,(120,100,40))

    jugador = nave.naveEspacial(width,height)
    cargarEnemigos()
    #el parametro es para q el proyectil se dibuje en las cc de la nave
    #Demoproyectil = proyectil(width/2,height-30)
    enJuego = True
    reloj = pygame.time.Clock()

    while True:
        reloj.tick(60)#ayuda a regular cuantos frame se ejecutan cada segundo
        tiempo = int(pygame.time.get_ticks()/1000)#necesita ser entero
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

        if len(jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()
                if x.rect.top<-10:
                    jugador.listaDisparo.remove(x)
                else:#para eliminar enemigo
                    for enemigo in listaEnemigo:
                        if x.rect.colliderect(enemigo.rect):
                            listaEnemigo.remove(enemigo)
                            jugador.listaDisparo.remove(x)
        
        if len(listaEnemigo)>0:
            for enemigo in listaEnemigo:
                enemigo.comportamiento(tiempo)
                enemigo.dibujar(ventana)
                if enemigo.rect.colliderect(jugador.rect):
                    jugador.destruccion()
                    enJuego=False
                    detenerTodo()
                if len(enemigo.listaDisparo)>0:
                    for x in enemigo.listaDisparo:
                        x.dibujar(ventana)
                        x.trayectoria()
                        if x.rect.colliderect(jugador.rect):
                            jugador.destruccion()
                            enJuego=False
                            detenerTodo()
                        if x.rect.top>900:
                            enemigo.listaDisparo.remove(x)
                        else:
                            for disparo in jugador.listaDisparo:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.listaDisparo.remove(disparo)
                                    enemigo.listaDisparo.remove(x)
        if enJuego==False:
            pygame.mixer.music.load('music/over.mp3')
            ventana.blit(texto,(300,300))
        pygame.display.update()
SpaceInvader()