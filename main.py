# GIT REPO IS https://github.com/C-C-Coalback/Conquest-LCG.git

import CardClasses
import CombatPhase
import CommandPhase
import DeployPhase
import PlanetCardsInit
import OrksCardsInit
import FindCard
import DeckHandling
import FindDeck
import PlayerClass
import random
import HeadquartersPhase
import pygame

# from PlayerClass import Player

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


def game_round(round_number, p_one, p_two):
    DeployPhase.deploy_phase(round_number, p_one, p_two)
    CommandPhase.command_phase(round_number, p_one, p_two)
    CombatPhase.combat_phase(round_number, p_one, p_two)
    HeadquartersPhase.hq_phase(round_number, p_one, p_two)


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
    for i in range(2,7,2):
        game_round(i, p_two, p_one)
        game_round(i + 1, p_one, p_two)



def init_player(player):
    warlord = player.get_headquarters()[0]
    player.shuffle_deck()
    print(warlord.get_starting_resources(), warlord.get_starting_cards())
    if player.add_resources(warlord.get_starting_resources()) == 0:
        print("Success in adding resources", player_one.get_resources())
    for i in range(warlord.get_starting_cards()):
        player.draw_card()
    return player


holder = input("Enter: ")
if holder == "c":
    DeckHandling.create_deck()
elif holder == "l":
    player_one = PlayerClass.Player('Abe')
    deck_string = FindDeck.find_deck()
    FindDeck.load_deck(deck_string, player_one)
    player_one.shuffle_deck()
    player_one.print_deck()
elif holder == "p":
    player_one = PlayerClass.Player('Abe')
    player_two = PlayerClass.Player('Bob')
    play_game(player_one, player_two)
elif holder == "g":
    pygame.init()
    bounds = (1024, 768)
    window = pygame.display.set_mode(bounds)
    pygame.display.set_caption("Conquest")
    nazdreg = pygame.image.load("C:\\Users\\argar\\PycharmProjects\\Conquest-LCG\\CardImages\\Nazdreg.webp").convert()
    window.blit(nazdreg, (0,0))
    pygame.display.flip()
    status = True
    while status:
        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                status = False
    pygame.quit()

