
vals = [1,2,5,6]

it = iter(vals)

print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())


class newName:

    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val = self.num
            self.num += 1
        else:
            raise StopIteration

        return val
vals = newName()

for i in vals:
    print(i)