class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(item, "inserted into the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow!")
        else:
            print("Deleted Element:", self.items.pop())

    def peek(self):
        if self.is_empty():
            print("Stack is Empty!")
        else:
            print("Top Element:", self.items[-1])

    def display(self):
        if self.is_empty():
            print("Stack is Empty!")
        else:
            print("Stack Elements (Top to Bottom):")
            for item in reversed(self.items):
                print(item)

    def size(self):
        print("Stack Size:", len(self.items))

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()
while True:
    print("\n******** STACK OPERATIONS ********")
    print("1. Push\n2. Pop\n3. Peek\n4. Display\n5. Size\n6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        stack.push(int(input("Enter the element to push: ")))
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.peek()
    elif choice == 4:
        stack.display()
    elif choice == 5:
        stack.size()
    elif choice == 6:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice! Please enter a valid option.")
