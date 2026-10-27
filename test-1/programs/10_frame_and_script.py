person_frame = {
    "name": "Alice",
    "age": 30,
    "occupation": "Engineer",
    "address": {"city": "Chennai", "zip": "600001"}
}

def morning_routine():
    steps = ["Wake up", "Brush teeth", "Exercise", "Take shower", "Eat breakfast"]
    for step in steps:
        print("Step:", step)

print("Name:", person_frame["name"])
print("City:", person_frame["address"]["city"])
morning_routine()
