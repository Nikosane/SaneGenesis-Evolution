import random

class Environment:
    def __init__(self):
        self.weather = "Sunny"
        self.terrain = "Plains"
        self.resources = {"food": 100, "water": 100, "materials": 50}
    
    def change_weather(self):
        self.weather = random.choice(["Sunny", "Rainy", "Stormy", "Snowy"])
        return self.weather

    def deplete_resources(self):
        for key in self.resources:
            self.resources[key] = max(0, self.resources[key] - random.randint(1, 10))

    def populate(self):
        print("🌍 Generating environment and agents...")

    def to_dict(self):
        return {"weather": self.weather, "terrain": self.terrain, "resources": self.resources}

    @classmethod
    def load_from_state(cls, data):
        env = cls()
        env.weather = data["weather"]
        env.terrain = data["terrain"]
        env.resources = data["resources"]
        return env
