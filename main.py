# GIT REPO IS https://github.com/C-C-Coalback/Conquest-LCG.git

import CardClasses
import PlanetCardsInit
import OrksCardsInit
import FindCard
import DeckHandling
import FindDeck
import PlayerClass
import random

#from PlayerClass import Player

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


def deploy_phase(round_number, p_one, p_two):
    p_one_passed = False
    p_two_passed = False
    print("deploy:", round_number)
    print("Hand of p_one:")
    p_one.print_hand()
    while not p_one_passed or not p_two_passed:
        if not p_one_passed:
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
                p_one_passed = True

        if not p_two_passed:
            play_card = input("Play card? 'y' or 'p' to play, 'pass' to pass")
            if play_card == "p" or play_card == "y":
                card_name = input("Enter card name to play:")
                card_position = p_two.find_card_in_hand(card_name)
                if card_position == -1:
                    print("Card not found in hand.")
                else:
                    planet_name = input("Enter planet name to play card at:")
                    pos = p_two.search_planets_in_game(planet_name)
                    if pos == -1:
                        print("Planet not found.")
                    else:
                        print("Planet found.")
                        print("Attempting to play card.")
                        object_holder = FindCard.find_card(p_two.get_cards()[card_position])
                        p_two.play_card(object_holder, pos + 1)
                        p_two.print_cards_in_play()
            elif play_card == "pass":
                p_two_passed = True


def resolve_command_struggle(planet_num, p_one, p_two):
    player_one_command = p_one.count_command_at_planet(planet_num)
    player_two_command = p_two.count_command_at_planet(planet_num)
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


def command_phase(round_number, p_one, p_two):
    planet_array2 = PlanetCardsInit.planet_cards_init()
    planet_name = input("Choose a planet to send the Warlord to:")
    pos = p_one.search_planets_in_game(planet_name)
    if pos == -1:
        print("Planet not found")
    else:
        print("Attempting to move Warlord")
        p_one.move_warlord_to_planet(pos + 1)
    p_one.print_cards_in_play()
    p_one.print_headquarters()
    planet_name = input("Choose a planet to send the Warlord to:")
    pos = p_two.search_planets_in_game(planet_name)
    if pos == -1:
        print("Planet not found")
    else:
        print("Attempting to move Warlord")
        p_two.move_warlord_to_planet(pos + 1)
    p_two.print_cards_in_play()
    p_two.print_headquarters()
    print("command:", round_number)
    planet_num = round_number
    planets_counted = 0
    c_res = [0, 0, 0, 0]
    while planet_num < 7 and planets_counted < 5:
        result = resolve_command_struggle(planet_num, p_one, p_two)
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
        elif result == 2:
            planet_name = p_two.get_planet_name_given_position(planet_num - 1)
            print("Planet name:", planet_name)
            for i in range(len(planet_array2)):
                if planet_name == planet_array2[i].get_name():
                    print("Resources of", planet_name, planet_array2[i].get_resources())
                    print("Cards of", planet_name, planet_array2[i].get_cards())
                    c_res[2] += planet_array2[i].get_resources()
                    c_res[3] += planet_array2[i].get_cards()
                    print("test", c_res[2])
        planets_counted += 1
        planet_num += 1
    print(c_res[0], c_res[1], c_res[2], c_res[3])
    print("Player one gets", c_res[0], "resources from command struggle")
    p_one.add_resources(c_res[0])
    print("Player one gets", c_res[1], "cards from command struggle")
    for i in range(c_res[1]):
        p_one.draw_card()
    print("Player two gets", c_res[2], "resources from command struggle")
    p_two.add_resources(c_res[2])
    print("Player two gets", c_res[3], "cards from command struggle")
    for i in range(c_res[3]):
        p_two.draw_card()
    # player two will need the same idea but with c_res[2] and c_res[3]
    print(p_one.get_resources())
    print(p_one.get_cards())
    print(p_two.get_resources())
    print(p_two.get_cards())

def unit_attacks_unit(att, defe, planet_id, att_pos, defe_pos):
    attack_value = att.get_attack_given_pos(planet_id, att_pos)
    damage_too_great = defe.assign_damage_to_pos(planet_id, defe_pos, attack_value)
    if damage_too_great:
        print("Card must be discarded")
        input("Hold attack")
        return 1
    input("Hold attack")
    return 0

def combat_turn(attacker, defender, planet_id):
    attacker_name = input("Enter unit to attack with or 'p' to pass")
    if attacker_name == "p":
        return True
    pos_attacker = attacker.search_card_at_planet(attacker_name, planet_id)
    print("position of unit:", pos_attacker)
    if pos_attacker != -1:
        if attacker.check_ready_pos(planet_id, pos_attacker):
            attacker.exhaust_given_pos(planet_id, pos_attacker)
            attacker.print_state_of_unit(planet_id, pos_attacker)
            defender_name = input("Enter unit to declare as defender")
            pos_defender = defender.search_card_at_planet(defender_name, planet_id)
            if pos_defender != -1:
                defender.print_state_of_unit(planet_id, pos_defender)
                input("hold")
                unit_dead = unit_attacks_unit(attacker, defender, planet_id, pos_attacker, pos_defender)
                defender.print_state_of_unit(planet_id, pos_defender)
                if unit_dead == 1:
                    defender.add_card_name_to_discard(defender_name)
                    defender.remove_card_from_play(planet_id, pos_defender)
                    defender.print_cards_at_planet(planet_id)
                    defender.print_discard()
                input("hold")
                return False
        else:
            print("Attacker not ready")
    #return to decide if player passed
    return combat_turn(attacker, defender, planet_id)

def combat_round(p_one, p_two, planet_id):
    p_one_passed = False
    p_two_passed = False
    while p_one_passed == False or p_two_passed == False:
        p_one_passed = combat_turn(p_one, p_two, planet_id)
        p_two_passed = combat_turn(p_two, p_one, planet_id)

def resolve_battle(p_one, p_two, planet_id, first_planet):
    planet_name = p_two.get_planet_name_given_position(planet_id - 1)
    player_one_check = p_one.check_if_units_present(planet_id)
    player_two_check = p_two.check_if_units_present(planet_id)
    while player_one_check and player_two_check:
        print("Both have units present. Combat round begins at:", planet_name)
        print("Player one units:")
        player_one.print_cards_at_planet(planet_id)
        print("Player two units:")
        player_two.print_cards_at_planet(planet_id)
        combat_round(player_one, player_two, planet_id)
        player_one_check = p_one.check_if_units_present(planet_id)
        player_two_check = p_two.check_if_units_present(planet_id)
        player_one.ready_all_at_planet(planet_id)
        player_two.ready_all_at_planet(planet_id)
    if player_one_check and not player_two_check:
        print("First player has units, second player doesn't")
        print("First player wins the battle")
        if first_planet:
            input("Hold, retreat from winning battle")
            player_one.retreat_all_at_planet(planet_id)
            player_one.capture_planet(planet_id)
    elif not player_one_check and player_two_check:
        print("Second player has units, first player doesn't")
        print("Second player wins the battle")
        if first_planet:
            player_two.retreat_all_at_planet(planet_id)
            player_two.capture_planet(planet_id)
    elif not player_one_check and not player_two_check:
        print("Neither player has units")

def check_for_battle(p_one, p_two, planet_id, first_planet):
    planet_name = p_two.get_planet_name_given_position(planet_id - 1)
    if first_planet:
        print("First planet. Resolve battle at:", planet_name)
        resolve_battle(p_one, p_two, planet_id - 1, first_planet)
    elif not first_planet:
        print("Not first planet. Check for Warlords at:", planet_name)
        if p_one.check_for_warlord(planet_id - 1):
            print("Battle is resolved at:", planet_name)
            resolve_battle(p_one, p_two, planet_id - 1, first_planet)
        elif p_two.check_for_warlord(planet_id - 1):
            print("Battle is resolved at:", planet_name)
            resolve_battle(p_one, p_two, planet_id - 1, first_planet)

def combat_phase(round_number, p_one, p_two):
    print("combat:", round_number)
    index = round_number
    planets_counted = 0
    first_planet = True
    while planets_counted < 5 and index < 7:
        check_for_battle(p_one, p_two, index, first_planet)
        first_planet = False
        index += 1
        planets_counted += 1
    p_one.retreat_warlord()
    p_two.retreat_warlord()
    p_one.print_headquarters()
    p_two.print_headquarters()


def hq_phase(round_number, p_one, p_two):
    print("hq:", round_number)
    p_one.ready_all_in_play()
    p_two.ready_all_in_play()
    p_one.add_resources(4)
    p_two.add_resources(4)
    p_one.draw_card()
    p_one.draw_card()
    p_two.draw_card()
    p_two.draw_card()


def game_round(round_number, p_one, p_two):
    deploy_phase(round_number, p_one, p_two)
    command_phase(round_number, p_one, p_two)
    combat_phase(round_number, p_one, p_two)
    hq_phase(round_number, p_one, p_two)


def play_game(p_one, p_two):
    deck_s = FindDeck.find_deck()
    FindDeck.load_deck(deck_s, p_one)
    p_one.shuffle_deck()
    deck_s = FindDeck.find_deck()
    FindDeck.load_deck(deck_s, p_two)
    p_two.shuffle_deck()
    planets_in_play_list = create_planets(planet_array)
    player_one.init_planets_in_game(planets_in_play_list)
    player_two.init_planets_in_game(planets_in_play_list)
    init_player(p_one)
    init_player(p_two)
    game_round(1, p_one, p_two)


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
player_two = PlayerClass.Player()

holder = input("Enter: ")
if holder == "c":
    DeckHandling.create_deck()
elif holder == "l":
    deck_string = FindDeck.find_deck()
    FindDeck.load_deck(deck_string, player_one)
    player_one.shuffle_deck()
    player_one.print_deck()
elif holder == "p":
    play_game(player_one, player_two)