class Card:
    def __init__(self, name, text, traits, cost, faction, loyalty, shields, card_type, unique):
        self.name = name
        self.text = text
        self.traits = traits
        self.cost = cost
        self.faction = faction
        self.loyalty = loyalty
        self.shields = shields
        self.card_type = card_type
        self.unique = unique

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

    def get_card_type(self):
        return self.card_type

    def get_unique(self):
        return self.unique


class WarlordCard(Card):
    def __init__(self, name, text, traits, faction, attack, health, bloodied_attack, bloodied_health, bloodied_text):
        super().__init__(name, text, traits, -1, faction, "Signature", 0, "Warlord", False)
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
    def __init__(self, name, text, traits, cost, faction, loyalty, attack, health, command, unique):
        super().__init__(name, text, traits, cost, faction, loyalty, 0, "Army", unique)
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
    def __init__(self, name, text, traits, cost, faction, loyalty, shields, unique):
        super().__init__(name, text, traits, cost, faction, loyalty, shields, "Event", unique)


class AttachmentCard(Card):
    def __init__(self, name, text, traits, cost, faction, loyalty, shields, unique):
        super().__init__(name, text, traits, cost, faction, loyalty, shields, "Attachment", unique)


class SupportCard(Card):
    def __init__(self, name, text, traits, cost, faction, loyalty, unique):
        super().__init__(name, text, traits, cost, faction, loyalty, 0, "Support", unique)


class TokenCard(Card):
    def __init__(self, name, text, traits, faction, attack, health):
        super().__init__(name, text, traits, -1, faction, "Common", 0, "Token", False)
        self.attack = attack
        self.health = health
        self.damage = 0

    def get_attack(self):
        return self.attack

    def get_health(self):
        return self.health

    def get_damage(self):
        return self.damage
