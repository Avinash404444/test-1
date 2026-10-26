class Searching:
    def __init__(self, elements):
        self.elements = elements

    def search(self, key):
        for i, element in enumerate(self.elements):
            if element == key:
                return i + 1
        return -1


elements = [10, 20, 30, 40, 50]
s = Searching(elements)
key = 30
position = s.search(key)
print("Elements:", elements)
print("Search Element:", key)
if position != -1:
    print("Element found at position:", position)
else:
    print("Element not found")
