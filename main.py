import pygame
from pygame.locals import *
import world
from world import *
import player
from player import *

#=========================================================#
#           Variables y constantes globales               #
#=========================================================#

minX = 0 ; maxX = 800 ; xd = 0 ; mouX = 0 
minY = 0 ; maxY = 380 ; yd = 0 ; mouY = 0 

menu = True ; ciclo = True
res = (400, 380)

#=========================================================#
#                  Funcion "Load_Image'                   #
#        Carga imagenes y convierte formato PyGame.       #
#=========================================================#

def Load_Image(sFile,transp = False):
    try: image = pygame.image.load(sFile)
    except pygame.error.message:
        raise SystemExit.message
    image = image.convert()  
    if transp:
        color = image.get_at((0,0))
        image.set_colorkey(color)
    return image

#=========================================================#
#                    Array de sprites                     #
#=========================================================#

def arraySprt():
    aSprt = []
    aSprt.append(Load_Image('./sprt/S00.png',False )) # Background [0]
    aSprt.append(Load_Image('./sprt/S01.png',False )) # Tile Azul  [1]
    return aSprt

#=========================================================#
#                 Inicializa PyGames                      #
#=========================================================#

def pygame_init():
    pygame.init()
    pygame.display.set_caption('Laberinto - MrRevillod')
    pygame.mouse.set_visible(False)
    return pygame.display.set_mode(res)

#=========================================================#
#                    Funcion MapInit                      #
#=========================================================#

def MapInit(maxX,maxY):
    return pygame.Surface(maxX,maxY)

#=========================================================#
#               Funciones Multifuncionales.               #
#=========================================================#

def Background():
    return Screen.blit(sprt[0],(xd,yd))

#===========================================================#
#                  La mitica funcion pausa.                 #
#                    La de toda la vida.                    #
#===========================================================#

def Pausa():
    while 1:
        e = pygame.event.wait()
        if e.type in (pygame.QUIT, pygame.KEYDOWN):
            return

#===========================================================#
#                     Ciclo Principal                       #
#===========================================================#

Screen = pygame_init()
sprt = arraySprt()
mundo1 = world(nivel1,sprt)
jugador = player(20,22)
ckey = pygame.key.get_pressed()

while ciclo: 

    if ckey[pygame.K_q]: 
        ciclo = False
    
    ev = pygame.event.get() 
    for e in ev:
        if e.type == pygame.QUIT:
            ciclo = False
        if e.type == pygame.MOUSEMOTION : mouX,mouY = e.pos

    Background()
    mundo1.draw(Screen)
    jugador.update(Screen, mundo1, sprt)

    pygame.time.delay(5)
    pygame.display.flip()

pygame.quit
