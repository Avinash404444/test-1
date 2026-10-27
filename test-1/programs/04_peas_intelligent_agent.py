class Environment:
    def __init__(self):
        self.rooms = {"A": "Dirty", "B": "Dirty"}
        self.location = "A"

class Agent:
    def __init__(self, environment):
        self.environment = environment
        self.score = 0

    def act(self):
        env = self.environment
        if env.rooms[env.location] == "Dirty":
            env.rooms[env.location] = "Clean"
            self.score += 1
            print(f"Cleaned {env.location}")
        else:
            env.location = "B" if env.location == "A" else "A"
            print(f"Moved to {env.location}")

    def run(self):
        for _ in range(4):
            self.act()
        print("Final:", self.environment.rooms, "Score:", self.score)

Agent(Environment()).run()
