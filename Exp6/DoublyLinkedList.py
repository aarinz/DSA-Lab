class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 1:
            self.insert_at_beginning(data)
            return
        temp = self.head
        for i in range(position - 2):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next
        if temp is None:
            print("Position out of range")
            return
        new_node.next = temp.next
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node
        new_node.prev = temp

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def delete_element(self, data):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp and temp.data != data:
            temp = temp.next
        if temp is None:
            print("Element not found in the list")
            return
        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev
        if temp == self.head:
            self.head = temp.next
        del temp

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" <-> " if temp.next else "\n")
            temp = temp.next

dll = DoublyLinkedList()
dll.insert_at_beginning(10)
dll.display()
dll.insert_at_position(20, 2)
dll.insert_at_position(30, 2)
dll.display()
dll.insert_at_end(40)
dll.display()
dll.delete_element(30)
dll.display()
dll.delete_element(50)