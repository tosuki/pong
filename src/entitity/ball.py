from src.entitity.entity import Entity

class Ball(Entity):
    def __init__(self, x, y):
        super().__init__("ball", 20, 20, x, y)