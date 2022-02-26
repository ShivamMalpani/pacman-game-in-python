import imp
from re import L
import pygame as pg
import sys
from settings import *

pg.init()
vec = pg.math.Vector2

class App:
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True
        self.state = 'intro'

    def run(self):
        while self.running:
            if self.state == 'intro':
                self.intro_events()
                self.intro_update()
                self.intro_draw()
            else :
                pass

            self.clock.tick(FPS) 
        pg.quit()
        sys.exit()



########################   INTRO FUNCTIONS   ########################


    def intro_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
    

    def intro_update(self):
        pass


    def intro_draw(self):
        pg.display.update()