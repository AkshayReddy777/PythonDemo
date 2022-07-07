

def calc(lst):

    even = 0;
    odd=0;
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even, odd


lst=[]
n = int(input("Enter the size of list"))
for i in range(0,n):
    ele = int(input())
    lst.append(ele)


even , odd = calc(lst)
print("Even : {} , Odd : {}".format(even,odd))