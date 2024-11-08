import sys
import pygame
import FindCard
import Drawing
from Drawing import draw_all


def deploy_phase(round_number, p_one, p_two):
    p_one_passed = False
    p_two_passed = False
    print("deploy:", round_number)
    print("Hand of", p_one.get_name_player())
    p_one.print_hand()
    print("Hand of", p_two.get_name_player())
    p_two.print_hand()
    while not p_one_passed or not p_two_passed:
        if not p_one_passed:
            p_one_passed = p_one.deploy_turn()
        if not p_two_passed:
            p_two_passed = p_two.deploy_turn()

def pygame_deploy_phase(round_number, p_one, p_two, game_screen):
    p_one_passed = False
    p_two_passed = False
    print("deploy:", round_number)
    print("Hand of", p_one.get_name_player())
    print("Hand of", p_two.get_name_player())
    Drawing.draw_all(game_screen, p_one, p_two)
    run = True
    while (not p_one_passed or not p_two_passed) and run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x, y)
                if 24 < y < 116:
                    position = x
                    position = position - 200
                    remainder = position % 80
                    position = int(position/80)
                    print(position, remainder)
                    if 62 < remainder:
                        pass
                    else:
                        print("Player two hand selected, card index", position)
                        print("Number of cards in hand:", len(p_two.get_cards()))
                        if len(p_two.get_cards()) > position:
                            planet_chosen = False
                            while not planet_chosen:
                                for event2 in pygame.event.get():
                                    if event2.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    if event2.type == pygame.MOUSEBUTTONDOWN:
                                        x2, y2 = pygame.mouse.get_pos()
                                        if 319 < y2 < 376:
                                            position2 = x2 - 60
                                            remainder2 = position2 % 165
                                            position2 = int(position2 / 165)
                                            print(position2, remainder2)
                                            if 84 < remainder2:
                                                pass
                                            else:
                                                print("Planets selected, index", position2)
                                                planet_chosen = True
                                                if position < 7:
                                                    object_holder = FindCard.find_card(p_two.get_cards()[position])
                                                    p_two.play_card(object_holder, position2 + 1)
                                                    draw_all(game_screen, p_one, p_two)
                elif 594 < y < 686:
                    position = x
                    position = position - 300
                    remainder = position % 80
                    position = int(position / 80)
                    print(position, remainder)
                    if 62 < remainder < 80:
                        pass
                    else:
                        print("Player one hand selected, card index", position)
                        print("Number of cards in hand:", len(p_one.get_cards()))
                        if len(p_one.get_cards()) > position:
                            planet_chosen = False
                            while not planet_chosen:
                                for event2 in pygame.event.get():
                                    if event2.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    if event2.type == pygame.MOUSEBUTTONDOWN:
                                        x2, y2 = pygame.mouse.get_pos()
                                        if 319 < y2 < 376:
                                            position2 = x2 - 60
                                            remainder2 = position2 % 165
                                            position2 = int(position2 / 165)
                                            print(position2, remainder2)
                                            if 84 < remainder2:
                                                pass
                                            else:
                                                print("Planets selected, index", position2)
                                                planet_chosen = True
                                                if position < 7:
                                                    object_holder = FindCard.find_card(p_one.get_cards()[position])
                                                    p_one.play_card(object_holder, position2 + 1)
                                                    draw_all(game_screen, p_one, p_two)

                elif 319 < y < 376:
                    print("Planets selected")

