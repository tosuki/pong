import pygame
from pygame.locals import *

from src.draw import Draw
from src.entitity.platform import Platform, BotPlatform

class Game:
    def __init__(self):
        self.width = 500
        self.height = 500

        self._is_running = False

        self.surface = pygame.display.set_mode((self.width, self.height), HWSURFACE)
        self._clock = pygame.time.Clock()
        self._draw = Draw(self)

        self.platform = Platform(20, 20, None)
        self.auto_platform = BotPlatform(self.width - 20, 20)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self._close()          
            self.platform.handle_key_press(self)

    def _loop(self):
        self._handle_events()
        self.auto_platform.on_update(self)
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
        