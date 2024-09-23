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
        self.ready = True

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

    def get_ready(self):
        return self.ready


class WarlordCard(Card):
    def __init__(self, name, text, traits, faction, attack, health, bloodied_attack, bloodied_health, bloodied_text,
                 starting_resources, starting_cards):
        super().__init__(name, text, traits, -1, faction, "Signature", 0, "Warlord", False)
        self.attack = attack
        self.health = health
        self.damage = 0
        self.bloodied = False
        self.bloodied_attack = bloodied_attack
        self.bloodied_health = bloodied_health
        self.bloodied_text = bloodied_text
        self.starting_resources = starting_resources
        self.starting_cards = starting_cards
        self.command = 999

    def get_attack(self):
        return self.attack

    def get_health(self):
        return self.health

    def get_damage(self):
        return self.damage

    def get_command(self):
        return self.command

    def get_bloodied_state(self):
        return self.bloodied

    def get_bloodied_attack(self):
        return self.bloodied_attack

    def get_bloodied_health(self):
        return self.bloodied_health

    def get_bloodied_text(self):
        return self.bloodied_text

    def get_starting_resources(self):
        return self.starting_resources

    def get_starting_cards(self):
        return self.starting_cards

    def damage_card(self, amount):
        amount = self.shield_window(amount)
        self.assign_damage(amount)
        if self.check_health():
            print("Card still standing")
            return 0
        else:
            print("Damage exceeds health")
            return 1

    def shield_window(self, amount):
        print(self.get_name(), "taking", amount, "damage. Shields:")
        shield = input()
        if shield == 0:
            print("No shields used")
        else:
            print("shield value:", shield)
            amount = int(amount)
            shield = int(shield)
            amount = amount - shield
            if amount < 0:
                amount = 0
        return amount

    def assign_damage(self, amount):
        self.damage = self.damage + amount

    def check_health(self):
        if self.health > self.damage:
            return 1
        else:
            return 0

    def print_info(self):
        if self.unique:
            print("Name: *", self.name)
        else:
            print("Name:", self.name)
        print("Type:", self.card_type)
        print("Faction:", self.faction)
        print("Traits:", self.traits)
        print("Resources:", self.starting_resources, "\nCards:", self.starting_cards)
        if not self.bloodied:
            print("Text:", self.text, "\nStats:", self.attack, "Attack,", self.health, "Health")
        else:
            print("Text:", self.bloodied_text, "\nStats:", self.bloodied_attack, "Attack,",
                  self.bloodied_health, "Health")


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

    def print_info(self):
        if self.unique:
            print("Name: *", self.name)
        else:
            print("Name:", self.name)
        print("Type:", self.card_type)
        print("Faction:", self.faction)
        print("Cost:", self.cost)
        print("Traits:", self.traits)
        print("Loyalty:", self.loyalty)
        print("Text:", self.text, "\nStats:", self.attack, "Attack,", self.health, "Health,", self.command, "Command")

    def damage_card(self, amount):
        amount = self.shield_window(amount)
        self.assign_damage(amount)
        if self.check_health():
            print("Card still standing")
            return 0
        else:
            print("Damage exceeds health")
            return 1

    def shield_window(self, amount):
        print(self.get_name(), "taking", amount, "damage. Shields:")
        shield = input()
        if shield == 0:
            print("No shields used")
        else:
            print("shield value:", shield)
            amount = int(amount)
            shield = int(shield)
            amount = amount - shield
            if amount < 0:
                amount = 0
        return amount

    def assign_damage(self, amount):
        self.damage = self.damage + amount

    def check_health(self):
        if self.health > self.damage:
            return 1
        else:
            return 0


class EventCard(Card):
    def __init__(self, name, text, traits, cost, faction, loyalty, shields, unique):
        super().__init__(name, text, traits, cost, faction, loyalty, shields, "Event", unique)

    def print_info(self):
        if self.unique:
            print("Name: *", self.name)
        else:
            print("Name:", self.name)
        print("Type:", self.card_type)
        print("Faction:", self.faction)
        print("Cost:", self.cost)
        print("Traits:", self.traits)
        print("Loyalty:", self.loyalty)
        print("Shields:", self.shields)
        print("Text:", self.text)


class AttachmentCard(Card):
    def __init__(self, name, text, traits, cost, faction, loyalty, shields, unique):
        super().__init__(name, text, traits, cost, faction, loyalty, shields, "Attachment", unique)

    def print_info(self):
        if self.unique:
            print("Name: *", self.name)
        else:
            print("Name:", self.name)
        print("Type:", self.card_type)
        print("Faction:", self.faction)
        print("Cost:", self.cost)
        print("Traits:", self.traits)
        print("Loyalty:", self.loyalty)
        print("Shields:", self.shields)
        print("Text:", self.text)


class SupportCard(Card):
    def __init__(self, name, text, traits, cost, faction, loyalty, unique):
        super().__init__(name, text, traits, cost, faction, loyalty, 0, "Support", unique)

    def print_info(self):
        if self.unique:
            print("Name: *", self.name)
        else:
            print("Name:", self.name)
        print("Type:", self.card_type)
        print("Faction:", self.faction)
        print("Cost:", self.cost)
        print("Traits:", self.traits)
        print("Loyalty:", self.loyalty)
        print("Shields:", self.shields)
        print("Text:", self.text)


class TokenCard(Card):
    def __init__(self, name, text, traits, faction, attack, health):
        super().__init__(name, text, traits, -1, faction, "Common", 0, "Token", False)
        self.attack = attack
        self.health = health
        self.damage = 0
        self.command = 0

    def get_attack(self):
        return self.attack

    def get_health(self):
        return self.health

    def get_damage(self):
        return self.damage

    def get_command(self):
        return self.command

    def damage_card(self, amount):
        amount = self.shield_window(amount)
        self.assign_damage(amount)
        if self.check_health():
            print("Card still standing")
            return 0
        else:
            print("Damage exceeds health")
            return 1

    def shield_window(self, amount):
        print(self.get_name(), "taking", amount, "damage. Shields:")
        shield = input()
        if shield == 0:
            print("No shields used")
        else:
            print("shield value:", shield)
            amount = int(amount)
            shield = int(shield)
            amount = amount - shield
            if amount < 0:
                amount = 0
        return amount

    def assign_damage(self, amount):
        self.damage = self.damage + amount

    def check_health(self):
        if self.health > self.damage:
            return 1
        else:
            return 0

    def print_info(self):
        print("Name:", self.name)
        print("Type:", self.card_type)
        print("Faction:", self.faction)
        print("Cost:", self.cost)
        print("Traits:", self.traits)
        print("Loyalty:", self.loyalty)
        print("Text:", self.text, "\nStats:", self.attack, "Attack,", self.health, "Health")


class PlanetCard:
    def __init__(self, name, text, cards, resources, red, blue, green):
        self.name = name
        self.text = text
        self.cards = cards
        self.resources = resources
        self.red = red
        self.blue = blue
        self.green = green

    def get_name(self):
        return self.name

    def get_text(self):
        return self.text

    def get_resources(self):
        return self.resources

    def get_cards(self):
        return self.cards

    def get_red(self):
        return self.red

    def get_blue(self):
        return self.blue

    def get_green(self):
        return self.green

    def print_info(self):
        print("Name:", self.name)
        print("Text:", self.text)
        print("Command:", self.resources, "resource(s),", self.cards, "card(s)")
        print("Icons:")
        if self.red:
            print("Red")
        if self.blue:
            print("Blue")
        if self.green:
            print("Green")
