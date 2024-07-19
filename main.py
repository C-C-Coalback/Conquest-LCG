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


class WarlordCard(Card):
    def __init__(self, name, text, traits, faction, attack, health, bloodied_attack, bloodied_health, bloodied_text):
        super().__init__(name, text, traits, -1, faction, "Signature", 0)
        self.attack = attack
        self.health = health
        self.damage = 0
        self.bloodied_attack = bloodied_attack
        self.bloodied_health = bloodied_health
        self.bloodied_text = bloodied_text

    def get_attack(self):
        return self.attack

    def get_health(self):
        return self.health

    def get_damage(self):
        return self.damage

    def get_bloodied_attack(self):
        return self.bloodied_attack

    def get_bloodied_health(self):
        return self.bloodied_health

    def get_bloodied_text(self):
        return self.bloodied_text


class ArmyCard(Card):
    def __init__(self, name, text, traits, cost, faction, loyalty, attack, health, command):
        super().__init__(name, text, traits, cost, faction, loyalty, 0)
        self.attack = attack
        self.health = health
        self.damage = 0
        self.command = command

    def get_attack(self):
        return self.attack

    def get_health(self):
        return self.health

    def get_damage(self):
        return self.damage

    def get_command(self):
        return self.command


class EventCard(Card):
    def __init__(self, name, text, traits, cost, faction, loyalty, shields):
        super().__init__(name, text, traits, cost, faction, loyalty, shields)


class AttachmentCard(Card):
    def __init__(self, name, text, traits, cost, faction, loyalty, shields):
        super().__init__(name, text, traits, cost, faction, loyalty, shields)


class TokenCard(Card):
    def __init__(self, name, text, traits, faction, attack, health):
        super().__init__(name, text, traits, -1, faction, "Common", 0)
        self.attack = attack
        self.health = health
        self.damage = 0

    def get_attack(self):
        return self.attack

    def get_health(self):
        return self.health

    def get_damage(self):
        return self.damage


"""   
card1 = ArmyCard("Splintered Path Acolyte", "Interrupt: When you deploy a Daemon unit, sacrifice this unit to reduce "
                                            "its cost by 2", "Cultist. Tzeentch.", 1, "Chaos", "Common", 1, 1, 1)
print("Name: ", card1.get_name())
print("Text: ", card1.get_text())
print("Traits: ", card1.get_traits())
print("Cost: ", card1.get_cost())
print("Faction: ", card1.get_faction())
print("Loyalty: ", card1.get_loyalty())
print("Shields: ", card1.get_shields())
print("Attack: ", card1.get_attack())
print("Health: ", card1.get_health())
print("Command: ", card1.get_command())

card2 = WarlordCard("Zarathur, High Sorcerer", "Interrupt: When damage is assigned to an enemy unit at this planet, "
                                               "increase that damage by 1.", "Psyker. Tzeentch.", "Chaos", 1, 6, 1, 5,
                    "Bloodied.")

print(card2.get_name())
print(card2.get_text())
print(card2.get_traits())
print(card2.get_cost())
print(card2.get_faction())
print(card2.get_loyalty())
print(card2.get_shields())
print(card2.get_attack())
print(card2.get_health())
print(card2.get_bloodied_attack())
print(card2.get_bloodied_health())
print(card2.get_bloodied_text())
"""
