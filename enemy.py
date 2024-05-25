import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 1

    def update(self):
        self.rect.x += self.direction
        if self.rect.right > 800 or self.rect.left < 0:
            self.direction *= -1
