from src.entitity.entity import Entity

class Score(Entity):
    def __init__(self):
        super().__init__("Score", 100, 50, 30, 30, (10, 10, 10))