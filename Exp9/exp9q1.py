class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        original_index = index  

        while self.table[index] is not None:
            index = (index + 1) % self.size
            if index == original_index:
                print("Hash table is full, cannot insert key:", key)
                return
            
        self.table[index] = key
        print(f"Inserted key {key} at index {index}")

    def search(self, key):
        index = self.hash_function(key)
        original_index = index 

        while self.table[index] is not None:
            if self.table[index] == key:
                print(f"Key {key} found at index {index}")
                return index
            index = (index + 1) % self.size
            if index == original_index:
                break
        print(f"Key {key} not found in the hash table")
        return None

    def display(self):
        print("Hash Table:")
        for i in range(len(self.table)):
            print("Index", i, ":", self.table[i])



# Example usage
if __name__ == "__main__":
    hash_table = HashTable(7) 
    hash_table.insert(10)
    hash_table.insert(20)
    hash_table.insert(15)
    hash_table.insert(7)
    hash_table.insert(18)
    hash_table.insert(5)

    hash_table.display()

    hash_table.search(15)  # Should find key
    hash_table.search(8)   # Should not find key
