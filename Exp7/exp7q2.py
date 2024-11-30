class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        newNode = Node(item)
        if self.front is None:
            self.front = self.rear = newNode
            return
        self.rear.next = newNode
        self.rear = newNode

    def dequeue(self):
        if self.front is None:
            raise IndexError("dequeue from an empty queue")
        item = self.front.data
        self.front = self.front.next
        return item

    def is_empty(self):
        return self.front is None

    def peek(self):
        if self.front is None:
            raise IndexError("peek from an empty queue")
        return self.front.data

if __name__ == "__main__":
    queue = LinkedQueue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Front element:", queue.peek())
    print("Dequeued element:", queue.dequeue())
    print("Dequeued element:", queue.dequeue())
    print("Is queue empty?", queue.is_empty())
    print("Dequeued element:", queue.dequeue())
    print("Is queue empty?", queue.is_empty())
