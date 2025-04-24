class Entity:
    def __init__(self, name, width, height, x, y, color = (255, 255, 255)):
        self.name = name
        self.width = width
        self.height = height
        self.color = color

        self.position = [x, y]

    def get_color(self):
        return self.color

    def set_position(self, x, y):
        if x != None:
            self.position[0] = x
        if y != None:
            self.position[1] = y
