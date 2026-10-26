class BinarySearch:
    def __init__(self, elements):
        self.elements = elements

    def search(self, key):
        low, high = 0, len(self.elements) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.elements[mid] == key:
                return mid
            elif key < self.elements[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1


elements = [10, 20, 30, 40, 50, 60, 70]
bs = BinarySearch(elements)
key = 50
result = bs.search(key)
if result != -1:
    print("Element found at position:", result + 1)
else:
    print("Element not found")
