import pygame, sys
from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load('../maps/background/background.png')

def start_screen(screen):
    start_surf = pygame.Surface((200, 65))
    text_font = pygame.font.Font('../fonts/edosz.ttf', 50)

    quit_button_text_surf = text_font.render('Quit', False, 'Black')
    start_text_surf = text_font.render('Start', False, 'Black')

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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    return 1
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

def death_screen(screen, score):
    text_font = pygame.font.Font('../fonts/edosz.ttf', 50)
    background_surf_2 = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_surf_2.fill('black')
    screen.blit(background_surf_2, (0, 0))

    score_text_surf = text_font.render(f'Score: {score}', False, 'white')
    score_text_rect = score_text_surf.get_rect(center=(
        SCREEN_WIDTH // 2 - SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
    screen.blit(score_text_surf, score_text_rect)

    end_screen_text_surf = text_font.render('You DIED', False, 'red')
    end_screen_text_rect = end_screen_text_surf.get_rect(center=(
        SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT // 4))
    screen.blit(end_screen_text_surf, end_screen_text_rect)

    menubutton_surf = pygame.Surface((250, 100))
    menubutton_surf.fill('white')
    menubutton_rect = menubutton_surf.get_rect(center=(
        SCREEN_WIDTH // 2 + SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + SCREEN_HEIGHT // 4))
    screen.blit(menubutton_surf, menubutton_rect)

    res_button_surf = pygame.Surface((250, 100))
    res_button_surf.fill('white')
    res_button_rect = res_button_surf.get_rect(center=(SCREEN_WIDTH // 2 + SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
    screen.blit(res_button_surf, res_button_rect)

    end_menu_text_surf = text_font.render('Main Menu', False, 'black')
    end_menu_text_rect = end_menu_text_surf.get_rect(center=(
        SCREEN_WIDTH // 2 + SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + SCREEN_HEIGHT // 4))
    screen.blit(end_menu_text_surf, end_menu_text_rect)

    end_res_text_surf = text_font.render('Restart', False, 'black')
    end_res_text_rect = end_res_text_surf.get_rect(center=(
        SCREEN_WIDTH // 2 + SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
    screen.blit(end_res_text_surf, end_res_text_rect)

    mouse_pos = pygame.mouse.get_pos()
    ret_3 = 3

    if res_button_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            ret_3 = 4

    if menubutton_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            ret_3 = 0

    pygame.display.update()
    return ret_3
