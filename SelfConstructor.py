
class Computer:

    def __init__(self):
        self.name= 'navin'
        self.age = 28




c1 = Computer()
c2 = Computer()


c1.name= 'rashi'
print(c1.name)
print(c2.name)
print(id(c1), id(c2))