from numpy import *

arr1 = array([1,2,3,4,5])

arr2 = linspace(0,20,9)

arr3 = logspace(2,40,3)

arr4 = arange(0,15,3)

arr5 = zeros(5, int)

arr6 = ones(6 , float)

print(arr1, arr2,arr3, arr4 ,arr5, arr6)


arr7 = arr1 + arr1

arr8 = sqrt(arr4)

arr9 = concatenate([arr7,arr1])

print(arr9, arr7, arr8)

arr10 = arr1

arr11 = arr2.view()

arr12 = arr3.copy()

print(arr12, arr11, arr10)

print(id(arr1), id(arr10))
print(id(arr2), id(arr11))
print(id(arr3), id(arr12))
