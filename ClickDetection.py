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
                if player.get_number() == 2 and 24 < y < 116:
                    position = x
                    position = position - 200
                    remainder = position % 80
                    position = int(position / 80)
                    print(position, remainder)
                    if 62 < remainder:
                        pass
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
                        pass
                    else:
                        print("Player one hand selected, card index", position)
                        print("Number of cards in hand:", len(player.get_cards()))
                        if len(player.get_cards()) > position:
                            return position