import pygame
from src.entitity.entity import Entity

class Platform(Entity):
    def __init__(self, x, y, speed):
        super().__init__("Plataforma pica", 10, 40, x, y, (255, 255, 255))
        self.speed = speed or 10

    def _check_boundaries_collision(self, game, next_position):
        position = next_position if next_position != None else self.position[1]

        return position >= game.height or position < 0

    def _move(self, game, y):
        if self._check_boundaries_collision(game, y):
            return
        self.set_position(None, y)

    def _move_up(self, game):
        self._move(game, self.position[1] - self.speed)

    def _move_down(self, game):
        self._move(game, self.position[1] + self.speed)

    def handle_key_press(self, game):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_w]:
            self._move_up(game)
        if keys_pressed[pygame.K_s]:
            self._move_down(game)

class BotPlatform (Platform):
    def __init__(self, x, y):
        super().__init__(x, y, 40)
        self._is_north = False # 0 -> up, 1 -> down

    def on_update(self, game):
        if self._check_boundaries_collision(game, None):
            self._is_north = not self._is_north

        if self._is_north:
            new_position = self.position[1] - 5
            self.set_position(None, new_position)
        else:
            self.set_position(None, self.position[1] + 5)