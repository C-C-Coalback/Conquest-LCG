# GIT REPO IS https://github.com/C-C-Coalback/Conquest-LCG.git
import CardClasses
from Phases import CombatPhase, HeadquartersPhase, CommandPhase, DeployPhase
from Inits import PlanetCardsInit, OrksCardsInit, ChaosCardsInit, FinalCardInit
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
chaos_card_array = ChaosCardsInit.chaos_cards_init()
final_card_array = FinalCardInit.final_card_init()
card_array = orks_card_array + chaos_card_array + final_card_array
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


def pygame_round(round_number, p_one, p_two, game_screen):
    DeployPhase.pygame_deploy_phase(round_number, p_one, p_two, game_screen)
    CommandPhase.pygame_command_phase(round_number, p_one, p_two, game_screen)
    CombatPhase.pygame_combat_phase(round_number, p_one, p_two, game_screen)
    HeadquartersPhase.pygame_hq_phase(round_number, p_one, p_two, game_screen)


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


def play_pygame(p_one, p_two, game_screen):
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
        pygame_round(i, p_one, p_two, game_screen)
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
    imperial_image = pygame.image.load("ImperialAquila.jpg").convert()
    window.blit(imperial_image, (0, 0))
    font = pygame.font.Font(None, 32)
    color = pygame.Color("green")
    txt_surface = font.render("Press p to play", True, color)
    window.blit(txt_surface, (500,  300))
    txt_surface2 = font.render("Press d to build a deck", True, color)
    window.blit(txt_surface2, (500, 325))
    pygame.display.flip()
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
                    play_pygame(player_one, player_two, window)
                if x.key == pygame.K_d:
                    print("D pressed, init deck-building procedure")
                    DeckHandling.pygame_create_deck(window)
                    status = False
    pygame.quit()
elif holder == "r":
    Replace.resize_files()