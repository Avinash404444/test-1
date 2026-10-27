facts = {"parent": [("john", "mary"), ("mary", "susan")]}

def is_parent(x, y):
    return (x, y) in facts["parent"]

def is_grandparent(x, z):
    for parent, child in facts["parent"]:
        if parent == x and is_parent(child, z):
            return True
    return False

query = input("Is John grandparent of Susan? (yes/no): ").strip().lower()
if query == "yes":
    print("Result:", is_grandparent("john", "susan"))
