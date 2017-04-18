import random

class Spell:
    def __init__(self, name, cost, dmg, types):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = types

    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)
