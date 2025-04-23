import pygame

class Draw:
    def __init__(self, game):
        self.game = game

    def _draw_rectangle_entity(self, entity):
        pygame.draw.rect(
            self.game.surface,
            pygame.Color(255, 255, 255),
            pygame.Rect(
                entity.position[0],
                entity.position[1],
                entity.width,
                entity.height
            )
        )

    def _draw_background(self):
        pygame.draw.rect(
            self.game.surface,
            pygame.Color(155, 155, 155),
            pygame.Rect(0, 0, self.game.width, self.game.height)
        )

    def draw_game(self):
        self._draw_background()
        self._draw_rectangle_entity(self.game.platform)
        self._draw_rectangle_entity(self.game.auto_platform)