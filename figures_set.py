class Figures:
    def __init__(self, name):
        self.name = name

    def set_colour(self, colour):
        self.colour = colour

    def set_coor(self, coor):
        self.coor = coor

    def move(self, new_coor):
        self.coor = new_coor
