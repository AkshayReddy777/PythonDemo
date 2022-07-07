
def factorial(n):
    fact = 1
    for i in range(1,n+1):

        fact = fact * i
    return fact
n = int(input("enter the factorial value "))
x = factorial(n)

print("factorial of the number is : {}".format(x))