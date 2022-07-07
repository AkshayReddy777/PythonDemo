from threading import *
class   h(Thread):
    def run(self):
        print("hello")

class he(Thread):
    def run(self):
        print("hi")

f1 = h()
f2 = he()

f1.start()
f2.start()