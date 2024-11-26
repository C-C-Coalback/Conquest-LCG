import FindCard
import pygame

def find_deck():
    file_to_read = open("deck_storage.txt", "r")
    deck_name = input("Enter deck name: ")
    file_text = file_to_read.read()
    pos = 0
    current_deck = ""
    while pos < len(file_text):
        while file_text[pos] != "#":
            current_deck += file_text[pos]
            pos += 1
        if current_deck == deck_name:
            print("Deck found")
            file_to_read.close()
            return read_deck(pos)
        else:
            while file_text[pos] != "\n":
                pos += 1
            pos += 1
            current_deck = ""
    file_to_read.close()
    print("Deck not found")
    return find_deck()


def find_pygame_deck(input_window):
    font = pygame.font.Font(None, 32)
    file_to_read = open("deck_storage.txt", "r")
    color_inactive = pygame.Color("white")
    color = color_inactive
    color_active = pygame.Color("blue")
    done = False
    active = False
    text = ""
    input_box = pygame.Rect(100, 100, 140, 32)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        input_window.fill((30, 30, 30))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        input_window.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(input_window, color, input_box, 2)
        pygame.display.flip()

    deck_name = text
    file_text = file_to_read.read()
    pos = 0
    current_deck = ""
    while pos < len(file_text):
        while file_text[pos] != "#":
            current_deck += file_text[pos]
            pos += 1
        if current_deck == deck_name:
            print("Deck found")
            file_to_read.close()
            return read_deck(pos)
        else:
            while file_text[pos] != "\n":
                pos += 1
            pos += 1
            current_deck = ""
    file_to_read.close()
    print("Deck not found")
    return find_pygame_deck(input_window)


def read_deck(pos):
    file_to_read = open("deck_storage.txt", "r")
    deck_contents = ""
    file_text = file_to_read.read()
    while file_text[pos] != "\n":
        deck_contents += file_text[pos]
        pos += 1
    return deck_contents


def load_deck(deck_string, player_object):
    print(deck_string)
    deck_string += "#"
    current_name = ""
    position = 1
    first_card = True
    while position < len(deck_string):
        while deck_string[position] != "#":
            current_name += deck_string[position]
            position += 1
        if first_card:
            player_object.add_to_hq(FindCard.find_card(current_name))
            first_card = False
        else:
            player_object.add_card_to_deck(current_name)
        current_name = ""
        position += 1
