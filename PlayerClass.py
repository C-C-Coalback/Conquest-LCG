import random
import copy
import FindCard


class Player:
    def __init__(self):
        self.resources = 0
        self.cards = []
        self.victory_display = []
        self.icons_gained = [0, 0, 0]
        self.headquarters = []
        self.deck = []
        self.cards_in_play = [[] for _ in range(8)]

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

    def init_planets_in_game(self, planets_in_game):
        for j in range(len(planets_in_game)):
            self.cards_in_play[0].append(planets_in_game[j])
            print(self.cards_in_play[0])

    def print_cards_in_play(self):
        print("No of planets:", len(self.cards_in_play[0]))
        for i in range(len(self.cards_in_play[0])):
            print("Cards at planet:", self.cards_in_play[0][i])
            if not self.cards_in_play[i + 1]:
                print("None")
            for j in range(len(self.cards_in_play[i + 1])):
                print(self.cards_in_play[i + 1][j].get_name())

    def play_card(self, card_to_play, planet_id):
        if FindCard.check_card_type(card_to_play, "Army"):
            print(self.get_resources())
            if self.spend_resources(card_to_play.get_cost()) == 0:
                self.cards_in_play[planet_id].append(copy.deepcopy(card_to_play))
                print("Played card")
                return 0
            else:
                print("Insufficient resources")
                return -1
        elif FindCard.check_card_type(card_to_play, "Support"):
            print(self.get_resources())
            if self.spend_resources((card_to_play.get_cost())) == 0:
                self.add_to_hq(card_to_play)
                print("Played card to HQ")
                for i in range(len(self.get_headquarters())):
                    print(self.get_headquarters()[i].get_name())
                return 0
            else:
                print("Insufficient resources")
                return -1
        else:
            print("Not an army/support card")
            return -1

    def add_card_to_deck(self, card_name):
        self.deck.append(card_name)

    def add_to_hq(self, card_object):
        self.headquarters.append(copy.deepcopy(card_object))

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

    def add_resources(self, amount):
        if amount > 0:
            self.resources += amount
            return 0
        else:
            print("Attempted to add", amount, "resources, may be an error")
            return -1

    def spend_resources(self, amount):
        if amount > self.resources:
            print("Attempted to spend more resources than you have.")
            return -1
        else:
            self.resources -= amount
            return 0
