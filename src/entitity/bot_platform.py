from src.entitity.platform import Platform

class BotPlatform (Platform):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._is_north = False # 0 -> up, 1 -> down

    def _check_boundaries_collision(self, game):
        return self.position[1] >= game.height or self.position[1] <= 0

    def on_update(self, game):
        if self._is_north:
            self.set_position(None, self.position[1] - 5)
        else:
            self.set_position(None, self.position[1] + 5)