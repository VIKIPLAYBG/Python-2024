import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, platform):
        super().__init__()
        self.surf = pygame.transform.scale(
            pygame.image.load('../enemy/enemy_1.png').convert_alpha(), (100, 50))
        self.image = self.surf
        self.rect = self.image.get_rect()
        self.platform = platform
        self.rect.centerx = platform.rect.centerx
        self.rect.bottom = platform.rect.top
        self.direction = 1

    def update(self):
        self.rect.x += self.direction
        if self.rect.right >= self.platform.rect.right or self.rect.left <= self.platform.rect.left:
            self.direction *= -1
            self.image = pygame.transform.flip(self.image, True, False)  # Flip the image

        self.collide_enemies()

    def collide_enemies(self):
        for enemy in self.platform.enemy_sprites:
            if self != enemy and self.rect.colliderect(enemy.rect):
                self.direction *= -1
                self.image = pygame.transform.flip(self.image, True, False)
                enemy.direction *= -1
                enemy.image = pygame.transform.flip(enemy.image, True, False)
