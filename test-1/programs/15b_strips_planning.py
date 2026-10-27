state = {"A", "box_A"}
goal = {"B", "box_B"}
actions = [
    ("Pick", {"A", "box_A"}, {"hold", "A"}),
    ("Move", {"A"}, {"B"}),
    ("Drop", {"B", "hold"}, {"box_B", "B"})
]
for name, preconditions, effects in actions:
    if preconditions <= state:
        state |= effects
        print(name)
print("Goal Achieved:", goal <= state)
