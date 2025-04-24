import pygame
from pygame.locals import *

from src.draw import Draw

from src.entitity.platform import Platform, BotPlatform
from src.entitity.score import Score
from src.entitity.ball import Ball

class Game:
    def __init__(self):
        self.width = 500
        self.height = 500

        self._is_running = False

        self.surface = pygame.display.set_mode((self.width, self.height), HWSURFACE)
        self._clock = pygame.time.Clock()
        self._draw = Draw(self)

        self.platform = Platform(0, self.height/2, None)
        self.ball = Ball(self.width / 2, self.height / 2)
        self.score = Score()
        self.auto_platform = BotPlatform(self.width-10, 20)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self._close()          
        self.platform.handle_key_press(self)

    def check_collision(self, entity_a, entity_b):
        ax, ay = entity_a.position
        bx, by = entity_b.position

        if (ax < bx + entity_b.width and
            ax + entity_a.width > bx and
            ay < by + entity_b.height and
            ay + entity_a.height > by):
            return True
        return False


    def _loop(self):
        self._handle_events()
        self.auto_platform.on_update(self)
        self.ball.on_update(self)
        self._draw.draw_game()


    def _close(self):
        self._is_running = False
        #self._draw.draw_game()

    def start(self):
        pygame.init()
        self._is_running = True
        
        while self._is_running:
            pygame.display.flip()
            self._loop()
            self._clock.tick(60)
        