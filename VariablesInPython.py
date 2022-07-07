
class Car:

    wheels = 4

    def __init__(self):
        self.name = 'bmw'
        self.mile = 10


c1 = Car()
c1.name = 'audi'
c2 = Car()
print(c1.name, c2.name)
c1.wheels
print(Car.wheels)
