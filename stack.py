class Stack:
    def __init__(self, size=10):
        if size < 1:
            return None
        self.stack = [None for i in range(size)]
        self.size = size
        self.position = -1

    def push(self, el):
        if self.position > self.position or el is None:
            return False
        else:
            self.position += 1
            self.stack[self.position] = el
            return self

    def pop(self):
        if self.position < 0:
            return None
        rez = self.stack[self.position]
        self.position -= 1
        return rez


assert type(Stack(10)) is not None
assert Stack(1) is not None
assert Stack() is not None
assert Stack().push(7).push(3) is not None
print(Stack().push(7).push(3).stack)

assert Stack().push(7).pop() is not None
assert Stack().push(7).push(2).pop() == 2
s = Stack().push(7).push(2)
s.pop()
print(s.pop())
