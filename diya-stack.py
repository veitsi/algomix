class Stack:
    def __init__(self, size=10):
        if size < 2:
            return None
        self.size = size
        self.__stack = [None for i in range(size)]
        self.__position = -1

    def __str__(self):
        return str(self.__stack[:self.__position + 1])

    def push(self, x):
        if type(x) != type(1):
            return None
        if self.__position == self.size - 1:
            return None
        self.__position += 1

        self.__stack[self.__position] = x
        return self

    def pop(self):
        if self.__position == -1:
            return None
        rez = self.__stack[self.__position]
        self.__position -= 1
        return rez


assert Stack() is not None
assert Stack(10) is not None

# assert Stack(1)==None
assert Stack().push(1) is not None
assert Stack().push(1).push(2) is not None

st1 = Stack().push(1).push(2)
assert str(st1) == "[1, 2]"
assert st1.pop() == 2
p2 = st1.pop()
print(p2)
assert p2 == 1

assert st1.pop() is None

assert st1.push(0x0A) is not None
assert st1.push(Stack()) is None

st1 = Stack(3)
assert st1.push(1).push(2).push(3).push(4) is None
