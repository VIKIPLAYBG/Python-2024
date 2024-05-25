import pygame
import random
from player import Player
from platform import Platform

# Инициализация на Pygame
pygame.init()

# Константи
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (135, 206, 235)

# Екран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Platformer Game")

# Създаване на играч
player = Player()

# Спрайт групи
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()

# Генериране на платформи
for i in range(5):
    p = Platform(random.randint(0, SCREEN_WIDTH - 100), random.randint(0, SCREEN_HEIGHT - 20), "normal")
    platforms.add(p)
    all_sprites.add(p)

# Генериране на пружинни платформи
for i in range(2):
    p = Platform(random.randint(0, SCREEN_WIDTH - 100), random.randint(0, SCREEN_HEIGHT - 20), "spring")
    platforms.add(p)
    all_sprites.add(p)

# Генериране на плъзгащи се платформи
for i in range(2):
    p = Platform(random.randint(0, SCREEN_WIDTH - 150), random.randint(0, SCREEN_HEIGHT - 20), "slide")
    platforms.add(p)
    all_sprites.add(p)

# Генериране на телепорт платформи
for i in range(2):
    p = Platform(random.randint(0, SCREEN_WIDTH - 100), random.randint(0, SCREEN_HEIGHT - 20), "teleport")
    platforms.add(p)
    all_sprites.add(p)

# Основен цикъл на играта
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()

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
