class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete(self, key):
        if self.head is None:
            print("Linked List is Empty")
            return
        temp = self.head
        if temp.data == key:
            self.head = temp.next
            print(key, "deleted successfully.")
            return
        prev = None
        while temp and temp.data != key:
            prev, temp = temp, temp.next
        if temp is None:
            print("Element not found.")
            return
        prev.next = temp.next
        print(key, "deleted successfully.")

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                print(key, "found in the linked list.")
                return
            temp = temp.next
        print(key, "not found.")

    def display(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


ll = LinkedList()
while True:
    print("\n----- LINKED LIST OPERATIONS -----")
    print("1. Insert\n2. Delete\n3. Search\n4. Display\n5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        ll.insert(int(input("Enter element to insert: ")))
    elif choice == 2:
        ll.delete(int(input("Enter element to delete: ")))
    elif choice == 3:
        ll.search(int(input("Enter element to search: ")))
    elif choice == 4:
        ll.display()
    elif choice == 5:
        print("Program Ended")
        break
    else:
        print("Invalid Choice")
