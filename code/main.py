import pygame
import random
from constants import *
from player import Player
from platforms import Platform

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Platformer Game")

player = Player()

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()

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

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()
    player.kill_player()

    for platform in platforms:
        if player.rect.colliderect(platform.rect) and player.velocity_y > 0:
            player.rect.bottom = platform.rect.top
            player.velocity_y = 0
            player.on_ground = True

    screen.fill(BACKGROUND_COLOR)

    all_sprites.draw(screen)
    screen.blit(player.image, player.rect.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
