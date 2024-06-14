import pygame
from constants import *
from screens import death_screen

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.look = 0
        self.surf = pygame.transform.scale(
            pygame.image.load('../player/player_idle_1.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.velocity_y = 0
        self.on_ground = False

    def update(self):
        self.velocity_y += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.look = 1
            if keys[pygame.K_LSHIFT]:
                self.rect.x -= DASH_SPEED
            else:
                self.rect.x -= PLAYER_SPEED

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.look = 2
            if keys[pygame.K_LSHIFT]:
                self.rect.x += DASH_SPEED
            else:
                self.rect.x += PLAYER_SPEED

        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:
            if keys[pygame.K_LSHIFT]:
                self.velocity_y = -18
            else:
                self.velocity_y = -15

        if self.look == 1:
            self.surf = pygame.transform.flip(self.surf, True, False)
        self.rect.y += self.velocity_y
        self.on_ground = False

    def kill_player(self):
        if self.rect.y >= SCREEN_HEIGHT:
            ret_3 = death_screen(screen, 0)
            return ret_3
