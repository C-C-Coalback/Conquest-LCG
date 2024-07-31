# GIT REPO IS https://github.com/C-C-Coalback/Conquest-LCG.git

import CardClasses
import PlanetCardsInit
import OrksCardsInit
import FindCard
import DeckHandling
import FindDeck
import PlayerClass
import random
import copy

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


def create_planets(planet_array_objects):
    planet_names = []
    for i in range(10):
        string = planet_array_objects[i].get_name()
        planet_names.append(string)
    random.shuffle(planet_names)
    planets_in_play_return = []
    for i in range(7):
        planets_in_play_return.append(planet_names[i])
    return planets_in_play_return


def play_card(player, card_to_play, planet_id, cards_at_planet_array):
    if FindCard.check_card_type(card_to_play, "No"):
        print(player.get_resources())
        if player.spend_resources(card_to_play.get_cost()) == 0:
            cards_at_planet_array[planet_id].append(copy.deepcopy(card_to_play))
            print("Played card")
            return cards_at_planet_array
        else:
            print("Insufficient resources.")
            return cards_at_planet_array
    elif FindCard.check_card_type(card_to_play, "Army"):
        print(player.get_resources())
        if player.spend_resources(card_to_play.get_cost()) == 0:
            player.add_to_hq(card_to_play)
            print("Played card to HQ")
            for i in range(len(player.get_headquarters())):
                if player.get_headquarters()[i] == "Nazdreg":
                    print("Nazdreg")
                else:
                    print(player.get_headquarters()[i].get_name())
            return cards_at_planet_array
        else:
            print("Insufficient resources.")
            return cards_at_planet_array
    else:
        print("Not an army/support card")
        return cards_at_planet_array


player_one = PlayerClass.Player()
cards_in_play_player_one = [[] for i in range(8)]

holder = input("Enter: ")
if holder == "c":
    DeckHandling.create_deck()
elif holder == "l":
    deck_string = FindDeck.find_deck()
    FindDeck.load_deck(deck_string, player_one)
    player_one.shuffle_deck()
    player_one.print_deck()
elif holder == "":
    FindDeck.load_deck("#Nazdreg#Nazdreg's Flash Gitz#Nazdreg's Flash Gitz#Nazdreg's Flash Gitz"
                       "#Nazdreg's Flash Gitz#Kraktoof Hall#Bigga is Betta"
                       "#Bigga is Betta#Cybork Body", player_one)
    player_one.shuffle_deck()
    player_one.draw_card()
    if player_one.add_resources(7) == 0:
        print("Success in adding resources", player_one.get_resources())
    planets_in_play = create_planets(planet_array)
    # print(planets_in_play)
    for j in range(len(planets_in_play)):
        cards_in_play_player_one[0].append(planets_in_play[j])
        # print(cards_in_play_player_one[0])
    # cards_in_play_player_one[1].append(player_one.get_cards()[0])
    # planet_id = input("Select planet number:")
    planet_id_temp = 4
    temp_object = FindCard.find_card(player_one.get_cards()[0])
    print(temp_object.get_name())
    cards_in_play_player_one = play_card(player_one, temp_object, planet_id_temp, cards_in_play_player_one)
    for i in range(len(cards_in_play_player_one[planet_id_temp])):
        print(cards_in_play_player_one[planet_id_temp][i].get_name())
    # cards_in_play_player_one[1].append(copy.deepcopy(temp_object))
    # print(cards_in_play_player_one[1][0].get_name())

# print_info_card()

# print_info_planet()
