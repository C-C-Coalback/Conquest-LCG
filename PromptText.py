import pygame
import sys
def prompt_textbox_for_deck_name(input_window):
    font = pygame.font.Font(None, 32)
    color_inactive = pygame.Color("white")
    color = color_inactive
    color_active = pygame.Color("blue")
    active = False
    text = ""
    input_box = pygame.Rect(100, 100, 140, 32)
    while True:
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
        input_window.fill((30, 30, 30))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        input_window.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(input_window, color, input_box, 2)
        pygame.display.flip()