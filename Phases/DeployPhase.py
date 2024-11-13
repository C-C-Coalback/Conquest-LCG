import sys
import pygame
import FindCard
import ClickDetection
from Drawing import draw_all
from PassCommand import check_for_pass


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
    draw_all(game_screen, p_one, p_two)
    run = True
    while (not p_one_passed or not p_two_passed) and run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x, y)
                if 24 < y < 116 and p_two.get_has_turn():
                    if check_for_pass(x, y, p_two.get_number()) == 1:
                        p_two_passed = True
                        p_two.toggle_turn()
                        if not p_one_passed:
                            p_one.toggle_turn()
                    else:
                        position = ClickDetection.determine_pos_hand(x, y, p_two)
                        if position == -1:
                            pass
                        else:
                            position2 = ClickDetection.prompt_pos_planet()
                            object_holder = FindCard.find_card(p_two.get_cards()[position])
                            if p_two.play_card(object_holder, position2 + 1) == 0:
                                if not p_one_passed:
                                    p_one.toggle_turn()
                                p_two.toggle_turn()
                                draw_all(game_screen, p_one, p_two)
                elif 594 < y < 686 and p_one.get_has_turn():
                    if check_for_pass(x, y, p_one.get_number()) == 1:
                        p_one_passed = True
                        p_one.toggle_turn()
                        if not p_two_passed:
                            p_two.toggle_turn()
                    else:
                        position = ClickDetection.determine_pos_hand(x, y, p_one)
                        if position == -1:
                            pass
                        else:
                            position2 = ClickDetection.prompt_pos_planet()
                            object_holder = FindCard.find_card(p_one.get_cards()[position])
                            if p_one.play_card(object_holder, position2 + 1) == 0:
                                if not p_two_passed:
                                    p_one.toggle_turn()
                                p_two.toggle_turn()
                                draw_all(game_screen, p_one, p_two)
                elif 319 < y < 376:
                    print("Planets selected")
    print("Success in passing.")
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False

