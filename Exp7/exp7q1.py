class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, item):
        newNode = Node(item)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        if self.top is None:
            print("Stack is empty! Cannot pop.")
            return None
        item = self.top.data
        self.top = self.top.next
        print(f"Popped {item} from the stack")
        return item

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.top is None:
            raise IndexError("peek from an empty stack")
        return self.top.data

# Example usage
if __name__ == "__main__":
    stack = LinkedStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top element:", stack.peek())  # Output: 30
    print("Popped element:", stack.pop())  # Output: 30
    print("Popped element:", stack.pop())  # Output: 20
    print("Is stack empty?", stack.is_empty())  # Output: False
    print("Popped element:", stack.pop())  # Output: 10
    print("Is stack empty?", stack.is_empty())  # Output: True
