from settings import *
from sprites import Sprite, MovingSprite
from player import Player


class Level:
    def __init__(self, tmx_map):
        self.display_surface = pygame.display.get_surface()

    def setup(self, tmx_map):
        # tiles
        for x, y, surf in tmx_map.get_layer_by_name('Terrain').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, (self.all_sprites, self.collision_sprites))

        # objects
        for obj in tmx_map.get_layer_by_name('Objects'):
            if obj.name == 'player':
                Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)

        # Moving objects
            for obj in tmx_map.get_layer_by_name('Moving Objects'):
                if obj.name == 'helicopter':
                    if obj.width > obj.height:  # horizontal moving
                        move_dir = 'x'
                        start_pos = (obj.x, obj.y + obj.height / 2)
                        end_pos = (obj.x + obj.width, obj.y + obj.height / 2)
                    else:  # vertical movement
                        move_dir = 'y'
                        start_pos = (obj.x + obj.width / 2, obj.y)
                        end_pos = (obj.x + obj.width / 2, obj.y + obj.height)
                speed = obj.properties['speed']
                MovingSprite((self.all_sprites, self.collision_sprites), start_pos, end_pos, move_dir, speed)

    def run(self):
        self.display_surface.fill('gray')