class Economy:
    def __init__(self):
        self.markets = {"food": 1.0, "water": 1.0, "materials": 1.0}
        self.currency_value = 1.0

    def fluctuate_prices(self):
        for item in self.markets:
            self.markets[item] *= random.uniform(0.9, 1.1)

    def to_dict(self):
        return {"markets": self.markets, "currency_value": self.currency_value}

    @classmethod
    def load_from_state(cls, data):
        eco = cls()
        eco.markets = data["markets"]
        eco.currency_value = data["currency_value"]
        return eco
