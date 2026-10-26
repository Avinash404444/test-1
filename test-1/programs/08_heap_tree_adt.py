class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def display(self):
        print("Heap:", self.heap)


heap = MaxHeap()
for value in [50, 30, 40, 10, 20, 35]:
    heap.insert(value)
heap.display()
