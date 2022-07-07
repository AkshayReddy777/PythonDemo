from array import *

arr = array('i', [])

n = int(input("enter the length of the array "))

for i in range(n):
    x = int(input("enter the array value "))
    arr.append(x)
print(arr)

val = int(input("enter the value for search "))
k = 0
for e in arr:
    if e == val:
        print(k)

    k+=1

