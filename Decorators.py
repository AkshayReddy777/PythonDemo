
def div(a,b):
    print(a/b)

def smart_div(func):

    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return inner
# here we modified an existing fn div with smart div and used the new fn
div1 = smart_div(div)

div1(2,4)



def plus_one(number):
    def add_one(number):
        return number + 1


    result = add_one(number)
    return result
print(plus_one(4))