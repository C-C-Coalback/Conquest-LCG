import pygame
import sys
def prompt_text(input_window, info_text):
    font = pygame.font.Font(None, 32)
    color_inactive = pygame.Color("white")
    color = color_inactive
    color_active = pygame.Color("blue")
    color_helpful = pygame.Color("green")
    color_warning = pygame.Color("red")
    active = False
    text = ""
    helpful_text = info_text
    split_text = info_text.split("\n")
    warning_text = ""
    if len(split_text) > 1:
        warning_text = split_text[0]
        helpful_text = split_text[1]
    print(split_text, helpful_text, warning_text)
    input_box = pygame.Rect(500, 300, 140, 32)
    while True:
        _ = pygame.time.wait(17)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        imperial_image = pygame.image.load("ImperialAquila.jpg").convert()
        input_window.blit(imperial_image, (0, 0))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        input_window.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(input_window, color, input_box, 2)
        txt_surface2 = font.render(helpful_text, True, color_helpful)
        input_window.blit(txt_surface2, (input_box.x+5, input_box.y-30))
        txt_surface3 = font.render(warning_text, True, color_warning)
        input_window.blit(txt_surface3, (input_box.x + 5, input_box.y - 60))
        pygame.display.flip()