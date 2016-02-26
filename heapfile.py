class Node:
    def __init__(self, value, left=None, right=None):
        assert value is not None
        self.value = value
        self.parent = None
        if right is not None:
            self.right = Node(right)
            self.right.parent = self
        if left is not None:
            self.left = Node(left)
            self.left.parent = self

    def __str__(self):
        rez = str(self.value) + ":"
        if hasattr(self, 'left'):
            rez += str(self.left.value)
        if hasattr(self, 'right'):
            rez += "," + str(self.right.value)
        return rez


'''testing Node class
# p=Node(None)
# p = Node(1)
# print(p)
# p=Node(1,4)
# print(p)
# p = Node(1)
# p2 = Node(4)
# p.left = p2
# p3 = Node(3)
# p.right = p3
# print(p)
p = Node(44, 4, 3)
print(p)
print(p.left.parent.value)
'''


class Heap:
    def __init__(self, a):
        if type(a) == type([]):
            assert len(a) > 0
            self.__top = Node(a[0])
            i = 0

    def see_top(self):
        return self.__top.value


h = Heap([4, 1, 2])
print(h._Heap__top)
assert h.see_top() == 4
# print(h._Heap__see_top())

