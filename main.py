# GIT REPO IS https://github.com/C-C-Coalback/Conquest-LCG.git

import CardClasses
import PlanetCardsInit
import OrksCardsInit
import FindCard
import DeckHandling
import FindDeck

snotling = CardClasses.TokenCard("Snotling", "", "Runt.", "Orks", 1, 1)

orks_card_array = OrksCardsInit.orks_cards_init()
planet_array = PlanetCardsInit.planet_cards_init()
faction_wheel = ["Astra Militarum", "Space Marines", "Tau", "Eldar",
                 "Dark Eldar", "Chaos", "Orks", "Astra Militarum", "Space Marines"]


def print_info_planet():
    planet_to_find = input("Select Planet: ")
    i = 0
    found = False
    while planet_array[i].get_resources() != -1 and not found:
        if planet_to_find == planet_array[i].get_name():
            planet_array[i].print_info()
            found = True
        else:
            i = i + 1
    if not found:
        retry = input("Planet not found. Retry? (y/n)")
        if retry == "y":
            print_info_planet()


def print_info_card():
    card_to_find = input("Select Card: ")
    card_object = FindCard.find_card(card_to_find)
    if card_object.get_shields() != -1:
        card_object.print_info()
    else:
        retry = input("Card not found. Retry? (y/n)")
        if retry == "y":
            print_info_card()


holder = input("Create_deck?")
if holder == "y":
    DeckHandling.create_deck()


# print_info_card()

# print_info_planet()


class Player:
    def __init__(self):
        self.resources = 0
        self.cards = []
        self.victory_display = []
        self.icons_gained = [0, 0, 0]
        self.headquarters = []
        self.deck = []

    def get_resources(self):
        return self.resources

    def get_cards(self):
        return self.cards

    def get_victory_display(self):
        return self.victory_display

    def get_icons_gained(self):
        return self.icons_gained

    def get_headquarters(self):
        return self.headquarters

    def get_deck(self):
        return self.deck

    def add_card_to_deck(self, card_name):
        self.deck.append(card_name)

    def print_deck(self):
        for i in range(len(self.deck)):
            print(self.deck[i])


player_one = Player()

deck_string = FindDeck.find_deck()
FindDeck.load_deck(deck_string, player_one)
player_one.print_deck()
