import ClickDetection
import pygame
from Drawing import draw_all
from FindCard import find_card

def osus_iv_ability(p_win, p_lose):
    print("Osus IV ability")
    if p_lose.spend_resources(1) == 0:
        p_win.add_resources(1)

def iridial_ability(p_win, p_lose, game_screen):
    print("Iridial ability")
    if p_win.get_number() == 1:
        draw_all(game_screen, p_win, p_lose, "Iridial ability")
    else:
        draw_all(game_screen, p_lose, p_win, "Iridial ability")
    pos_unit, pos_planet = ClickDetection.prompt_pos_unit_anywhere(p_win, game_screen)
    if pos_unit != -1 and pos_planet != -1:
        p_win.remove_damage_from_pos(pos_planet, pos_unit, 999)
    if pos_unit != -1 and pos_planet == -1:
        p_win.remove_damage_from_pos_headquarters(pos_unit, 999)

def plannum_ability(p_win, p_lose, game_screen):
    print("Plannum ability")
    if p_win.get_number() == 1:
        draw_all(game_screen, p_win, p_lose, "Plannum ability")
    else:
        draw_all(game_screen, p_lose, p_win, "Plannum ability")
    pos_unit, pos_planet = ClickDetection.prompt_pos_unit_anywhere(p_win, game_screen, pygame.Color("blue"))
    if pos_unit != -1 and pos_planet != -1:
        if p_win.get_cards_in_play()[pos_planet + 1][pos_unit].get_card_type() == "Warlord":
            print("Unit is a Warlord, movement forbidden with Plannum")
        else:
            target_planet = ClickDetection.prompt_pos_planet()
            p_win.move_unit_from_planet_to_planet(pos_unit, pos_planet, target_planet)
    if pos_unit != -1 and pos_planet == -1:
        if p_win.get_headquarters()[pos_unit] == "Warlord" or p_win.get_headquarters()[pos_unit] == "Support":
            print("Unit is a Warlord / Support, movement forbidden with Plannum")
        else:
            target_planet = ClickDetection.prompt_pos_planet()
            p_win.move_unit_from_hq_to_planet(pos_unit, target_planet)

def tarrus_ability(p_win, p_lose, game_screen):
    print("Tarrus ability")
    if p_win.get_number() == 1:
        draw_all(game_screen, p_win, p_lose, "Tarrus ability")
    else:
        draw_all(game_screen, p_lose, p_win, "Tarrus ability")
    if p_win.count_number_units_in_play() < p_lose.count_number_units_in_play():
        choice = ClickDetection.prompt_two_choices(p_win, game_screen, ["Resources", "Cards"])
        if choice == 1:
            p_win.add_resources(3)
        elif choice == 2:
            p_win.draw_card()
            p_win.draw_card()
            p_win.draw_card()

def yvarn_ability(p_win, p_lose, game_screen):
    print("Y'varn ability")
    if p_win.get_number() == 1:
        draw_all(game_screen, p_win, p_lose, "Y'varn ability")
    else:
        draw_all(game_screen, p_lose, p_win, "Y'varn ability")
    position = ClickDetection.prompt_pos_hand(p_win)
    if position != -1:
        object_holder = find_card(p_win.get_cards()[position])
        if p_win.play_unit_without_cost(object_holder, True):
            print("Card played")
    if p_win.get_number() == 1:
        draw_all(game_screen, p_win, p_lose, "Y'varn ability")
    else:
        draw_all(game_screen, p_lose, p_win, "Y'varn ability")
    position = ClickDetection.prompt_pos_hand(p_lose)
    if position != -1:
        object_holder = find_card(p_lose.get_cards()[position])
        if p_lose.play_unit_without_cost(object_holder, True) == 0:
            print("Card played")
    if p_win.get_number() == 1:
        draw_all(game_screen, p_win, p_lose, "Y'varn ability")
    else:
        draw_all(game_screen, p_lose, p_win, "Y'varn ability")

def barlus_ability():
    print("Barlus ability")

def ferrin_ability():
    print("Ferrin ability")

def carnath_ability():
    print("Carnath ability")

def elouith_ability():
    print("Elouith ability")

def atrox_prime_ability():
    print("Atrox Prime ability")