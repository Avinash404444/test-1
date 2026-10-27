state = {"A", "package", "free"}
goal = {"B", "delivered"}
actions = [
    ("Move A-B", {"A", "free"}, {"B"}),
    ("Deliver", {"B", "package"}, {"delivered"})
]
for name, preconditions, effects in actions:
    if preconditions <= state:
        state |= effects
        print(name)
print("Goal Achieved:", goal <= state)
