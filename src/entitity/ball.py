from src.entitity.entity import Entity

class Ball(Entity):
    def __init__(self, x, y):
        super().__init__("ball", 20, 20, x, y)
        self._speed = 5
        self._diagonal_factor = self._speed - self._speed/2
        self._is_north = True
        self._is_east = True

    def _get_diagonal_y(self):
        return self.position[1]+self._diagonal_factor if self._is_north else self.position[1]-self._diagonal_factor

    def move_left(self):
        self.set_position(
            self.position[0]-10,
            self._get_diagonal_y()
        )

    def move_right(self):
        self.set_position(
            self.position[0]+10,
            self._get_diagonal_y()
        )

    def _check_boundaries(self, game):
        if self.position[0] >= game.width or self.position[0] <= 0:
            self._is_east = not self._is_east
        if self.position[1] >= game.height or self.position[1] <= 0:
            self._is_north = not self._is_north

    def on_update(self, game):
        self._check_boundaries(game)
        if self._is_east:
            self.move_left()
        else:
            self.move_right()
