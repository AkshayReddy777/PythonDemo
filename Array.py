from array import array

values = array('i', [1,2])
values.reverse()

newValues = array(values.typecode, (a*5 for a in values))
for e in newValues:
    print(e)