pos = -1
def search(lst,n):
    i = 0
    while i < len(lst):
        if lst[i] == n:
            globals()['pos'] = i+1
            return True
        i = i+1
    return False


def forsearch(lst , n):

    for i in lst:
        if i == n:
            globals()['pos'] = lst.index(i)+1
            return True
    return False

lst = [1,2,5,6,9,10,12,7]
n = 10

if forsearch(lst , n):
    print("found at " , pos)
else:
    print("not found")