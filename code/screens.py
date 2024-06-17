import pygame
import sys
from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load('../maps/background/background.png')


def start_screen(screen):
    screen.blit(background, (0, 0))

    text_font = pygame.font.Font('../fonts/edosz.ttf', 50)

    start_text_surf = text_font.render('Start', False, 'Black')
    control_button_text_surf = text_font.render('Controls', False, 'Black')
    quit_button_text_surf = text_font.render('Quit', False, 'Black')

    start_surf = pygame.Surface((250, 80))
    start_surf.fill('White')
    start_rect = start_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT // 4))

    control_surf = pygame.Surface((250, 80))
    control_rect = control_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    control_surf.fill('White')

    quit_surf = pygame.Surface((250, 80))
    quit_rect = quit_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + SCREEN_HEIGHT // 4))
    quit_surf.fill('White')

    screen.blit(background, (0, 0))
    screen.blit(start_surf, start_rect)
    screen.blit(control_surf, control_rect)
    screen.blit(quit_surf, quit_rect)

    start_text_rect = start_text_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT // 4))
    screen.blit(start_text_surf, start_text_rect)

    control_button_text_rect = control_button_text_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(control_button_text_surf, control_button_text_rect)

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
                elif control_rect.collidepoint(event.pos):
                    return 2
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()


def controls_menu(screen):
    screen.blit(background, (0, 0))
    text_font = pygame.font.Font('../fonts/edosz.ttf', 50)

    controls_text = pygame.font.Font('../fonts/edosz.ttf', 75)
    controls_text_surf = controls_text.render('Controls:', False, 'Black')
    controls_text_surf = text_font.render('Controls:', False, 'Black')

    moving_text = pygame.font.Font('../fonts/edosz.ttf', 75)
    moving_text_surf = moving_text.render('Moving - A S D or Arrow Keys', False, 'Black')
    moving_text_surf = text_font.render('Moving - A S D or Arrow Keys', False, 'Black')

    jump_text = pygame.font.Font('../fonts/edosz.ttf', 65)
    jump_text_surf = jump_text.render('Jumping - W, Space or Arrow UP', False, 'Black')
    jump_text_surf = text_font.render('Jumping - W, Space or Arrow UP', False, 'Black')

    back_button_text = pygame.font.Font('../fonts/edosz.ttf', 75)
    back_button_text_surf = back_button_text.render('Back', False, 'Black')
    back_button_text_surf = text_font.render('Back', False, 'Black')

    controls_text_rect = controls_text_surf.get_rect(center=(
        SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT // 4 - SCREEN_HEIGHT // 8))
    screen.blit(controls_text_surf, controls_text_rect)

    moving_text_rect = moving_text_surf.get_rect(center=(
        SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT // 4 + SCREEN_HEIGHT // 8))
    screen.blit(moving_text_surf, moving_text_rect)

    jump_text_rect = jump_text_surf.get_rect(center=(
        SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(jump_text_surf, jump_text_rect)

    back_surf = pygame.Surface((200, 65))
    back_rect = back_surf.get_rect(center=(
        SCREEN_WIDTH // 2 - SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + SCREEN_HEIGHT // 4 + SCREEN_HEIGHT // 8))
    back_surf.fill('White')
    screen.blit(back_surf, back_rect)

    back_button_text_rect = back_button_text_surf.get_rect(center=(
        SCREEN_WIDTH // 2 - SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + SCREEN_HEIGHT // 4 + SCREEN_HEIGHT // 8))
    screen.blit(back_button_text_surf, back_button_text_rect)

    ret_2 = 2
    mouse_pos = pygame.mouse.get_pos()
    if back_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            ret_2 = 0

    pygame.display.update()

    return ret_2


def death_screen(screen, score):

    text_font = pygame.font.Font('../fonts/edosz.ttf', 50)
    background_surf_2 = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_surf_2.fill('black')
    screen.blit(background_surf_2, (0, 0))

    score_text_surf = text_font.render(f'Score: {score}', False, 'White')
    score_text_rect = score_text_surf.get_rect(center=(
        SCREEN_WIDTH // 2 - SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
    screen.blit(score_text_surf, score_text_rect)

    end_screen_text_surf = text_font.render('You DIED', False, 'Red')
    end_screen_text_rect = end_screen_text_surf.get_rect(center=(
        SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT // 4))
    screen.blit(end_screen_text_surf, end_screen_text_rect)

    menubutton_surf = pygame.Surface((250, 100))
    menubutton_surf.fill('White')
    menubutton_rect = menubutton_surf.get_rect(center=(
        SCREEN_WIDTH // 2 + SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + SCREEN_HEIGHT // 4))
    screen.blit(menubutton_surf, menubutton_rect)

    res_button_surf = pygame.Surface((250, 100))
    res_button_surf.fill('White')
    res_button_rect = res_button_surf.get_rect(center=(SCREEN_WIDTH // 2 + SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
    screen.blit(res_button_surf, res_button_rect)

    end_menu_text_surf = text_font.render('Main Menu', False, 'Black')
    end_menu_text_rect = end_menu_text_surf.get_rect(center=(
        SCREEN_WIDTH // 2 + SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + SCREEN_HEIGHT // 4))
    screen.blit(end_menu_text_surf, end_menu_text_rect)

    end_res_text_surf = text_font.render('Restart', False, 'Black')
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
