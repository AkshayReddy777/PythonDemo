'''import  sys

print(sys.getrecursionlimit())
def greet():
    print("AKSHAY")
    greet()

greet()'''


def factrec(n):

    if(n == 0):
        return 1

    return n * factrec(n-1)

print(factrec(5))