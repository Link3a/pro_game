class BaseObject:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self):
        return [self.x, self.y, self.z]

class Block(BaseObject):

    def Shatter(self):
        self.x = self.y = self.z = None


class Entity(BaseObject):
    def move(self, x, y, z):
        self.x, self.y, self.z = x, y, z


class Thing(BaseObject):
    pass

house = Block(2, 2, 4)
house.z = 100
human = Entity(2, 4, 4)
human.move(3, 4, 5)
human.z = 999
print(house.get_coordinates())
print(human.get_coordinates())


