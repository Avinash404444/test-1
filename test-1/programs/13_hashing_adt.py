class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        start = index
        while self.table[index] is not None:
            index = (index + 1) % self.size
            if index == start:
                raise OverflowError("Hash table is full")
        self.table[index] = key

    def search(self, key):
        index = self.hash_function(key)
        start = index
        while self.table[index] is not None:
            if self.table[index] == key:
                return index
            index = (index + 1) % self.size
            if index == start:
                break
        return -1

    def display(self):
        print("Hash Table:")
        for i, value in enumerate(self.table):
            print(i, ":", value)


h = HashTable(7)
for value in [10, 20, 15, 7, 25]:
    h.insert(value)
h.display()

key = 15
position = h.search(key)
if position != -1:
    print("Element", key, "found at index:", position)
else:
    print("Element", key, "not found")
