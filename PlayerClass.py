import random


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

    def add_to_hq(self, card_name):
        self.headquarters.append(card_name)

    def draw_card(self):
        if not self.deck:
            print("Deck is empty, you lose!")
        else:
            self.cards.append(self.deck[0])
            del self.deck[0]

    def print_hand(self):
        for i in range(len(self.cards)):
            print(self.cards[i])

    def print_deck(self):
        for i in range(len(self.deck)):
            print(self.deck[i])

    def shuffle_deck(self):
        random.shuffle(self.deck)
