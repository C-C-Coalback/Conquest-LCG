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
    """
    p_one_hand = p_one.get_cards()
    x_c = 500
    y_c = 500
    for i in range(len(p_one_hand)):
        card_image_name = "ResizedImages/" + p_one_hand[i] + ".jpg"
        for letter in card_image_name:
            if letter == " ":
                card_image_name = card_image_name.replace(letter, "_")
        card_image = pygame.image.load(card_image_name).convert()
        game_screen.blit(card_image, (x_c, y_c))
        x_c += 100
    pygame.display.flip()
    """
    print("Hand of", p_two.get_name_player())
    p_two.print_hand()
    p_two.pygame_print_hand(game_screen)
    run = True
    while (not p_one_passed or not p_two_passed) and run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
