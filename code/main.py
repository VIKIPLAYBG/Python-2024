import pygame
import random
import sys
from constants import *
from player import Player
from platforms import Platform
from enemy import Enemy
from screens import start_screen, death_screen

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Platformer Game")

player = Player()

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
enemies = pygame.sprite.Group()

str_platform = Platform(SCREEN_WIDTH // 2 - (1.2 * PLAYER_WIDTH), SCREEN_HEIGHT // 2, "start")
platforms.add(str_platform)
all_sprites.add(str_platform)

reg_platforms = {
    Platform((SCREEN_WIDTH - 600), (SCREEN_HEIGHT - 500), "normal"),
    Platform((SCREEN_WIDTH - 1400), (SCREEN_HEIGHT - 700), "normal"),
    Platform((SCREEN_WIDTH - 1700), (SCREEN_HEIGHT - 900), "normal"),
    Platform((SCREEN_WIDTH - 1600), (SCREEN_HEIGHT - 400), "normal"),
    Platform((SCREEN_WIDTH - 900), (SCREEN_HEIGHT - 300), "normal")
}
platforms.add(reg_platforms)
all_sprites.add(reg_platforms)

enemy_spawn_time = 2000
last_enemy_spawn = pygame.time.get_ticks()

running = True
clock = pygame.time.Clock()

game_active = 0
points = 0

while running:
    if game_active == 0:
        game_active = start_screen(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_active == 1:

        # Every {enemy_spawn_time} milliseconds, an enemy spawns
        current_time = pygame.time.get_ticks()
        if current_time - last_enemy_spawn > enemy_spawn_time:
            enemy = Enemy(random.randint(0, SCREEN_WIDTH - 40), random.randint(0, SCREEN_HEIGHT - 40))
            enemies.add(enemy)
            all_sprites.add(enemy)
            last_enemy_spawn = current_time

        player.update()
        if player.kill_player() == 3:
            game_active = 3

        for platform in platforms:
            if player.rect.colliderect(platform.rect) and player.velocity_y > 0:
                player.rect.bottom = platform.rect.top
                player.velocity_y = 0
                player.on_ground = True

        for enemy in enemies:
            if player.rect.colliderect(enemy.rect):
                if player.velocity_y > 0:
                    enemy.kill()
                    points += 5
                    player.velocity_y = -15
                else:
                    game_active = 3

        all_sprites.update()

        background = pygame.image.load('../maps/background/background.png')
        screen.blit(background, (0, 0))

        text_font = pygame.font.Font('../fonts/edosz.ttf', 50)
        score_text_surf = text_font.render(f'Score: {points}', False, 'white')
        score_text_rect = score_text_surf.get_rect(center=(
            SCREEN_WIDTH // 2 - SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        screen.blit(score_text_surf, score_text_rect)

        all_sprites.draw(screen)
        screen.blit(player.surf, player.rect.topleft)

        pygame.display.flip()
        clock.tick(60)

    elif game_active == 3:
        game_active = death_screen(screen, points)

    elif game_active == 4:
        player = Player()
        all_sprites = pygame.sprite.Group()
        platforms = pygame.sprite.Group()
        enemies = pygame.sprite.Group()
        platforms.add(str_platform)
        all_sprites.add(str_platform)
        platforms.add(reg_platforms)
        all_sprites.add(reg_platforms)
        points = 0
        last_enemy_spawn = pygame.time.get_ticks()
        game_active = 1

pygame.quit()
sys.exit()
