import random

class Evolution:
    def __init__(self):
        pass

    def mutate_agent(self, agent):
        traits = ["intelligence", "strength", "charisma"]
        trait = random.choice(traits)
        return f"{agent} has evolved with increased {trait}!"
