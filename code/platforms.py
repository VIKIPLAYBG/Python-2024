import pygame
from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, platform_type):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load('../maps/platforms/platforms.png').convert_alpha(), (300, 75))
        self.platform_type = platform_type

        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.rect.x = x
        self.rect.y = y

