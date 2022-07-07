from numpy import *

arr = array([23,12,56,9,2])
max = arr[0]
for i in range(len(arr)):
    if arr[i]>max:
        max = arr[i]
print(max)


