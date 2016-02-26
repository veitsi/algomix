import random


def partify(start, end):
    print('partify start, end ', start, end)
    while True:
        pos_index = random.randrange(start, end + 1)
        pindex = end
        pivot = a[pos_index]
        i=end
        while i>start:
            if a[pindex] > pivot:
                pindex -= 1
            i-=1
        print("founded ",pindex)
        # input("Press Enter to continue...")
        break
    a[pindex], a[pos_index] = a[pos_index], a[pindex]

    i, j = start, end
    while i != j:
        print('pindex', pindex)
        while i < pindex:
            if a[i] > pivot:
                break
            i += 1
        while j > pindex:
            if a[j] < pindex:
                break
            j -= 1
        print(a)
        print('i,j ',i,j)
        if i < pindex or j > pindex:
            a[i], a[j] = a[j], a[i]
    return pindex


def quick(start, end):
    print('quick start, end ', start, end)
    if end < start or start < 0 or end < 0 \
            or start > len(a) or end > len(a):
        return False
    if end == start:
        return True
    if end - start == 1:
        if a[start] > a[end]:
            a[start], a[end] = a[end], a[start]
        return a[start], a[end]
    print(a)
    pindex = partify(start, end)
    print('pindex =', pindex)
    print(a)
    if pindex > start:
        print('left part')
        quick(start, pindex - 1)
    if pindex < end:
        print('right part')
        quick(pindex + 1, end)
    return True


# a = [7, 8, 4, 1, 3, 0, 2, 5]
# assert quick(1, 1) == True
# assert quick(3, 3) == True
# assert quick(0, 1) == (7, 8)
# assert quick(1, 2) == (4, 8)
# assert quick(6, 7) == (2, 5)

a = [3, 2, 9, 1, 0, 5, 8, 7]
a= [12, 7, 18, 1, 0, 4, 11, 3, 9]
partify(1, 7)
#quick(0, 7)
# a = [7, 8, 4, 1, 3, 0, 12, 2]
# partify(0, len(a) - 1)
# a = [7, 8, 4, 1, 3, 0, 2, 5]
# quick(0,len(a)-1)
