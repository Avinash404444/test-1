class Sorting:
    def __init__(self, elements):
        self.elements = elements

    def sort(self):
        n = len(self.elements)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.elements[j] > self.elements[j + 1]:
                    self.elements[j], self.elements[j + 1] = self.elements[j + 1], self.elements[j]

    def display(self):
        print("Sorted Elements:", self.elements)


elements = [50, 20, 40, 10, 30]
s = Sorting(elements)
print("Original Elements:", elements)
s.sort()
s.display()
