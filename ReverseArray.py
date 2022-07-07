from array import *

arr = array('i', [])

n = int(input("enter the length of the array "))

for i in range(n):
    x = int(input("enter the array value "))
    arr.append(x)
print(arr)

arr2 = array('i', [])
j = n-1
while j >= 0:
    arr2.append(arr[j])
    j=j-1
print(arr2)
