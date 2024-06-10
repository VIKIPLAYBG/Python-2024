import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load('../enemy/enemy_1.png').convert_alpha(), (100, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 1
        self.on_ground = False

    def update(self):
        self.rect.x += self.direction
        if self.rect.right > 800 or self.rect.left < 0:
            self.direction *= -1
