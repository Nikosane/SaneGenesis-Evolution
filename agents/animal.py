from agents.base_agent import BaseAgent

class Animal(BaseAgent):
    def __init__(self, name):
        super().__init__(name, "Animal", memory_enabled=False)

    def think(self):
        actions = ["Hunt", "Flee", "Rest"]
        decision = random.choice(actions)
        return decision
