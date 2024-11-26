# GIT REPO IS https://github.com/C-C-Coalback/Conquest-LCG.git
import CardClasses
from Phases import CombatPhase, HeadquartersPhase, CommandPhase, DeployPhase
from Inits import PlanetCardsInit, OrksCardsInit
import FindCard
import DeckHandling
import FindDeck
import PlayerClass
import Drawing
import Replace
import random
import pygame

snotling = CardClasses.TokenCard("Snotling", "", "Runt.", "Orks", 1, 1, "NO IMAGE")

orks_card_array = OrksCardsInit.orks_cards_init()
planet_array = PlanetCardsInit.planet_cards_init()
faction_wheel = ["Astra Militarum", "Space Marines", "Tau", "Eldar",
                 "Dark Eldar", "Chaos", "Orks", "Astra Militarum", "Space Marines"]

class ConquestGame:
    def __init__(self, p_one, p_two):
        self.phase = None
        self.round_number = 1
        self.p_one = p_one
        self.p_two = p_two

    def increment_round(self):
        self.round_number += 1

    def get_p_one(self):
        return self.p_one

    def get_p_two(self):
        return self.p_two

    def get_phase(self):
        return self.phase

    def set_phase(self, new_phase):
        self.phase = new_phase

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


def pygame_round(round_number, p_one, p_two, game_screen, conquest_game):
    DeployPhase.pygame_deploy_phase(round_number, p_one, p_two, game_screen, conquest_game)
    CommandPhase.pygame_command_phase(round_number, p_one, p_two, game_screen, conquest_game)
    CombatPhase.pygame_combat_phase(round_number, p_one, p_two, game_screen, conquest_game)
    HeadquartersPhase.pygame_hq_phase(round_number, p_one, p_two, game_screen, conquest_game)


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


def play_pygame(conquest_game, p_one, p_two, game_screen):
    deck_s = FindDeck.find_pygame_deck(game_screen)
    FindDeck.load_deck(deck_s, p_one)
    p_one.shuffle_deck()
    deck_s = FindDeck.find_pygame_deck(game_screen)
    FindDeck.load_deck(deck_s, p_two)
    p_two.shuffle_deck()
    planets_in_play_list = create_planets(planet_array)
    player_one.init_planets_in_game(planets_in_play_list)
    player_two.init_planets_in_game(planets_in_play_list)
    init_player(p_one)
    init_player(p_two)
    Drawing.draw_mat(game_screen)
    Drawing.draw_planets(game_screen, p_one)
    # cardback = pygame.image.load("ResizedImages/Cardback.jpg").convert()
    # window.blit(cardback, (170, 485))
    i = 1
    while i < 8:
        pygame_round(i, p_one, p_two, game_screen, conquest_game)
        i = i + 1


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
    player_one = PlayerClass.Player('Abe', 1)
    deck_string = FindDeck.find_deck()
    FindDeck.load_deck(deck_string, player_one)
    player_one.shuffle_deck()
    player_one.print_deck()
elif holder == "p":
    player_one = PlayerClass.Player('Abe', 1)
    player_two = PlayerClass.Player('Bob', 2)
    play_game(player_one, player_two)
elif holder == "g":
    pygame.init()
    bounds = (1200, 700)
    window = pygame.display.set_mode(bounds)
    pygame.display.set_caption("Conquest")
    status = True
    while status:
        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                status = False
            if x.type == pygame.KEYDOWN:
                if x.key == pygame.K_p:
                    print("P pressed, init play procedure")
                    player_one = PlayerClass.Player('Abe', 1)
                    player_two = PlayerClass.Player('Bob', 2)
                    player_two.toggle_turn()
                    player_two.toggle_initiative()
                    conquest_game = ConquestGame(player_one, player_two)
                    play_pygame(conquest_game, player_one, player_two, window)
    pygame.quit()
elif holder == "r":
    Replace.resize_files()