from array import *

arr = array('i', [])

n = int(input("enter the length of the array "))

for i in range(n):
    x = int(input("enter the array value "))
    arr.append(x)
print(arr)
del arr[2]
arr.pop(2)
print(arr)