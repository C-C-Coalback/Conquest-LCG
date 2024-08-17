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


def deploy_phase(round_number, p_one):
    passed = False
    print("deploy:", round_number)
    print("Hand of p_one:")
    p_one.print_hand()
    while not passed:
        play_card = input("Play card? 'y' or 'p' to play, 'pass' to pass")
        if play_card == "p" or play_card == "y":
            card_name = input("Enter card name to play:")
            card_position = p_one.find_card_in_hand(card_name)
            if card_position == -1:
                print("Card not found in hand.")
            else:
                planet_name = input("Enter planet name to play card at:")
                pos = p_one.search_planets_in_game(planet_name)
                if pos == -1:
                    print("Planet not found.")
                else:
                    print("Planet found.")
                    print("Attempting to play card.")
                    object_holder = FindCard.find_card(p_one.get_cards()[card_position])
                    p_one.play_card(object_holder, pos + 1)
                    p_one.print_cards_in_play()
        elif play_card == "pass":
            passed = True


def resolve_command_struggle(planet_num, p_one):
    player_one_command = p_one.count_command_at_planet(planet_num)
    player_two_command = 0
    if player_one_command > player_two_command:
        print(player_one_command, "greater than",
              player_two_command, "at planet no", planet_num, "player one wins command")
        return 1
    elif player_two_command > player_one_command:
        print(player_two_command, "greater than",
              player_one_command, "at planet no", planet_num, "player two wins command")
        return 2
    else:
        print("command is equal")
        return 0
    pass


def command_phase(round_number, p_one):
    planet_array2 = PlanetCardsInit.planet_cards_init()
    print("command:", round_number)
    planet_num = round_number
    planets_counted = 0
    c_res = [0, 0, 0, 0]
    while planet_num < 7 and planets_counted < 5:
        result = resolve_command_struggle(planet_num, p_one)
        print("Test", result)
        if result == 1:
            planet_name = p_one.get_planet_name_given_position(planet_num - 1)
            print("Planet name:", planet_name)
            for i in range(len(planet_array2)):
                if planet_name == planet_array2[i].get_name():
                    print("Resources of", planet_name, planet_array2[i].get_resources())
                    print("Cards of", planet_name, planet_array2[i].get_cards())
                    c_res[0] += planet_array2[i].get_resources()
                    c_res[1] += planet_array2[i].get_cards()
                    print("test", c_res[0])
        planets_counted += 1
        planet_num += 1
    print(c_res[0], c_res[1], c_res[2], c_res[3])
    print("Player one gets", c_res[0], "resources from command struggle")
    p_one.add_resources(c_res[0])
    print("Player one gets", c_res[1], "cards from command struggle")
    for i in range(c_res[1]):
        p_one.draw_card()
    # player two will need the same idea but with c_res[2] and c_res[3]
    print(p_one.get_resources())
    print(p_one.get_cards())


def combat_phase(round_number, p_one):
    print("combat:", round_number)


def hq_phase(round_number, p_one):
    print("hq:", round_number)


def game_round(round_number, p_one):
    deploy_phase(round_number, p_one)
    command_phase(round_number, p_one)
    combat_phase(round_number, p_one)
    hq_phase(round_number, p_one)


def play_game(p_one):
    deck_s = FindDeck.find_deck()
    FindDeck.load_deck(deck_s, p_one)
    p_one.shuffle_deck()
    planets_in_play_list = create_planets(planet_array)
    player_one.init_planets_in_game(planets_in_play_list)
    init_player(p_one)
    game_round(1, p_one)


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
elif holder == "p":
    play_game(player_one)
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
