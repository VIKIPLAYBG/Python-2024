import pygame
from constants import *

player_1 = pygame.image.load('../player/player_moving_1.png').convert_alpha()
player_1 = pygame.transform.scale(player_1, (PLAYER_WIDTH, PLAYER_HEIGHT))
player_2 = pygame.image.load('../player/player_moving_2.png').convert_alpha()
player_2 = pygame.transform.scale(player_2, (PLAYER_WIDTH, PLAYER_HEIGHT))
player_3 = pygame.image.load('../player/player_moving_3.png').convert_alpha()
player_3 = pygame.transform.scale(player_3, (PLAYER_WIDTH, PLAYER_HEIGHT))
player_4 = pygame.image.load('../player/player_moving_4.png').convert_alpha()
player_4 = pygame.transform.scale(player_4, (PLAYER_WIDTH, PLAYER_HEIGHT))
player_5 = pygame.image.load('../player/player_moving_5.png').convert_alpha()
player_5 = pygame.transform.scale(player_5, (PLAYER_WIDTH, PLAYER_HEIGHT))
player_6 = pygame.image.load('../player/player_moving_6.png').convert_alpha()
player_6 = pygame.transform.scale(player_6, (PLAYER_WIDTH, PLAYER_HEIGHT))

player = [player_1, player_2, player_3, player_4, player_5, player_6]
player_index = 0
player_surf = player[player_index]


def player_animations():
    global player_surf, player_index

    player_index += 0.05
    if player_index >= len(player):
        player_index = 0
    player_surf = player[int(player_index)]
    return player_surf

# enemy_1 = pygame.transform.scale(
#     pygame.image.load('Shark/32bit-shark-thresher1.png').convert_alpha(), (HOSTILE_WIDTH, HOSTILE_HEIGHT))
# enemy_2 = pygame.transform.scale(
#     pygame.image.load('Shark/32bit-shark-thresher2.png').convert_alpha(), (HOSTILE_WIDTH, HOSTILE_HEIGHT))
# enemy_3 = pygame.transform.scale(
#     pygame.image.load('Shark/32bit-shark-thresher3.png').convert_alpha(), (HOSTILE_WIDTH, HOSTILE_HEIGHT))
# enemy_4 = pygame.transform.scale(
#     pygame.image.load('Shark/32bit-shark-thresher4.png').convert_alpha(), (HOSTILE_WIDTH, HOSTILE_HEIGHT))
#
# enemy = [enemy_1, enemy_2, enemy_3, enemy_4]
# enemy_index = 0
# enemy_surf = enemy[enemy_index]
#
#
# def enemy_animations():
#     global enemy_index, enemy_surf
#
#     enemy_index += 0.05
#     if enemy_index >= len(enemy):
#         enemy_index = 0
#     enemy_surf = enemy[int(enemy_index)]
#     return enemy_surf
