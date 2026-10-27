class Agent:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def move(self):
        self.position += 1

agents = [Agent("Agent 1", 0), Agent("Agent 2", 2), Agent("Agent 3", 4)]
for step in range(3):
    print("Step", step + 1)
    for agent in agents:
        agent.move()
        print(agent.name, "Position:", agent.position)
