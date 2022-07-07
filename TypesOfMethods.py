
class Student:

    school = 'Trs'

    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2
    def avg(self):
        return (self.a1/2 + self.a2/2)

s1 = Student(2,4)
s2 = Student(5,7)


print(s1.avg(),s2.avg())
s2.avg()