import pygame
import world
from pygame.locals import *
from world import *

class player():

    def __init__(self, x, y):
        img = pygame.image.load("./sprt/S02.png")
        self.rescale = pygame.transform.scale(img, (15, 15)) 
        self.rect = self.rescale.get_rect() 
        self.ancho = self.rescale.get_width() 
        self.alto = self.rescale.get_height() 
        self.rect.x = x 
        self.rect.y = y 
    
    def update(self, Screen, mundo, sprt): 
        
        dirX = 0
        dirY = 0

        ckey = pygame.key.get_pressed()

        if ckey [pygame.K_UP]: 
            dirY -= 1

        elif ckey [pygame.K_LEFT]: 
            dirX -= 1
        
        elif ckey [pygame.K_RIGHT]: 
            dirX += 1

        if ckey [pygame.K_DOWN]: 
            dirY += 1

        for i in mundo.listaTile:
            if i[1].colliderect(self.rect.x + dirX, self.rect.y, self.ancho, self.alto):
                dirX = 0

            if i[1].colliderect(self.rect.x, self.rect.y + dirY, self.ancho, self.alto):
                dirY = 0 

        self.rect.x += dirX
        self.rect.y += dirY
        
        Screen.blit(self.rescale, self.rect)
        return 
