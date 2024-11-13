from PassCommand import check_for_pass
import pygame
import sys

def prompt_pos_hand(player):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x, y, player.get_number())
                if check_for_pass(x, y, player.get_number()) == 1:
                    return -1
                result = determine_pos_hand(x, y, player)
                if result == -1:
                    pass
                else:
                    return result

def determine_pos_hand(x, y, player):
    if player.get_number() == 2 and 24 < y < 116:
        position = x
        position = position - 200
        remainder = position % 80
        position = int(position / 80)
        print(position, remainder)
        if 62 < remainder:
            return -1
        else:
            print("Player two hand selected, card index", position)
            print("Number of cards in hand:", len(player.get_cards()))
            if len(player.get_cards()) > position:
                return position
    elif player.get_number() == 1 and 594 < y < 686:
        position = x
        position = position - 300
        remainder = position % 80
        position = int(position / 80)
        print(position, remainder)
        if 62 < remainder < 80:
            return -1
        else:
            print("Player one hand selected, card index", position)
            print("Number of cards in hand:", len(player.get_cards()))
            if len(player.get_cards()) > position:
                return position

def prompt_pos_planet():
    planet_chosen = False
    while not planet_chosen:
        for event2 in pygame.event.get():
            if event2.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event2.type == pygame.MOUSEBUTTONDOWN:
                x2, y2 = pygame.mouse.get_pos()
                planet_chosen = True
                if 319 < y2 < 376:
                    position2 = x2 - 60
                    remainder2 = position2 % 165
                    position2 = int(position2 / 165)
                    print(position2, remainder2)
                    if 84 < remainder2:
                        pass
                    else:
                        print("Planets selected, index", position2)
                        if position2 < 7:
                            return position2