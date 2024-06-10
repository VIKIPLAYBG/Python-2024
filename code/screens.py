import pygame
from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load('../maps/background/background.png')


def start_screen():
    start_surf = pygame.Surface((200, 65))

    text_font = pygame.font.Font('../fonts/edosz.ttf', 50)

    quit_button_text = pygame.font.Font('../fonts/edosz.ttf', 75)
    quit_button_text_surf = quit_button_text.render('Quit', False, 'Black')
    quit_button_text_surf = text_font.render('Quit', False, 'Black')

    start_text = pygame.font.Font('../fonts/edosz.ttf', 75)
    start_text_surf = start_text.render('START', False, 'Black')
    start_text_surf = text_font.render('START', False, 'Black')

    quit_surf = pygame.Surface((200, 65))
    quit_rect = quit_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + SCREEN_HEIGHT // 4))
    quit_surf.fill('white')

    start_surf.fill('white')
    start_rect = start_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT // 4))

    screen.blit(background, (0, 0))
    screen.blit(start_surf, start_rect)
    screen.blit(quit_surf, quit_rect)

    start_text_rect = start_text_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT // 4))
    screen.blit(start_text_surf, start_text_rect)

    quit_button_text_rect = quit_button_text_surf.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + SCREEN_HEIGHT // 4))
    screen.blit(quit_button_text_surf, quit_button_text_rect)

    pygame.display.update()

    ret = 0

    mouse_pos = pygame.mouse.get_pos()
    if start_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            ret = 1

    if quit_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            pygame.quit()
            exit()

    return ret
