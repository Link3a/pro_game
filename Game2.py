class BaseObject:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
         self.__y = y

    def set_z(self, z):
        self.__z = z

    def get_coordinates(self):
        return [self.__x, self.__y, self.__z]

class Block(BaseObject):

    def Shatter(self):
        self.set_x(None)
        self.set_y(None)
        self.set_z(None)

class Entity(BaseObject):
    def move(self, x, y, z):
        self.set_x(x)
        self.set_y(y)
        self.set_z(z)

class Thing(BaseObject):
    pass

house = Block(2, 2, 4)
house.Shatter()
print(house.get_coordinates())
human = Entity(2, 4, 4)
human.move(3, 4, 5)
print(house.get_coordinates())
print(human.get_coordinates())