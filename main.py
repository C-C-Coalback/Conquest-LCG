# GIT REPO IS https://github.com/C-C-Coalback/Conquest-LCG.git

import CardClasses
import PlanetCardsInit
import OrksCardsInit
import FindCard
import DeckHandling
import FindDeck
import PlayerClass
import random

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


def init_player(player):
    warlord = player.get_headquarters()[0]
    player.shuffle_deck()
    print(warlord.get_starting_resources(), warlord.get_starting_cards())
    if player.add_resources(warlord.get_starting_resources()) == 0:
        print("Success in adding resources", player_one.get_resources())
    for i in range(warlord.get_starting_cards()):
        player.draw_card()
    return player


player_one = PlayerClass.Player()

holder = input("Enter: ")
if holder == "c":
    DeckHandling.create_deck()
elif holder == "l":
    deck_string = FindDeck.find_deck()
    FindDeck.load_deck(deck_string, player_one)
    player_one.shuffle_deck()
    player_one.print_deck()
elif holder == "":
    planets_in_play = create_planets(planet_array)
    player_one.init_planets_in_game(planets_in_play)
    FindDeck.load_deck("#Nazdreg#Nazdreg's Flash Gitz#Nazdreg's Flash Gitz#Nazdreg's Flash Gitz"
                       "#Nazdreg's Flash Gitz#Kraktoof Hall#Bigga is Betta"
                       "#Bigga is Betta#Cybork Body", player_one)
    player_one = init_player(player_one)
    card_name_to_find = input("Enter card name to play:")
    return_value = player_one.find_card_in_hand(card_name_to_find)
    if return_value != -1:
        print("Card found at position:", return_value)
        temp_object = FindCard.find_card(player_one.get_cards()[return_value])
        planet_to_play_card = input("Select planet to play the card at:")
        planet_position = player_one.search_planets_in_game(planet_to_play_card)
        if planet_position != -1:
            print("Planet", planet_to_play_card, "is at position", planet_position)
            player_one.play_card(temp_object, planet_position + 1)
            player_one.print_cards_in_play()
            player_one.print_hand()
            player_one.remove_card_from_hand(return_value)
            player_one.print_hand()
            print("New bit:", player_one.get_cards_in_play()[planet_position + 1][0].get_name())
            damage = input("How much damage to deal:")
            if player_one.get_cards_in_play()[planet_position + 1][0].damage_card(damage):
                player_one.print_cards_in_play()
                stupid_object_holder = player_one.get_cards_in_play()[planet_position + 1][0].get_name()
                player_one.discard_card(stupid_object_holder)
                player_one.remove_card_from_play(planet_position, 0)
                player_one.print_cards_in_play()
                player_one.print_discard()

    '''
    player_one.shuffle_deck()
    player_one.draw_card()
    if player_one.add_resources(7) == 0:
        print("Success in adding resources", player_one.get_resources())
    planet_id_temp = 4
    temp_object = FindCard.find_card(player_one.get_cards()[0])
    print(temp_object.get_name())
    return_value = player_one.play_card(temp_object, planet_id_temp)
    player_one.print_cards_in_play()
'''
# print_info_card()

# print_info_planet()
