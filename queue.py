class Queue:
    def __init__(self,size=10):
        if size<1:
            return None
        self.queue=[None for i in range(size)]
        self.head=0
        self.tail=-1

    def enqueue(self,el):
        if el is None:
            return None
        self.tail+=1
        self.queue[self.tail]=el
        return self

    def dequeue(self):
        if self.head<0:
            return None
        rez = self.queue[self.head]
        self.head+=1
        return rez

assert Queue() is not None
assert Queue(5) is not None
assert Queue(5).queue==[None, None, None, None, None]
print(Queue(5).queue)

assert Queue().enqueue(5) is not None
assert Queue().enqueue(5).enqueue(3) is not None
print(Queue().enqueue(5).enqueue(3).queue)
assert Queue().enqueue(5).dequeue()==5
