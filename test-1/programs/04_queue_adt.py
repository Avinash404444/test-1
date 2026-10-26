queue = []

while True:
    print("\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter the element: ")
        queue.append(item)
        print(item, "inserted into the queue")
    elif choice == 2:
        if not queue:
            print("Queue is empty")
        else:
            print("Deleted element:", queue.pop(0))
    elif choice == 3:
        print("Queue:", queue) if queue else print("Queue is empty")
    elif choice == 4:
        print("Exiting program")
        break
    else:
        print("Invalid choice")
