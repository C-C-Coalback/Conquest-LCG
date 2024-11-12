import random
import copy
import FindCard
import pygame
from Inits import PlanetCardsInit

class Player:
    def __init__(self, name, number):
        self.number = number
        self.name_player = name
        self.has_initiative = True
        self.has_turn = True
        self.resources = 0
        self.cards = []
        self.victory_display = []
        self.icons_gained = [0, 0, 0]
        self.headquarters = []
        self.deck = []
        self.discard = []
        self.cards_in_play = [[] for _ in range(8)]
        self.images_on_screen = [[] for _ in range(11)]
        self.position_images = [[] for _ in range(11)]
        #i_o_s[0-6] = "Cards at Planets"
        #i_o_s[7] = "Hand"
        #i_o_s[8] = "HQ"
        #i_o_s[9] = "Top Discard"
        #i_o_s[10] = "Victory Display"

    def get_has_turn(self):
        return self.has_turn

    def get_has_initiative(self):
        return self.has_initiative

    def get_name_player(self):
        return self.name_player

    def get_position_images(self):
        return self.position_images

    def get_images_on_screen(self):
        return self.images_on_screen

    def get_number(self):
        return self.number

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

    def get_discard(self):
        return self.discard

    def toggle_turn(self):
        if self.has_turn:
            self.has_turn = False
        else:
            self.has_turn = True

    def toggle_initiative(self):
        if self.has_initiative:
            self.has_initiative = False
        else:
            self.has_initiative = True

    def get_cards_in_play(self):
        return self.cards_in_play

    def get_planet_name_given_position(self, planet_id):
        return self.cards_in_play[0][planet_id]

    def init_planets_in_game(self, planets_in_game):
        for j in range(len(planets_in_game)):
            self.cards_in_play[0].append(planets_in_game[j])
            print(self.cards_in_play[0])

    def search_planets_in_game(self, planet_name):
        for j in range(len(self.cards_in_play[0])):
            if self.cards_in_play[0][j] == planet_name:
                print("Planet found")
                return j
        print("Planet not found")
        return -1

    def print_cards_in_play(self):
        print("No of planets:", len(self.cards_in_play[0]))
        for i in range(len(self.cards_in_play[0])):
            print("Cards at planet:", self.cards_in_play[0][i])
            if not self.cards_in_play[i + 1]:
                print("None")
            for j in range(len(self.cards_in_play[i + 1])):
                print(self.cards_in_play[i + 1][j].get_name())

    def pygame_print_cards_in_play(self, game_screen):
        print("No of planets:", len(self.cards_in_play[0]))
        x_first_planet = 60
        y_first_planet = 230
        x_increment = 62
        y_increment = -88
        if self.number == 1:
            y_first_planet = 385
            y_increment = 88
        for i in range(len(self.cards_in_play[0])):
            print("Cards at planet:", self.cards_in_play[0][i])
            x_current_planet = x_first_planet + (i * 165)
            y_current_planet = y_first_planet
            if not self.cards_in_play[i + 1]:
                print("None")
            for j in range(len(self.cards_in_play[i + 1])):
                print(self.cards_in_play[i + 1][j].get_name())
                card_string = self.cards_in_play[i + 1][j].get_name()
                for letter in card_string:
                    if letter == " ":
                        card_string = card_string.replace(letter, "_")
                card_image_name = "ResizedImages/" + card_string + ".jpg"
                card_image = pygame.image.load(card_image_name).convert()
                game_screen.blit(card_image, (x_current_planet, y_current_planet))
                # pygame.display.flip()
                x_current_planet = x_current_planet + x_increment
                if x_current_planet > x_first_planet + 165 * i + x_increment:
                    x_current_planet = x_first_planet + 165 * i
                    y_current_planet = y_current_planet + y_increment


    def print_cards_at_planet(self, planet_id):
        for j in range(len(self.cards_in_play[planet_id + 1])):
            print(self.cards_in_play[planet_id + 1][j].get_name())

    def get_number_of_cards_at_planet(self, planet_id):
        return len(self.cards_in_play[planet_id + 1])

    def check_for_warlord(self, planet_id):
        print("Looking for warlord at:", self.cards_in_play[0][planet_id])
        if not self.cards_in_play[planet_id + 1]:
            pass
        else:
            for j in range(len(self.cards_in_play[planet_id + 1])):
                print("Card is:", self.cards_in_play[planet_id + 1][j].get_name())
                print("Check if card is a warlord.")
                if self.cards_in_play[planet_id + 1][j].get_card_type() == "Warlord":
                    print("Card is a Warlord")
                    return 1
                else:
                    print("Card is not a Warlord")
        print("Warlord is not present")
        return 0

    def check_if_units_present(self, planet_id):
        print("Checking for cards at:", self.cards_in_play[0][planet_id])
        if not self.cards_in_play[planet_id + 1]:
            print("No cards present.")
            return 0
        print("Cards present.")
        return 1

    def count_command_at_planet(self, planet_id):
        command = 0
        for i in range(len(self.cards_in_play[planet_id])):
            print(self.cards_in_play[planet_id][i].get_command())
            if self.cards_in_play[planet_id][i].get_ready():
                command += self.cards_in_play[planet_id][i].get_command()
        return command

    def capture_planet(self, planet_id):
        planet_name = self.cards_in_play[0][planet_id]
        print("Attempting to capture planet.")
        print("Planet to capture:", planet_name)
        planet_cards = PlanetCardsInit.planet_cards_init()
        i = 0
        while planet_cards[i].get_name() != "FINAL CARD":
            if planet_cards[i].get_name() == planet_name:
                self.victory_display.append(planet_cards[i])
                self.print_victory_display()
                self.print_icons_on_captured()
                return 0
            else:
                i += 1
        return -1

    def retreat_unit(self, planet_id, unit_id):
        # print("Name of card:", self.cards_in_play[planet_id + 1][unit_id].get_name())
        self.headquarters.append(copy.deepcopy(self.cards_in_play[planet_id + 1][unit_id]))
        del self.cards_in_play[planet_id + 1][unit_id]

    def retreat_combat_window(self, planet_id):
        done_retreating = False
        while not done_retreating:
            retreat_a_unit = input(self.get_name_player() + " Retreat unit? (y/n)")
            if retreat_a_unit == "n":
                done_retreating = True
            elif retreat_a_unit == "y":
                unit_name = input("Enter name of unit to retreat with")
                unit_pos = self.search_card_at_planet(unit_name, planet_id)
                if unit_pos == -1:
                    print("Unit not found")
                else:
                    self.exhaust_given_pos(planet_id, unit_pos)
                    self.retreat_unit(planet_id, unit_pos)


    def pygame_retreat_combat_window(self, planet_id, game_screen):
        done_retreating = False
        while not done_retreating:
            retreat_a_unit = input(self.get_name_player() + " Retreat unit? (y/n)")
            if retreat_a_unit == "n":
                done_retreating = True
            elif retreat_a_unit == "y":
                unit_name = input("Enter name of unit to retreat with")
                unit_pos = self.search_card_at_planet(unit_name, planet_id)
                if unit_pos == -1:
                    print("Unit not found")
                else:
                    self.exhaust_given_pos(planet_id, unit_pos)
                    self.retreat_unit(planet_id, unit_pos)


    def retreat_all_at_planet(self, planet_id):
        while self.cards_in_play[planet_id + 1]:
            self.retreat_unit(planet_id, 0)
        self.print_cards_at_planet(planet_id + 1)
        self.print_headquarters()

    def retreat_warlord(self):
        for i in range(len(self.cards_in_play[0])):
            if not self.cards_in_play[i + 1]:
                pass
            for j in range(len(self.cards_in_play[i + 1])):
                if self.cards_in_play[i + 1][j].get_card_type() == "Warlord":
                    self.retreat_unit(i, j)

    def print_victory_display(self):
        print("Cards in victory display:")
        for i in range(len(self.victory_display)):
            print(self.victory_display[i].get_name())

    def print_icons_on_captured(self):
        total_icons = [0, 0, 0]
        for i in range(len(self.victory_display)):
            if self.victory_display[i].get_red():
                total_icons[0] += 1
            if self.victory_display[i].get_blue():
                total_icons[1] += 1
            if self.victory_display[i].get_green():
                total_icons[2] += 1
        print("Total Icons:", total_icons)

    def find_card_in_hand(self, card_name_to_find):
        for i in range(len(self.cards)):
            if self.cards[i] == card_name_to_find:
                print("Card found")
                return i
        print("Card not found")
        return -1

    def search_card_at_planet(self, card_name, planet_id):
        for i in range(len(self.cards_in_play[planet_id + 1])):
            if self.cards_in_play[planet_id + 1][i].get_name() == card_name:
                print("Card found:", self.cards_in_play[planet_id + 1][i].get_name(),
                      "position:", i)
                confirm = input("Confirm card selection.(y/n)")
                if confirm == "y":
                    return i
        return -1

    def exhaust_given_pos(self, planet_id, unit_id):
        self.cards_in_play[planet_id + 1][unit_id].exhaust_card()

    def check_warlord_given_pos(self, planet_id, unit_id):
        if self.cards_in_play[planet_id + 1][unit_id].get_card_type() == "Warlord":
            return True
        return False

    def ready_given_pos(self, planet_id, unit_id):
        self.cards_in_play[planet_id + 1][unit_id].ready_card()

    def ready_all_at_planet(self, planet_id):
        for i in range(len(self.cards_in_play[planet_id + 1])):
            self.ready_given_pos(planet_id, i)

    def ready_all_in_headquarters(self):
        for i in range(len(self.headquarters)):
            self.headquarters[i].ready_card()

    def ready_all_in_play(self):
        for i in range(len(self.cards_in_play[0])):
            self.ready_all_at_planet(i)
        self.ready_all_in_headquarters()

    def check_ready_pos(self, planet_id, unit_id):
        return self.cards_in_play[planet_id + 1][unit_id].get_ready()

    def get_attack_given_pos(self, planet_id, unit_id):
        attack_value = self.cards_in_play[planet_id + 1][unit_id].get_attack()
        return attack_value

    def get_shields_given_pos(self, pos_in_hand):
        shield_card_name = self.cards[pos_in_hand]
        card_object = FindCard.find_card(shield_card_name)
        return card_object.get_shields()

    def assign_damage_to_pos(self, planet_id, unit_id, damage):
        damage_too_great = self.cards_in_play[planet_id + 1][unit_id].damage_card(self, damage)
        return damage_too_great

    def print_state_of_unit(self, planet_id, unit_id):
        print("Name:", self.cards_in_play[planet_id + 1][unit_id].get_name())
        if self.cards_in_play[planet_id + 1][unit_id].get_ready():
            print("Ready")
        else:
            print("Exhausted")
        print("Damage:", self.cards_in_play[planet_id + 1][unit_id].get_damage())

    def commit_warlord_to_planet(self, planet_id):
        headquarters_list = self.get_headquarters()
        for i in range(len(headquarters_list)):
            if headquarters_list[i].get_card_type() == "Warlord":
                print(headquarters_list[i].get_name())
                self.cards_in_play[planet_id].append(copy.deepcopy(headquarters_list[i]))
                self.headquarters.remove(headquarters_list[i])
                self.commit_units_to_planet(planet_id)
                return 0
        return -1

    def commit_units_to_planet(self, planet_id):
        headquarters_list = self.get_headquarters()
        i = 0
        while i < len(headquarters_list):
            print("here", headquarters_list[i].get_name())
            if headquarters_list[i].get_card_type() == "Army" or headquarters_list[i].get_card_type() == "Token":
                print(headquarters_list[i].get_name())
                headquarters_list[i].exhaust_card()
                self.cards_in_play[planet_id].append(copy.deepcopy(headquarters_list[i]))
                self.headquarters.remove(headquarters_list[i])
                i = i - 1
            i = i + 1

    def play_card(self, card_to_play, planet_id):
        if FindCard.check_card_type(card_to_play, "Army"):
            if self.spend_resources(card_to_play.get_cost()) == 0:
                self.cards_in_play[planet_id].append(copy.deepcopy(card_to_play))
                self.cards.remove(card_to_play.get_name())
                print("Played card")
                return 0
            else:
                print("Insufficient resources")
                return -1
        elif FindCard.check_card_type(card_to_play, "Support"):
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

    def deploy_turn(self):
        play_card = input(self.get_name_player() + " play card? 'y' or 'p' to play, 'pass' to pass")
        if play_card == "p" or play_card == "y":
            card_name = input("Enter card name to play:")
            card_position = self.find_card_in_hand(card_name)
            if card_position == -1:
                print("Card not found in hand.")
                return self.deploy_turn()
            else:
                planet_name = input("Enter planet name to play card at:")
                pos = self.search_planets_in_game(planet_name)
                if pos == -1:
                    print("Planet not found.")
                    return self.deploy_turn()
                else:
                    print("Planet found.")
                    print("Attempting to play card.")
                    object_holder = FindCard.find_card(self.get_cards()[card_position])
                    self.play_card(object_holder, pos + 1)
                    self.print_cards_in_play()
                    return False
        elif play_card == "pass":
            return True
        else:
            print("Command unrecognised.")
            return self.deploy_turn()

    def pygame_deploy_turn(self, card_position, planet_id):
        print("Deploy unit to planet")

    def remove_card_from_play(self, planet_num, card_pos):
        # card_object = self.cards_in_play[planet_num + 1][card_pos]
        # self.discard_object(card_object)
        del self.cards_in_play[planet_num + 1][card_pos]

    def add_card_name_to_discard(self, card_name):
        self.discard.append(card_name)

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

    def remove_card_from_hand(self, card_pos):
        del self.cards[card_pos]

    def discard_card_from_hand(self, card_pos):
        self.discard.append(self.cards[card_pos])
        del self.cards[card_pos]

    def print_hand(self):
        print("Cards in hand:")
        for i in range(len(self.cards)):
            print(self.cards[i])

    def pygame_print_hand(self, game_screen):
        hand = self.get_cards()
        x_c = 300
        y_c = 595
        increment = 80
        if self.number == 2:
            x_c = 200
            y_c = 25
            increment = 80
        for i in range(len(hand)):
            card_image_name = "ResizedImages/" + hand[i] + ".jpg"
            for letter in card_image_name:
                if letter == " ":
                    card_image_name = card_image_name.replace(letter, "_")
            card_image = pygame.image.load(card_image_name).convert()
            game_screen.blit(card_image, (x_c, y_c))
            x_c += increment

    def pygame_print_hq(self, game_screen):
        hq = self.get_headquarters()
        x_c = 300
        y_c = 500
        increment = 80
        if self.number == 2:
            x_c = 300
            y_c = 125
            increment = 80
        for i in range(len(hq)):
            card_image_name = "ResizedImages/" + hq[i].get_name() + ".jpg"
            for letter in card_image_name:
                if letter == " ":
                    card_image_name = card_image_name.replace(letter, "_")

            card_image = pygame.image.load(card_image_name).convert()
            game_screen.blit(card_image, (x_c, y_c))
            x_c += increment

    def print_deck(self):
        for i in range(len(self.deck)):
            print(self.deck[i])

    def print_headquarters(self):
        print("Headquarters:")
        for i in range(len(self.headquarters)):
            try:
                print(self.headquarters[i].get_name())
            except AttributeError:
                print("Attribute error")
                print(self.headquarters[i])

    def print_discard(self):
        for i in range(len(self.discard)):
            print(self.discard[i])

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
