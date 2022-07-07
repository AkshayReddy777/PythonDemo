
pos = -1


def search(lst, n):
    low = 0
    upper = len(lst) - 1

    while low <= upper:
        mid = (low+upper)//2

        if lst[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < n:
                low = mid+1
            else:
                upper = mid-1
    return False


def forsearch(lst , n):

    for i in lst:
        if i == n:
            globals()['pos'] = lst.index(i)+1
            return True
    return False


lst = [1, 2, 5, 6, 9, 100, 12, 15, 19, 22, 24, 26]
n = 120
lst.sort()
print(lst)
if search(lst , n):
    print("found at ", pos)
else:
    print("not found")





