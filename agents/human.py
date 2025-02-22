from agents.base_agent import BaseAgent

class Human(BaseAgent):
    def __init__(self, name):
        super().__init__(name, "Human")

    def think(self):
        actions = ["Trade", "Form Alliance", "Go to War", "Explore"]
        decision = random.choice(actions)
        self.remember(f"Decided to {decision}")
        return decision
