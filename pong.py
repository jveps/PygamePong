#A Pong clone made in Pygame.

import sys
import pygame
from pygame.locals import *
from pongSettings import *
from sprites import *
import random
import time

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width,height))
        self.running = True

    def startScreen(self):
        self.screen.fill(black)
        self.toText("My Pygame Pong Game",white,50,30,100)
        self.toText("Press any key to start",white,20,200,350)
        pygame.display.flip()
        self.keyWait()

    def toText(self,message,color,fontSize,x,y):
    	self.font = pygame.font.SysFont("Arial",fontSize)
    	self.fontObj = self.font.render(message,1,color)
    	self.screen.blit(self.fontObj,(x,y))

    def keyWait(self):
    	wait = True
    	while wait:
    		for event in pygame.event.get():
    			if event.type == QUIT:
    				wait = False
    				self.running = False
    				pygame.quit()
    				sys.exit()

    			elif event.type == KEYUP:
    				wait = False

    def new(self):
        self.topRect = pygame.Rect(0,0,600,500)
        self.botRect = pygame.Rect(0,500,600,100)
        self.player1 = Slider(10,210)
        self.computer1 = Slider(570,210)
        self.ball1 = Ball(280,230)
        self.allSprites = pygame.sprite.Group(self.player1,self.computer1,self.ball1)
        self.sliderGroup = pygame.sprite.Group(self.player1,self.computer1)
        self.screen.fill(black,self.botRect)
        self.screen.fill(black,self.topRect)
        pygame.draw.rect(self.screen,white,self.botRect,10)
        self.toText(scoreText,white,30,50,520)
        pygame.display.flip()
        self.run()

    def run(self):
    	#main game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.render()
            self.update()
            #below is temporary for opponent movement
            self.computer1.rect.bottom = self.ball1.rect.bottom

    def render(self):
        self.screen.fill(black)
        self.toText(scoreText,white,30,50,520)
        self.allSprites.draw(self.screen)
        pygame.draw.rect(self.screen,white,self.botRect,10)

    def events(self):
        for event in pygame.event.get():
        	if event.type == QUIT:
        		self.running = False
        		pygame.quit()
        		sys.exit()

        self.keys = pygame.key.get_pressed()

        if self.keys[K_UP]:
            self.player1.rect.y = (self.player1.rect.y - paddleSpeed)

        elif self.keys[K_DOWN]:
        	self.player1.rect.y = (self.player1.rect.y + paddleSpeed)

    def update(self):
        self.toText(self.player1.getScore(),white,30,150,520)
        self.toText(self.computer1.getScore(),white,30,440,520)
        self.allSprites.update()
        s1,s2 = self.ball1.checkScore()
        self.player1.setScore(s1)
        self.computer1.setScore(s2)
        pygame.display.flip()
        self.player1.rect.clamp_ip(self.topRect)
        self.collide = pygame.sprite.spritecollide(self.ball1,self.sliderGroup,False)
        
        if self.collide:
            self.ball1.changeDirection()

        #game over check (first to 3 wins!)
        if self.player1.score == 3 or self.computer1.score == 3:
            self.gameOver()

    def gameOver(self):
        self.playing = False
        self.goStatus = True
        self.screen.fill(black)
        self.toText("Game Over",white,50,170,250)
        self.toText("Play again?",white,30,220,350)
        self.toText("[Enter] = Yes, [Esc] = No",white,30,150,400)
        pygame.display.flip()

        while self.goStatus:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN:

                    if event.key == K_RETURN:
                        self.goStatus = False
                        self.new()

                    if event.key == K_ESCAPE:
                	    self.running = False
                	    pygame.quit()
                	    sys.exit()

def main():
    g = Game()
    g.startScreen()
    while g.running:
        g.new()

main()