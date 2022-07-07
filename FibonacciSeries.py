
def fibonacci(n):

    x = int(n)
    a = 0;
    b = 1;
    if x < 0:
        print("enter the positive num only")
        return
    print(a , end="\n")
    print(b)
    for i in range(0,x-2):
        c = a+b
        print(c)
        a=b
        b=c

def fibonacciUntilCertainNumber(n):

    x = int(n)
    a = 0;
    b = 1;
    if x < 0:
        print("enter the positive num only")
        return
    print(a , end="\n")
    print(b)
    for i in range(0,x-2):
        c = a+b
        if c < x:
            print(c)
            a = b
            b = c


n = input("enter the limit for the series ")
fibonacciUntilCertainNumber(n)
fibonacci(n)
print("GoodDay")