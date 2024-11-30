class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def isEmpty(self):
        return self.front == -1

    def enqueue(self, item):
        if self.isFull():
            return "Queue overflow"
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size 
        self.queue[self.rear] = item
        return f"Enqueued: {item}"

    def dequeue(self):
        if self.isEmpty():
            return "Queue underflow"
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return f"Dequeued: {item}"

    def display(self):
        if self.isEmpty():
            return "Queue is empty"
        if self.rear >= self.front:
            print("Queue contents:", self.queue[self.front:self.rear + 1])
        else:
            print("Queue contents:", self.queue[self.front:] + self.queue[:self.rear + 1])

cq = CircularQueue(5)
print(cq.isEmpty())
print(cq.enqueue(2))
print(cq.enqueue(4))
print(cq.enqueue(8))
print(cq.isEmpty())
print(cq.dequeue())
cq.display()
