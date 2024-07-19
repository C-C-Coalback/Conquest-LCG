# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# GIT REPO IS https://github.com/C-C-Coalback/Conquest-LCG.git


class Card:
    def __init__(self, name, text, traits, cost, faction, loyalty, shields):
        self.name = name
        self.text = text
        self.traits = traits
        self.cost = cost
        self.faction = faction
        self.loyalty = loyalty
        self.shields = shields

    def get_name(self):
        return self.name

    def get_text(self):
        return self.text

    def get_traits(self):
        return self.traits

    def get_cost(self):
        return self.cost

    def get_faction(self):
        return self.faction

    def get_loyalty(self):
        return self.loyalty

    def get_shields(self):
        return self.shields


card1 = Card("Splintered Path Acolyte", "Interrupt: When you deploy a Daemon unit, sacrifice this unit to reduce its "
                                        "cost by 2", "Cultist. Tzeentch.", 1, "Chaos", "Common", 0)
print(card1.get_name())
print(card1.get_text())
print(card1.get_traits())
print(card1.get_cost())
print(card1.get_faction())
print(card1.get_loyalty())
print(card1.get_shields())
