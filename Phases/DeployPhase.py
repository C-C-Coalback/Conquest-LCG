import sys
import pygame

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
    p_one.print_hand()
    p_one.pygame_print_hand(game_screen)
    p_one.pygame_print_hq(game_screen)
    print("Hand of", p_two.get_name_player())
    p_two.print_hand()
    p_two.pygame_print_hand(game_screen)
    p_two.pygame_print_hq(game_screen)
    run = True
    while (not p_one_passed or not p_two_passed) and run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x, y)
