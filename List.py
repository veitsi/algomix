class List_item:
    def __init__(self, value):
        assert value is not None
        self.value = value
        self.next = None

    def connect(self, item):
        self.next = item
        return item


assert List_item(5) is not None
assert List_item(5).value == 5
item = List_item(5)
item.connect(List_item(7)).connect(List_item(3))
assert item.value == 5
assert item.next.next.value == 3
