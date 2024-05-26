import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, platform_type):
        super().__init__()
        self.platform_type = platform_type

        # Starting platform is BLACK
        if self.platform_type == "start":
            self.image = pygame.Surface((100, 20))
            self.image.fill((0, 0, 0))

        # Normal platforms are GREEN
        if self.platform_type == "normal":
            self.image = pygame.Surface((100, 20))
            self.image.fill((0, 255, 0))

        # Spring platforms are YELLOW
        elif self.platform_type == "spring":
            self.image = pygame.Surface((100, 20))
            self.image.fill((255, 255, 0))

        # Slide platforms are BLUE
        elif self.platform_type == "slide":
            self.image = pygame.Surface((150, 20))
            self.image.fill((0, 0, 255))

        # Teleport platforms are PINK
        elif self.platform_type == "teleport":
            self.image = pygame.Surface((100, 20))
            self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.platform_type == "slide":
            self.rect.x += 1
            if self.rect.left > 800:
                self.rect.right = 0
            elif self.platform_type == "spring" or self.platform_type == "teleport":
                pass
