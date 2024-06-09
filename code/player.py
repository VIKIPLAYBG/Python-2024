import pygame
from constants import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load('../player/player_idle_1.png')
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.velocity_y = 0
        self.on_ground = False

    def update(self):
        self.velocity_y += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if keys[pygame.K_LSHIFT]:
                self.rect.x -= DASH_SPEED
            else:
                self.rect.x -= PLAYER_SPEED

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if keys[pygame.K_LSHIFT]:
                self.rect.x += DASH_SPEED
            else:
                self.rect.x += PLAYER_SPEED

        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:
            self.velocity_y = -15

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.on_ground = False
        self.rect.y += self.velocity_y
        self.on_ground = False

    def kill_player(self):
        if self.rect.y >= SCREEN_HEIGHT:
            pygame.quit()