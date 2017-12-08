import pygame
from pongSettings import *
import random

class Slider(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((slideWidth,slideHeight))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.left = posx
        self.rect.top = posy
        self.score = 0

    def setScore(self,newscore):
    	self.score += newscore

    def getScore(self):
        return str(self.score)

class Ball(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((ballWidth,ballHeight))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.left = posx
        self.rect.top = posy
        pygame.draw.circle(self.image, white,(10,10),10)
        self.moveBall()

    def moveBall(self):
        #selects a random x,y choice for initial direction
        self.xdirection = random.choice(["left","right"])
        self.ydirection = random.choice(["up","down"])

		
    def changeDirection(self):
        if self.xdirection == "left":
            self.xdirection = "right"

        elif self.xdirection == "right":
            self.xdirection = "left"


    def update(self):
        if self.xdirection == "left":
            self.rect.x -= ballSpeed

        elif self.xdirection == "right":
            self.rect.x += ballSpeed

        if self.ydirection == "up":
            self.rect.y -= ballSpeed

        elif self.ydirection == "down":
            self.rect.y += ballSpeed

        #bouncy physics - HIGHLY experimental (and HIGHLY bouncy)
        if self.rect.top <= 0:
            self.ydirection = "down"

        elif self.rect.bottom >= 500:
            self.ydirection = "up"

        #check if score
        #if (self.rect.left <= -60) or (self.rect.right >= 660):
            #self.reset()

    def checkScore(self):
        if (self.rect.left <= -60):
            self.reset()
            return 0,1
            
        elif (self.rect.right >= 660):
            self.reset()
            return 1,0
        
        else:
            return 0,0

    def reset(self):
        self.rect.x = 280
        self.rect.y = 230
        self.moveBall()