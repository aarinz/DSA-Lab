class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning")

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            self.insert_at_beginning(data)
            return
        current = self.head
        for _ in range(position - 1):
            if not current:
                print("Position out of bounds")
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node
        print(f"Inserted {data} at position {position}")

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"Inserted {data} at the end")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Inserted {data} at the end")

    def delete(self, key):
        if not self.head:
            print("List is empty")
            return
        if self.head.data == key:
            self.head = self.head.next
            print(f"Deleted: {key}")
            return
        current = self.head
        while current.next and current.next.data != key:
            current = current.next
        if not current.next:
            print(f"Element {key} not found")
            return
        current.next = current.next.next
        print(f"Deleted: {key}")

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("List contents:", elements)

# Example usage
sll = SinglyLinkedList()

# Case 1: Insert at the beginning
sll.insert_at_beginning(10)
sll.display()

# Case 2: Insert at a position
sll.insert_at_position(20, 1)
sll.display()

# Case 3: Insert at the end
sll.insert_at_end(30)
sll.display()

# Case 4: Delete existing and non-existing elements
sll.delete(10)  # Existing
sll.delete(50)  # Non-existing
sll.display()
