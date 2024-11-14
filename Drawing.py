import pygame


def draw_mat(game_screen):
    playmat = pygame.image.load("Playmat.png").convert()
    game_screen.blit(playmat, (0, 100))

def draw_planets(game_screen, player):
    x_c = 60
    y_c = 320
    planet_array = player.get_cards_in_play()
    in_play_test = player.get_planets_in_play()
    for i in range(7):
        if in_play_test[i]:
            for letter in planet_array[0][i]:
                if letter == " ":
                    planet_array[0][i] = planet_array[0][i].replace(letter, "_")
            planet_image_name = "ResizedImages/" + planet_array[0][i] + ".jpg"
            planet_image = pygame.image.load(planet_image_name).convert()
            game_screen.blit(planet_image, (x_c, y_c))
        x_c += 165

def draw_hand(game_screen, player):
    player.pygame_print_hand(game_screen)

def draw_both_hand(game_screen, p_one, p_two):
    draw_hand(game_screen, p_one)
    draw_hand(game_screen, p_two)

def draw_hq(game_screen, player):
    player.pygame_print_hq(game_screen)

def draw_both_hq(game_screen, p_one, p_two):
    draw_hq(game_screen, p_one)
    draw_hq(game_screen, p_two)

def draw_in_play(game_screen, player):
    player.pygame_print_cards_in_play(game_screen)

def draw_both_in_play(game_screen, p_one, p_two):
    p_one.pygame_print_cards_in_play(game_screen)
    p_two.pygame_print_cards_in_play(game_screen)

def draw_pass_button_player_one(game_screen):
    font = pygame.font.Font(None, 32)
    color = pygame.Color("red")
    text = "Pass"
    pass_button = pygame.Rect(1100, 600, 50, 50)
    txt_surface = font.render(text, True, color)
    game_screen.blit(txt_surface, (pass_button.x + 5, pass_button.y + 5))
    pygame.draw.rect(game_screen, color, pass_button, 2)

def draw_pass_button_player_two(game_screen):
    font = pygame.font.Font(None, 32)
    color = pygame.Color("red")
    text = "Pass"
    pass_button = pygame.Rect(50, 50, 50, 50)
    txt_surface = font.render(text, True, color)
    game_screen.blit(txt_surface, (pass_button.x + 5, pass_button.y + 5))
    pygame.draw.rect(game_screen, color, pass_button, 2)

def draw_victory_display_both(game_screen, p_one, p_two):
    p_one.draw_victory_display(game_screen)
    p_two.draw_victory_display(game_screen)

def draw_both_pass_button(game_screen):
    draw_pass_button_player_one(game_screen)
    draw_pass_button_player_two(game_screen)

def draw_resource_icon_both(game_screen):
    icon = pygame.image.load("Netrunner_credit.png").convert()
    game_screen.blit(icon, (1000, 600))
    game_screen.blit(icon, (125, 50))


def draw_resource_number_both(game_screen, player_one, player_two):
    resources_p_one = str(player_one.get_resources())
    resources_p_two = str(player_two.get_resources())
    font = pygame.font.Font(None, 32)
    color = pygame.Color("green")
    txt_surface_one = font.render(resources_p_one, True, color)
    game_screen.blit(txt_surface_one, (1019, 615))
    txt_surface_two = font.render(resources_p_two, True, color)
    game_screen.blit(txt_surface_two, (144, 65))


def draw_all(game_screen, p_one, p_two):
    color = (1, 1, 1)
    game_screen.fill(color)
    draw_mat(game_screen)
    draw_planets(game_screen, p_one)
    draw_both_hand(game_screen, p_one, p_two)
    draw_both_hq(game_screen, p_one, p_two)
    draw_both_in_play(game_screen, p_one, p_two)
    draw_both_pass_button(game_screen)
    draw_resource_icon_both(game_screen)
    draw_resource_number_both(game_screen, p_one, p_two)
    draw_victory_display_both(game_screen, p_one, p_two)
    pygame.display.flip()

