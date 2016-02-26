def find_place(a=[], el=None):
    assert a == sorted(a)
    i = len(a) - 1
    while i > -1:
        if a[i] < el:
            i += 1
            break
        i -= 1
    if i == -1:
        i = 0
    return i


def insertion_sort(a=[]):
    if len(a) < 2:
        return a
    b = [a[0]]
    i = 1
    while i < len(a):
        b.insert(find_place(b, a[i]), a[i])
        i += 1
    return b


assert find_place([0], 1) == 1
assert find_place([1], 0) == 0
assert find_place([1, 3, 4, 9, 11], 2) == 1

assert insertion_sort([]) == []
assert insertion_sort([1]) == [1]
assert insertion_sort([7, 4]) == [4, 7]
assert insertion_sort([7, 11, 9, 3, 12, 4]) == [3, 4, 7, 9, 11, 12]

assert insertion_sort([8, 8, 8]) == [8, 8, 8]
