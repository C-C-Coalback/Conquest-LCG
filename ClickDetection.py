from PassCommand import check_for_pass
from ActionChecker import check_for_action
import pygame
import sys

def prompt_pos_hand(player):
    run = True
    while run:
        _ = pygame.time.wait(17)
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
            return -1
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
            return -1
    return -1

def determine_pos_hq(x, y, player):
    if player.get_number() == 1 and 500 < y < 588:
        position = x
        position = position - 300
        remainder = position % 80
        position = int(position / 80)
        print(position, remainder)
        if 62 < remainder < 80:
            return -1
        else:
            print("Player one HQ selected, card index", position)
            print("Number of cards in hand:", len(player.get_headquarters()))
            if len(player.get_headquarters()) > position:
                return position
            return -1
    elif player.get_number() == 2 and 125 < y < 213:
        position = x
        position = position - 300
        remainder = position % 80
        position = int(position / 80)
        print(position, remainder)
        if 62 < remainder:
            return -1
        else:
            print("Player two HQ selected, card index", position)
            print("Number of cards in HQ:", len(player.get_headquarters()))
            if len(player.get_headquarters()) > position:
                return position
            return -1
    return -1

def prompt_pos_planet():
    planet_chosen = False
    while not planet_chosen:
        _ = pygame.time.wait(17)
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
    return -1

def prompt_two_choices(player, game_screen, choices_list):
    box1 = pygame.Rect(1047, 214, 150, 40)
    box2 = pygame.Rect(1047, 254, 150, 40)
    font = pygame.font.Font(None, 32)
    choice1_text = choices_list[0]
    choice2_text = choices_list[1]
    color = pygame.Color("blue")
    choice1_txt_surface = font.render(choice1_text, True, color)
    game_screen.blit(choice1_txt_surface, (box1.x + 5, box1.y + 5))
    choice2_txt_surface = font.render(choice2_text, True, color)
    game_screen.blit(choice2_txt_surface, (box2.x + 5, box2.y + 5))
    pygame.draw.rect(game_screen, color, box1, 2)
    pygame.draw.rect(game_screen, color, box2, 2)
    pygame.display.flip()
    while True:
        _ = pygame.time.wait(17)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if box1.collidepoint(event.pos):
                    return 1
                elif box2.collidepoint(event.pos):
                    return 2
                x, y = pygame.mouse.get_pos()
                print(x, y)
                if check_for_pass(x, y, player.get_number()) == 1:
                    return -1

def prompt_n_choices(player, game_screen, choices_list):
    font = pygame.font.Font(None, 32)
    box_array = []
    txt_surface_array = []
    color = pygame.Color("blue")
    for i in range(len(choices_list)):
        box_array.append("")
        txt_surface_array.append("")
    x_current = 1047
    y_current = 214
    y_increment = 40
    for i in range(len(choices_list)):
        box_array[i] = pygame.Rect(x_current, y_current, 150, 40)
        y_current = y_current + y_increment
        txt_surface_array[i] = font.render(choices_list[i], True, color)
    for i in range(len(choices_list)):
        pygame.draw.rect(game_screen, color, box_array[i], 2)
        game_screen.blit(txt_surface_array[i], (box_array[i].x + 5, box_array[i].y + 5))
    pygame.display.flip()
    while True:
        _ = pygame.time.wait(17)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(choices_list)):
                    if box_array[i].collidepoint(event.pos):
                        return i
                    x, y = pygame.mouse.get_pos()
                    print(x, y)
                    if check_for_pass(x, y, player.get_number()) == 1:
                        return -1

def prompt_pos_unit_anywhere_all_players(p_one, p_two, game_screen = None, color1 = None):
    while True:
        _ = pygame.time.wait(17)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x, y)
                if check_for_pass(x, y, p_one.get_number()) == 1 or check_for_pass(x, y, p_two):
                    return -1, -1, -1
                if y > 385:
                    current_player = p_one
                    if p_one.get_number() == 2:
                        current_player = p_two
                    if y > 500:
                        position = determine_pos_hq(x, y, current_player)
                        if position != -1:
                            if color1 is not None:
                                x_for_drawing = position * 80 + 300
                                y_for_drawing = 500
                                pygame.draw.rect(game_screen, color1,
                                                 [x_for_drawing, y_for_drawing, 62, 88], 2)
                                pygame.display.flip()
                            return 1, position, -1
                    else:
                        x_pos = x % 165
                        if 60 < x_pos < 185:
                            print("Player one units")
                            print(x, y)
                            position = y
                            position = position - 385
                            position = int(position / 88)
                            position = 2 * position
                            if x_pos > 122:
                                position = position + 1
                            planet_pos = x - 60
                            planet_pos = int(planet_pos / 165)
                            if position < current_player.get_number_of_cards_at_planet(planet_pos):
                                print("Card present")
                                if color1 is not None:
                                    x_for_drawing = planet_pos * 165 + 60
                                    if x_pos > 122:
                                        x_for_drawing = x_for_drawing + 62
                                    y_for_drawing = (int(position / 2) * 88) + 385
                                    pygame.draw.rect(game_screen, color1,
                                                     [x_for_drawing, y_for_drawing, 62, 88], 2)
                                    pygame.display.flip()
                                return 1, position, planet_pos
                elif y < 320:
                    current_player = p_one
                    if p_one.get_number() == 1:
                        current_player = p_two
                    if y < 212:
                        position = determine_pos_hq(x, y, current_player)
                        if position != -1:
                            if color1 is not None:
                                x_for_drawing = position * 80 + 300
                                y_for_drawing = 125
                                pygame.draw.rect(game_screen, color1,
                                                 [x_for_drawing, y_for_drawing, 62, 88], 2)
                                pygame.display.flip()
                            return 2, position, -1
                    else:
                        x_pos = x % 165
                        if 60 < x_pos < 185:
                            print("Player two units")
                            print(x, y)
                            position = y
                            position = position - 320
                            position = -1 * position
                            position = int(position / 88)
                            position = 2 * position
                            if x_pos > 122:
                                position = position + 1
                            planet_pos = x - 60
                            planet_pos = int(planet_pos / 165)
                            if position < current_player.get_number_of_cards_at_planet(planet_pos):
                                print("Card present")
                                if color1 is not None:
                                    x_for_drawing = planet_pos * 165 + 60
                                    if x_pos > 122:
                                        x_for_drawing = x_for_drawing + 62
                                    y_for_drawing = (int(position / 2) * -88) + 232
                                    pygame.draw.rect(game_screen, color1,
                                                     [x_for_drawing, y_for_drawing, 62, 88], 2)
                                    pygame.display.flip()
                                return 2, position, planet_pos


def prompt_pos_unit_anywhere(player, game_screen = None, color1 = None, hand_is_option = None):
    while True:
        _ = pygame.time.wait(17)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x, y)
                if check_for_pass(x, y, player.get_number()) == 1:
                    return -1, -1
                if y > 385 and player.get_number() == 1:
                    if y > 500:
                        if hand_is_option:
                            hand_pos = determine_pos_hand(x, y, player)
                            if hand_pos != -1:
                                return hand_pos, -2
                        position = determine_pos_hq(x, y, player)
                        if position != -1:
                            if color1 is not None:
                                x_for_drawing = position * 80 + 300
                                y_for_drawing = 500
                                pygame.draw.rect(game_screen, color1,
                                                 [x_for_drawing, y_for_drawing, 62, 88], 2)
                                pygame.display.flip()
                            return position, -1
                    else:
                        x_pos = x % 165
                        if 60 < x_pos < 185:
                            print("Player one units")
                            print(x, y)
                            position = y
                            position = position - 385
                            position = int(position / 88)
                            position = 2 * position
                            if x_pos > 122:
                                position = position + 1
                            planet_pos = x - 60
                            planet_pos = int(planet_pos / 165)
                            if position < player.get_number_of_cards_at_planet(planet_pos):
                                print("Card present")
                                if color1 is not None:
                                    x_for_drawing = planet_pos * 165 + 60
                                    if x_pos > 122:
                                        x_for_drawing = x_for_drawing + 62
                                    y_for_drawing = (int(position / 2) * 88) + 385
                                    pygame.draw.rect(game_screen, color1,
                                                     [x_for_drawing, y_for_drawing, 62, 88], 2)
                                    pygame.display.flip()
                                return position, planet_pos
                elif y < 320 and player.get_number() == 2:
                    if y < 212:
                        if hand_is_option:
                            hand_pos = determine_pos_hand(x, y, player)
                            if hand_pos != -1:
                                return hand_pos, -2
                        position = determine_pos_hq(x, y, player)
                        if position != -1:
                            if color1 is not None:
                                x_for_drawing = position * 80 + 300
                                y_for_drawing = 125
                                pygame.draw.rect(game_screen, color1,
                                                 [x_for_drawing, y_for_drawing, 62, 88], 2)
                                pygame.display.flip()
                            return position, -1
                    else:
                        x_pos = x % 165
                        if 60 < x_pos < 185:
                            print("Player two units")
                            print(x, y)
                            position = y
                            position = position - 320
                            position = -1 * position
                            position = int(position / 88)
                            position = 2 * position
                            if x_pos > 122:
                                position = position + 1
                            planet_pos = x - 60
                            planet_pos = int(planet_pos / 165)
                            if position < player.get_number_of_cards_at_planet(planet_pos):
                                print("Card present")
                                if color1 is not None:
                                    x_for_drawing = planet_pos * 165 + 60
                                    if x_pos > 122:
                                        x_for_drawing = x_for_drawing + 62
                                    y_for_drawing = (int(position / 2) * -88) + 232
                                    pygame.draw.rect(game_screen, color1,
                                                     [x_for_drawing, y_for_drawing, 62, 88], 2)
                                    pygame.display.flip()
                                return position, planet_pos


def prompt_pos_unit_any_planet(player, game_screen = None, color1 = None):
    while True:
        _ = pygame.time.wait(17)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x, y)
                if check_for_pass(x, y, player.get_number()) == 1:
                    return -1
                if y > 385 and player.get_number() == 1:
                    x_pos = x % 165
                    if 60 < x_pos < 185:
                        print("Player one units")
                        print(x, y)
                        position = y
                        position = position - 385
                        position = int(position / 88)
                        position = 2 * position
                        if x_pos > 122:
                            position = position + 1
                        planet_pos = x - 60
                        planet_pos = int(planet_pos / 165)
                        if position < player.get_number_of_cards_at_planet(planet_pos):
                            print("Card present")
                            if color1 is not None:
                                x_for_drawing = planet_pos * 165 + 60
                                if x > 122:
                                    x_for_drawing = x_for_drawing + 62
                                y_for_drawing = (int(position / 2) * 88) + 385
                                pygame.draw.rect(game_screen, color1,
                                                 [x_for_drawing, y_for_drawing, 62, 88], 2)
                                pygame.display.flip()
                            return position, planet_pos
                elif y < 320 and player.get_number() == 2:
                    x_pos = x % 165
                    if 60 < x_pos < 185:
                        print("Player two units")
                        print(x, y)
                        position = y
                        position = position - 320
                        position = -1 * position
                        position = int(position / 88)
                        position = 2 * position
                        if x_pos > 122:
                            position = position + 1
                        planet_pos = x - 60
                        planet_pos = int(planet_pos / 165)
                        if position < player.get_number_of_cards_at_planet(planet_pos):
                            print("Card present")
                            if color1 is not None:
                                x_for_drawing = planet_pos * 165 + 60
                                if x > 122:
                                    x_for_drawing = x_for_drawing + 62
                                y_for_drawing = (int(position / 2) * -88) + 232
                                pygame.draw.rect(game_screen, color1,
                                                 [x_for_drawing, y_for_drawing, 62, 88], 2)
                                pygame.display.flip()
                            return position, planet_pos


def prompt_pos_unit_at_planet(player, planet_id, game_screen = None, color1 = None):
    x_req_1 = (planet_id * 165) + 60
    x_req_2 = (planet_id * 165) + 185
    average = (planet_id * 165) + 122
    while True:
        _ = pygame.time.wait(17)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x, x_req_1, x_req_2, y)
                if check_for_pass(x, y, player.get_number()) == 1:
                    return -1
                if check_for_action(x, y, player.get_number()) == 1:
                    return -2
                if x_req_1 < x < x_req_2:
                    if y > 385 and player.get_number() == 1:
                        print("Player one units")
                        print(x, y)
                        position = y
                        position = position - 385
                        position = int(position / 88)
                        position = 2 * position
                        if x > average:
                            position = position + 1
                        print(position)
                        if position < player.get_number_of_cards_at_planet(planet_id):
                            print("Card present")
                            if color1 is not None:
                                x_for_drawing = x_req_1
                                if x > average:
                                    x_for_drawing = average
                                y_for_drawing = (int(position / 2) * 88) + 385
                                pygame.draw.rect(game_screen, color1,
                                                 [x_for_drawing, y_for_drawing, 62, 88], 2)
                                pygame.display.flip()
                            return position
                    elif y < 320 and player.get_number() == 2:
                        print("Player two units")
                        position = y
                        position = position - 320
                        position = -1 * position
                        position = int(position / 88)
                        position = 2 * position
                        if x > average:
                            position = position + 1
                        print(position)
                        if position < player.get_number_of_cards_at_planet(planet_id):
                            print("Card present")
                            if color1 is not None:
                                x_for_drawing = x_req_1
                                if x > average:
                                    x_for_drawing = average
                                y_for_drawing = (int(position / 2) * -88) + 232
                                print("Drawing", x_for_drawing, y_for_drawing)
                                pygame.draw.rect(game_screen, color1,
                                                 [x_for_drawing, y_for_drawing, 62, 88], 2)
                                pygame.display.flip()
                            return position