class LinearQueue:
    def __init__(self, s):
        self.size = s
        self.queue = [None] * self.size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return self.rear == self.size - 1

    def enqueue(self, elem):
        if self.is_full():
            print("Queue is full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = elem
            print(f"{elem} enqueued to queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            item = self.queue[self.front]
            self.front += 1
            print(f"{item} dequeued from queue")
            return item

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements are:", self.queue[self.front:self.rear + 1])
        
s = LinearQueue(5)
s.enqueue(10)
s.enqueue(20)
s.enqueue(30)
s.display()
s.dequeue()
s.display()
s.enqueue(40)
s.enqueue(50)
s.display()
s.enqueue(60)
s.dequeue()
s.display()
