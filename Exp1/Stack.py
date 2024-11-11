class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * self.size
        self.top = -1

    def isFull(self):
        return self.top == self.size - 1
    
    def isEmpty(self):
        return self.top == -1
    
    def push(self, element):
        if self.isFull():
            print("Stack is Full")
        else:
            self.top +=1
            self.stack[self.top] = element
            print(f"{element} pushed to stack")
    
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            i = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            print(f"{i} popped from stack")
            return i
    
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.stack[self.top]
        
    def display(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(self.stack)

s = Stack(5)
s.push(1)
s.push(2)
s.push(3)   
s.push(4)
s.display()
s.pop()
s.display()
