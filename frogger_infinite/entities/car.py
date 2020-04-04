import pygame as pg

from frogger_infinite import SCREEN_SIZE
from frogger_infinite import GridStruct
from frogger_infinite.entities.entity import Entity
from game_engine.asset_utils import get_asset_file


class Car(Entity):
    IMAGE_SIZE = (GridStruct.GRID_SIZE, GridStruct.GRID_SIZE)

    def __init__(self, init_position, direction=None, image_name=None, speed=2.5, *groups):
        self.image_name = image_name or 'car_R'
        self.direction = direction or (1, 0)
        self.speed = speed
        super().__init__(init_position, *groups)

    def load_image(self):
        image = pg.image.load(get_asset_file('{}.png'.format(self.image_name)))
        image.set_colorkey((255, 255, 255))
        return image

    def update(self):
        self.move(self.speed * self.direction[0], self.speed * self.direction[1])
        if self.rect.left < 0:
            self.move(SCREEN_SIZE[0], 0)
        if self.rect.right > SCREEN_SIZE[0]:
            self.move(-SCREEN_SIZE[0], 0)
        if self.rect.top < 0:
            self.move(0, SCREEN_SIZE[1])
        if self.rect.bottom > SCREEN_SIZE[1]:
            self.move(0, -SCREEN_SIZE[1])

    def is_deadly(self):
        return True
