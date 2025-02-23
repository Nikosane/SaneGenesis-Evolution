class Society:
    def __init__(self):
        self.population = 10
        self.government_type = "Tribal"

    def evolve_government(self):
        possible_govs = ["Tribal", "Monarchy", "Democracy", "Technocracy"]
        self.government_type = random.choice(possible_govs)

    def grow_population(self):
        self.population += random.randint(1, 5)

    def to_dict(self):
        return {"population": self.population, "government_type": self.government_type}

    @classmethod
    def load_from_state(cls, data):
        soc = cls()
        soc.population = data["population"]
        soc.government_type = data["government_type"]
        return soc
