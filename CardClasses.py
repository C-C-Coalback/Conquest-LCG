import ClickDetection

class Card:
    def __init__(self, name, text, traits, cost, faction, loyalty, shields, card_type, unique, image_name):
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
        self.image_name = image_name

    def get_name(self):
        return self.name

    def get_text(self):
        return self.text

    def get_traits(self):
        return self.traits

    def get_image_name(self):
        return self.image_name()

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

    def ready_card(self):
        self.ready = True

    def exhaust_card(self):
        self.ready = False


class WarlordCard(Card):
    def __init__(self, name, text, traits, faction, attack, health, bloodied_attack, bloodied_health, bloodied_text,
                 starting_resources, starting_cards, image_name):
        super().__init__(name, text, traits, -1, faction, "Signature", 0, "Warlord", False
                         , image_name)
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

    def pygame_damage_card(self, player, amount, game_screen):
        amount = self.pygame_shield_window(player, amount, game_screen)
        self.assign_damage(amount)
        if self.check_health():
            print("Card still standing")
            return 0
        else:
            print("Damage exceeds health")
            return 1

    def pygame_shield_window(self, player, amount, game_screen):
        print(self.get_name(), "taking", amount, "damage.")
        print("GOT HERE")
        while True:
            position = ClickDetection.prompt_pos_hand(player)
            if position == -1:
                print("No shields used")
                return amount
            shield = player.get_shields_given_pos(position)
            if shield == -1:
                input("Card somehow found in hand but not in database.")
            elif shield == 0:
                print("Card has no shields on it. Use something else.")
            else:
                player.discard_card_from_hand(position)
                print("shield value:", shield)
                amount = int(amount)
                shield = int(shield)
                amount = amount - shield
                if amount < 0:
                    amount = 0
            return amount

    def damage_card(self, player, amount):
        amount = self.shield_window(player, amount)
        self.assign_damage(amount)
        if self.check_health():
            print("Card still standing")
            return 0
        else:
            print("Damage exceeds health")
            return 1

    def shield_window(self, player, amount):
        print(self.get_name(), "taking", amount, "damage.")
        keep_looping = True
        shield = 0
        while keep_looping:
            shield_card = input("Enter the name of a card to shield with, or nothing to not use a shield:")
            if shield_card == "":
                keep_looping = False
            else:
                pos_hand = player.find_card_in_hand(shield_card)
                if pos_hand == -1:
                    print("Card not found in hand")
                else:
                    shield = player.get_shields_given_pos(pos_hand)
                    if shield == -1:
                        input("Card somehow found in hand but not in database.")
                    elif shield == 0:
                        input("Card has no shields on it. Use something else.")
                    else:
                        player.discard_card_from_hand(pos_hand)
                        keep_looping = False
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

    def bloody_warlord(self):
        self.damage = 0
        self.health = self.bloodied_health
        self.attack = self.bloodied_attack
        self.text = self.bloodied_text
        self.bloodied = True

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
    def __init__(self, name, text, traits, cost, faction, loyalty, attack, health, command, unique, image_name):
        super().__init__(name, text, traits, cost, faction, loyalty, 0, "Army", unique, image_name)
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

    def pygame_damage_card(self, player, amount, game_screen):
        amount = self.pygame_shield_window(player, amount, game_screen)
        self.assign_damage(amount)
        if self.check_health():
            print("Card still standing")
            return 0
        else:
            print("Damage exceeds health")
            return 1

    def pygame_shield_window(self, player, amount, game_screen):
        print(self.get_name(), "taking", amount, "damage.")
        print("GOT HERE")
        while True:
            position = ClickDetection.prompt_pos_hand(player)
            if position == -1:
                print("No shields used")
                return amount
            shield = player.get_shields_given_pos(position)
            if shield == -1:
                input("Card somehow found in hand but not in database.")
            elif shield == 0:
                print("Card has no shields on it. Use something else.")
            else:
                player.discard_card_from_hand(position)
                print("shield value:", shield)
                amount = int(amount)
                shield = int(shield)
                amount = amount - shield
                if amount < 0:
                    amount = 0
            return amount

    def damage_card(self, player, amount):
        amount = self.shield_window(player, amount)
        self.assign_damage(amount)
        if self.check_health():
            print("Card still standing")
            return 0
        else:
            print("Damage exceeds health")
            return 1

    def shield_window(self, player, amount):
        print(self.get_name(), "taking", amount, "damage.")
        shield_card = input("Enter the name of a card to shield with:")
        pos_hand = player.find_card_in_hand(shield_card)
        shield = player.get_shields_given_pos(pos_hand)
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
    def __init__(self, name, text, traits, cost, faction, loyalty, shields, unique, image_name):
        super().__init__(name, text, traits, cost, faction, loyalty, shields, "Event", unique, image_name)

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
    def __init__(self, name, text, traits, cost, faction, loyalty, shields, unique, image_name):
        super().__init__(name, text, traits, cost, faction, loyalty, shields, "Attachment", unique, image_name)

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
    def __init__(self, name, text, traits, cost, faction, loyalty, unique, image_name):
        super().__init__(name, text, traits, cost, faction, loyalty, 0, "Support", unique, image_name)

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
    def __init__(self, name, text, traits, faction, attack, health, image_name):
        super().__init__(name, text, traits, -1, faction, "Common", 0, "Token", False,
                         image_name)
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

    def pygame_damage_card(self, player, amount, game_screen):
        amount = self.pygame_shield_window(player, amount, game_screen)
        self.assign_damage(amount)
        if self.check_health():
            print("Card still standing")
            return 0
        else:
            print("Damage exceeds health")
            return 1

    def pygame_shield_window(self, player, amount, game_screen):
        print(self.get_name(), "taking", amount, "damage.")
        print("GOT HERE")
        while True:
            position = ClickDetection.prompt_pos_hand(player)
            if position == -1:
                print("No shields used")
                return amount
            shield = player.get_shields_given_pos(position)
            if shield == -1:
                input("Card somehow found in hand but not in database.")
            elif shield == 0:
                print("Card has no shields on it. Use something else.")
            else:
                player.discard_card_from_hand(position)
                print("shield value:", shield)
                amount = int(amount)
                shield = int(shield)
                amount = amount - shield
                if amount < 0:
                    amount = 0
            return amount

    def shield_window(self, player, amount):
        print(self.get_name(), "taking", amount, "damage.")
        shield_card = input("Enter the name of a card to shield with:")
        pos_hand = player.find_card_in_hand(shield_card)
        shield = player.get_shields_given_pos(pos_hand)
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
    def __init__(self, name, text, cards, resources, red, blue, green, image_name):
        self.name = name
        self.text = text
        self.cards = cards
        self.resources = resources
        self.red = red
        self.blue = blue
        self.green = green
        self.image_name = image_name

    def get_name(self):
        return self.name

    def get_image_name(self):
        return self.image_name

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
