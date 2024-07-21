# GIT REPO IS https://github.com/C-C-Coalback/Conquest-LCG.git

import CardClasses
import PlanetCardsInit
import OrksCardsInit

snotling = CardClasses.TokenCard("Snotling", "", "Runt.", "Orks", 1, 1)

orks_card_array = OrksCardsInit.orks_cards_init()
planet_array = PlanetCardsInit.planet_cards_init()

# print(planet_array[0].get_text())


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
    i = 0
    found = False
    while orks_card_array[i].get_shields() != -1 and not found:
        if card_to_find == orks_card_array[i].get_name():
            orks_card_array[i].print_info()
            found = True
        else:
            i = i + 1
    if not found:
        retry = input("Card not found. Retry? (y/n)")
        if retry == "y":
            print_info_card()


print_info_card()

# print_info_planet()
