import pygame


import ClickDetection
from Drawing import draw_all


def unit_attacks_unit(att, defe, planet_id, att_pos, defe_pos):
    attack_value = att.get_attack_given_pos(planet_id, att_pos)
    damage_too_great = defe.assign_damage_to_pos(planet_id, defe_pos, attack_value)
    if damage_too_great:
        print("Card must be discarded")
        #input("Hold attack")
        return 1
    #input("Hold attack")
    return 0

def pygame_unit_attacks_unit(att, defe, planet_id, att_pos, defe_pos, game_screen):
    attack_value = att.get_attack_given_pos(planet_id, att_pos)
    damage_too_great = defe.pygame_assign_damage_to_pos(planet_id, defe_pos, attack_value, game_screen)
    if damage_too_great:
        print("Card must be discarded")
        #input("Hold attack")
        return 1
    #input("Hold attack")
    return 0


def combat_turn(attacker, defender, planet_id):
    print(attacker.get_name_player(), '\'s turn to attack', sep='')
    attacker_name = input("Enter unit to attack with or 'p' to pass")
    if attacker_name == "p":
        return True
    pos_attacker = attacker.search_card_at_planet(attacker_name, planet_id)
    print("position of unit:", pos_attacker)
    if pos_attacker != -1:
        if attacker.check_ready_pos(planet_id, pos_attacker):
            attacker.exhaust_given_pos(planet_id, pos_attacker)
            # attacker.print_state_of_unit(planet_id, pos_attacker)
            if attacker.check_warlord_given_pos(planet_id, pos_attacker):
                option_retreat_warlord = input("Card is a Warlord. Retreat? (y/n)")
                if option_retreat_warlord == "y":
                    attacker.retreat_unit(planet_id, pos_attacker)
                    return False
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
    # return to decide if player passed
    return combat_turn(attacker, defender, planet_id)



def pygame_combat_turn(attacker, defender, planet_id, game_screen):
    print(attacker.get_name_player(), '\'s turn to attack', sep='')
    pos_attacker = ClickDetection.prompt_pos_unit_at_planet(attacker, planet_id, game_screen, pygame.Color("red"))
    if pos_attacker == -1:
        return True
    pos_defender = ClickDetection.prompt_pos_unit_at_planet(defender, planet_id, game_screen, pygame.Color("blue"))
    if pos_defender == -1:
        return pygame_combat_turn(attacker, defender, planet_id, game_screen)
    print("position of unit:", pos_attacker)
    print("SUCCESS")

    if attacker.check_ready_pos(planet_id, pos_attacker):
        attacker.exhaust_given_pos(planet_id, pos_attacker)
        defender.print_state_of_unit(planet_id, pos_defender)
        unit_dead = pygame_unit_attacks_unit(attacker, defender, planet_id, pos_attacker, pos_defender, game_screen)
        defender.print_state_of_unit(planet_id, pos_defender)
        if unit_dead == 1:
            # defender.add_card_name_to_discard(defender_name)
            if defender.check_if_warlord(planet_id, pos_defender):
                defender.bloody_warlord_given_pos(planet_id, pos_defender)
            else:
                defender.remove_card_from_play(planet_id, pos_defender)
                defender.print_cards_at_planet(planet_id)
                defender.print_discard()
        attacker.toggle_turn()
        defender.toggle_turn()
        draw_all(game_screen, attacker, defender)
        return False
    else:
        print("Attacker not ready")
    # return to decide if player passed
    return pygame_combat_turn(attacker, defender, planet_id, game_screen)



def combat_round(p_one, p_two, planet_id):
    planet_name = p_two.get_planet_name_given_position(planet_id)
    p_one_passed = False
    p_two_passed = False
    print("Both have units present. Combat round begins at:", planet_name)
    print(p_one.get_name_player(), "units:")
    p_one.print_cards_at_planet(planet_id)
    print(p_two.get_name_player(), "units:")
    p_two.print_cards_at_planet(planet_id)
    while not p_one_passed or not p_two_passed:
        p_one_passed = combat_turn(p_one, p_two, planet_id)
        p_two_passed = combat_turn(p_two, p_one, planet_id)
    p_one.ready_all_at_planet(planet_id)
    p_two.ready_all_at_planet(planet_id)
    p_one.retreat_combat_window(planet_id)
    p_two.retreat_combat_window(planet_id)

def determine_combat_initiative(p_one, p_two, planet_id):
    p_one_has_warlord = p_one.check_for_warlord(planet_id)
    p_two_has_warlord = p_two.check_for_warlord(planet_id)
    if p_one_has_warlord == p_two_has_warlord:
        return p_one.get_has_initiative()
    return p_one_has_warlord

def pygame_combat_round(p_one, p_two, planet_id, game_screen):
    planet_name = p_two.get_planet_name_given_position(planet_id)
    p_one_passed = False
    p_two_passed = False
    print("Both have units present. Combat round begins at:", planet_name)
    print(p_one.get_name_player(), "units:")
    p_one.print_cards_at_planet(planet_id)
    print(p_two.get_name_player(), "units:")
    p_two.print_cards_at_planet(planet_id)
    while not p_one_passed or not p_two_passed:
        if determine_combat_initiative(p_one, p_two, planet_id):
            p_one.set_has_turn(True)
            p_two.set_has_turn(False)
            draw_all(game_screen, p_one, p_two)
            p_one_passed = pygame_combat_turn(p_one, p_two, planet_id, game_screen)
            if p_one_passed:
                p_one.set_has_turn(False)
                p_two.set_has_turn(True)
            draw_all(game_screen, p_one, p_two)
            p_two_passed = pygame_combat_turn(p_two, p_one, planet_id, game_screen)
        else:
            p_one.set_has_turn(False)
            p_two.set_has_turn(True)
            draw_all(game_screen, p_one, p_two)
            p_two_passed = pygame_combat_turn(p_two, p_one, planet_id, game_screen)
            if p_two_passed:
                p_one.set_has_turn(True)
                p_two.set_has_turn(False)
            draw_all(game_screen, p_one, p_two)
            p_one_passed = pygame_combat_turn(p_one, p_two, planet_id, game_screen)
    p_one.ready_all_at_planet(planet_id)
    p_two.ready_all_at_planet(planet_id)
    done_retreating = False
    p_one.set_retreating(True)
    p_two.set_retreating(True)
    while not done_retreating:
        if determine_combat_initiative(p_one, p_two, planet_id):
            p_one.set_has_turn(True)
            p_two.set_has_turn(False)
            draw_all(game_screen, p_one, p_two)
            done_retreating = p_one.pygame_retreat_combat_window(planet_id, game_screen)
        else:
            p_one.set_has_turn(False)
            p_two.set_has_turn(True)
            draw_all(game_screen, p_one, p_two)
            done_retreating = p_two.pygame_retreat_combat_window(planet_id, game_screen)
        draw_all(game_screen, p_one, p_two)
    done_retreating = False
    p_one.toggle_turn()
    p_two.toggle_turn()
    draw_all(game_screen, p_one, p_two)
    while not done_retreating:
        if determine_combat_initiative(p_one, p_two, planet_id):
            p_one.set_has_turn(False)
            p_two.set_has_turn(True)
            draw_all(game_screen, p_one, p_two)
            done_retreating = p_two.pygame_retreat_combat_window(planet_id, game_screen)
        else:
            p_one.set_has_turn(True)
            p_two.set_has_turn(False)
            draw_all(game_screen, p_one, p_two)
            done_retreating = p_one.pygame_retreat_combat_window(planet_id, game_screen)
        draw_all(game_screen, p_one, p_two)
    p_one.set_retreating(False)
    p_two.set_retreating(False)
    p_one.toggle_turn()
    p_two.toggle_turn()

def resolve_planet_battle_effect(p_win, p_lose, planet_id):
    planet_name = p_win.get_planet_name_given_position(planet_id)
    print("Resolve battle ability:")
    print(planet_name)
    if planet_name == "Osus_IV":
        print("Osus IV ability")
        if p_lose.spend_resources(1) == 0:
            p_win.add_resources(1)
    elif planet_name == "Iridial":
        print("Iridial ability")
    elif planet_name == "Plannum":
        print("Plannum ability")
    elif planet_name == "Tarrus":
        print("Tarrus ability")
    elif planet_name == "Y'varn":
        print("Y'varn ability")
    elif planet_name == "Barlus":
        print("Barlus ability")
    elif planet_name == "Ferrin":
        print("Ferrin ability")
    elif planet_name == "Carnath":
        print("Carnath ability")
    elif planet_name == "Elouith":
        print("Elouith ability")
    elif planet_name == "Atrox_Prime":
        print("Atrox Prime ability")

def resolve_battle(p_one, p_two, planet_id, first_planet):
    player_one_check = p_one.check_if_units_present(planet_id)
    player_two_check = p_two.check_if_units_present(planet_id)
    while player_one_check and player_two_check:
        combat_round(p_one, p_two, planet_id)
        player_one_check = p_one.check_if_units_present(planet_id)
        player_two_check = p_two.check_if_units_present(planet_id)
    if player_one_check and not player_two_check:
        print(p_one.get_name_player(), "has units,", p_two.get_name_player(), "doesn't")
        print(p_two.get_name_player(), "wins the battle")
        if first_planet:
            input("Hold, retreat from winning battle")
            p_one.retreat_all_at_planet(planet_id)
            p_one.capture_planet(planet_id)
    elif not player_one_check and player_two_check:
        print(p_two.get_name_player(), "has units,", p_one.get_name_player(), "doesn't")
        print(p_two.get_name_player(), "wins the battle")
        if first_planet:
            p_two.retreat_all_at_planet(planet_id)
            p_two.capture_planet(planet_id)
    elif not player_one_check and not player_two_check:
        print("Neither player has units")



def pygame_resolve_battle(p_one, p_two, planet_id, first_planet, game_screen):
    player_one_check = p_one.check_if_units_present(planet_id)
    player_two_check = p_two.check_if_units_present(planet_id)
    while player_one_check and player_two_check:
        pygame_combat_round(p_one, p_two, planet_id, game_screen)
        draw_all(game_screen, p_one, p_two)
        player_one_check = p_one.check_if_units_present(planet_id)
        player_two_check = p_two.check_if_units_present(planet_id)
    if player_one_check and not player_two_check:
        print(p_one.get_name_player(), "has units,", p_two.get_name_player(), "doesn't")
        print(p_two.get_name_player(), "wins the battle")
        resolve_planet_battle_effect(p_one, p_two, planet_id)
        if first_planet:
            p_one.retreat_all_at_planet(planet_id)
            p_one.capture_planet(planet_id)
    elif not player_one_check and player_two_check:
        print(p_two.get_name_player(), "has units,", p_one.get_name_player(), "doesn't")
        print(p_two.get_name_player(), "wins the battle")
        resolve_planet_battle_effect(p_two, p_one, planet_id)
        if first_planet:
            p_two.retreat_all_at_planet(planet_id)
            p_two.capture_planet(planet_id)
    elif not player_one_check and not player_two_check:
        print("Neither player has units")
    if first_planet:
        p_one.toggle_planet_in_play(planet_id)
        p_two.toggle_planet_in_play(planet_id)


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

def pygame_check_for_battle(p_one, p_two, planet_id, first_planet, game_screen):
    planet_name = p_two.get_planet_name_given_position(planet_id - 1)
    if first_planet:
        print("First planet. Resolve battle at:", planet_name)
        pygame_resolve_battle(p_one, p_two, planet_id - 1, first_planet, game_screen)
    elif not first_planet:
        print("Not first planet. Check for Warlords at:", planet_name)
        if p_one.check_for_warlord(planet_id - 1):
            print("Battle is resolved at:", planet_name)
            pygame_resolve_battle(p_one, p_two, planet_id - 1, first_planet, game_screen)
        elif p_two.check_for_warlord(planet_id - 1):
            print("Battle is resolved at:", planet_name)
            pygame_resolve_battle(p_one, p_two, planet_id - 1, first_planet, game_screen)
    draw_all(game_screen, p_one, p_two)

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

def pygame_combat_phase(round_number, p_one, p_two, game_screen):
    print("combat:", round_number)
    p_one.set_phase("Combat")
    p_two.set_phase("Combat")
    index = round_number
    planets_counted = 0
    first_planet = True
    draw_all(game_screen, p_one, p_two)
    while planets_counted < 5 and index < 7:
        pygame_check_for_battle(p_one, p_two, index, first_planet, game_screen)
        first_planet = False
        index += 1
        planets_counted += 1
    p_one.retreat_warlord()
    p_two.retreat_warlord()
    p_one.print_headquarters()
    p_two.print_headquarters()
