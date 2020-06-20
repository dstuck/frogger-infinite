import pygame as pg

from frogger_infinite.entities.entity import Entity
from frogger_infinite import GridStruct
from game_engine.asset_utils import get_asset_file


class LillyPad(Entity):
    IMAGE_SIZE = (GridStruct.GRID_SIZE, GridStruct.GRID_SIZE)

    def __init__(self, init_position, *groups):
        self.has_frog = False
        super().__init__(init_position, *groups)

    def load_image(self):
        if self.has_frog:
            image = pg.image.load(get_asset_file('player.png'))
            image.set_colorkey((0, 0, 0))
            return image
        else:
            image = pg.Surface(self.IMAGE_SIZE, pg.SRCALPHA, 32)
            image = pg.Surface(self.IMAGE_SIZE, 3333, 32)
            return image.convert_alpha()

    def is_solid(self):
        return self.has_frog

    def add_frog(self):
        self.has_frog = True
        self.refresh_image()
        self.make_dirty()
