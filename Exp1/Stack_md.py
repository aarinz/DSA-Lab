class Stack:
    def __init__(self,size):
        self.size = size
        self.stack = [None] * self.size
        self.top = -1 #follows 0 based indexing
    
    def isFull(self):
        return self.top == self.size - 1 #top is at the last index

    def isEmpty(self):
        return self.top == -1
    
    def push(self, element):
        if self.isFull():
            print("Stack is Full")
        else:
            self.top += 1
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


print("push")
print("pop")
print("peek")
print("display")
print("exit")

while True:
    print("Enter your choice:")
    choice = input()
    if choice == "1":
        element = input("Enter the element to push:")
        s.push(element)
    elif choice == "2":
        print(s.pop())
    elif choice == "3":
        print(s.peek())
    elif choice == "4":
        s.display()
    elif choice == "5":
        break
