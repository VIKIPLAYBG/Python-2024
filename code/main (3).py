import pygame
import random
import sys
from constants import *
from player import Player
from platforms import Platform
from enemy import Enemy

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Platformer Game")

player = Player()

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Generating the BLACK starting platform
str_platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2, "start")
platforms.add(str_platform)
all_sprites.add(str_platform)

# Generating the GREEN regular platforms
for i in range(5):
    reg_platform = Platform(random.randint(0, SCREEN_WIDTH - 100), random.randint(0, SCREEN_HEIGHT - 20), "normal")
    platforms.add(reg_platform)
    all_sprites.add(reg_platform)

# Generating the YELLOW spring platforms
for i in range(2):
    spr_platform = Platform(random.randint(0, SCREEN_WIDTH - 100), random.randint(0, SCREEN_HEIGHT - 20), "spring")
    platforms.add(spr_platform)
    all_sprites.add(spr_platform)

# Generating the BLUE slippery platforms
for i in range(2):
    sld_platform = Platform(random.randint(0, SCREEN_WIDTH - 150), random.randint(0, SCREEN_HEIGHT - 20), "slide")
    platforms.add(sld_platform)
    all_sprites.add(sld_platform)

# Generating the PINK teleport platforms
for i in range(2):
    tp_platform = Platform(random.randint(0, SCREEN_WIDTH - 100), random.randint(0, SCREEN_HEIGHT - 20), "teleport")
    platforms.add(tp_platform)
    all_sprites.add(tp_platform)

enemy_spawn_time = 2000  # Време за спам на врагове (в милисекунди)
last_enemy_spawn = pygame.time.get_ticks()  # Последно време на спам на враг

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Спам на врагове на всеки enemy_spawn_time милисекунди
    current_time = pygame.time.get_ticks()
    if current_time - last_enemy_spawn > enemy_spawn_time:
        enemy = Enemy(random.randint(0, SCREEN_WIDTH - 40), random.randint(0, SCREEN_HEIGHT - 40))
        enemies.add(enemy)
        all_sprites.add(enemy)
        last_enemy_spawn = current_time

    player.update()
    player.kill_player()

    # Проверка за колизия между играча и платформите
    for platform in platforms:
        if player.rect.colliderect(platform.rect) and player.velocity_y > 0:
            player.rect.bottom = platform.rect.top
            player.velocity_y = 0
            player.on_ground = True

    # Проверка за колизия между играча и враговете
    for enemy in enemies:
        if player.rect.colliderect(enemy.rect):
            # Ако играчът пада върху врага, врагът умира
            if player.velocity_y > 0:
                enemy.kill()
                player.velocity_y = -15  # Играчът отскача
            else:
                running = False  # Играта приключва, ако врагът докосне играча

    all_sprites.update()

    background = pygame.image.load('../maps/background/background.png')
    screen.blit(background, (0, 0))

    all_sprites.draw(screen)
    screen.blit(player.image, player.rect.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()