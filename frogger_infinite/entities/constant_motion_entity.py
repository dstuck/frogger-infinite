import pygame as pg

from frogger_infinite import SCREEN_SIZE
from frogger_infinite import GridStruct
from frogger_infinite.entities.entity import Entity
from game_engine.asset_utils import get_asset_file


class ConstantMotionEntity(Entity):
    IMAGE_SIZE = (GridStruct.GRID_SIZE, GridStruct.GRID_SIZE)

    def __init__(self, init_position, direction, image_name, speed=1, clear_color=(0, 0, 0), *groups):
        self.image_name = image_name
        self.direction = direction
        self.speed = speed
        self.clear_color = clear_color
        self.velocity = tuple(i * self.speed for i in self.direction)
        super().__init__(init_position, *groups)

    def load_image(self):
        image = pg.image.load(get_asset_file('{}.png'.format(self.image_name)))
        image.set_colorkey(self.clear_color)
        return image

    def update(self):
        self.add_next_move(self.velocity)
        if self.rect.center[0] < 0:
            self.move(SCREEN_SIZE[0], 0)
        if self.rect.center[0] > SCREEN_SIZE[0]:
            self.move(-SCREEN_SIZE[0], 0)
        if self.rect.center[1] < 0:
            self.move(0, SCREEN_SIZE[1])
        if self.rect.center[1] > SCREEN_SIZE[1]:
            self.move(0, -SCREEN_SIZE[1])

    def is_deadly(self):
        return False
