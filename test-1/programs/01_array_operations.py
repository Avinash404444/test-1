from array import array

arr = array('i', [10, 20, 30, 40, 50])
print("Original Array:", arr)

print("\nArray Elements:")
for i in arr:
    print(i, end=" ")

arr.insert(2, 25)
print("\n\nAfter Inserting 25 at Index 2:")
print(arr)

arr.append(60)
print("\nAfter Appending 60:")
print(arr)

arr.remove(40)
print("\nAfter Removing 40:")
print(arr)

search = int(input("\nEnter element to search: "))
if search in arr:
    print(search, "found at index", arr.index(search))
else:
    print(search, "not found in the array")

index = int(input("\nEnter index to update: "))
value = int(input("Enter new value: "))
arr[index] = value
print("\nAfter Updating:")
print(arr)

print("\nFirst Element:", arr[0])
print("Last Element:", arr[-1])
print("Length of Array:", len(arr))

arr.reverse()
print("\nReversed Array:")
print(arr)
