class Entity:
    def __init__(self, name, width, height, x, y):
        self.name = name
        self.width = width
        self.height = height

        self.position = [x, y]

    def set_position(self, x, y):
        if x != None:
            self.position[0] = x
        if y != None:
            self.position[1] = y
