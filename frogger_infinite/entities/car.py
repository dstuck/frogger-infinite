import pygame as pg

from frogger_infinite.entities.entity import Entity
from game_engine.asset_utils import get_asset_file


class Car(Entity):
    IMAGE_SIZE = (53, 39)

    def __init__(self, init_position, speed=10, *groups):
        self.speed = speed
        super().__init__(init_position, *groups)

    def load_image(self):
        image = pg.image.load(get_asset_file('car_1.png'))
        image.set_colorkey((255, 255, 255))
        return image

