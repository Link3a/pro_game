class Animal:
    def breathe(self):
    pass

    def eat(self):


class Fish(Animal):
    def swim(self):
    pass


class Bird(Animal):
    def lay_eggs(self):
    pass


class FlyingBird(Animal):
    def fly(self):
    pass

sparrow = FlyingBird()
sparrow.fly()
