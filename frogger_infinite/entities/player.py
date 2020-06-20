import pygame as pg

from frogger_infinite.entities.entity import Entity
from frogger_infinite import GridStruct
from frogger_infinite.entities.lilly_pad import LillyPad
from game_engine.asset_utils import get_asset_file


class Player(Entity):
    IMAGE_SIZE = (GridStruct.GRID_SIZE, GridStruct.GRID_SIZE)

    def __init__(self, init_position, speed=GridStruct.GRID_SIZE, *groups):
        self.speed = speed
        self.is_dead = False
        self.has_won = False
        super().__init__(init_position, *groups)

    def load_image(self):
        image = pg.image.load(get_asset_file('player.png'))
        image.set_colorkey((0, 0, 0))
        return image

    def collide(self, other_entity):
        self.make_dirty()
        if other_entity.is_deadly():
            self.is_dead = True
        if other_entity.is_rideable() and self.fits_on_rect(other_entity.rect):
            self.add_next_move(other_entity.is_rideable())
        if isinstance(other_entity, LillyPad):
            if not other_entity.has_frog and other_entity.fits_on_rect(other_entity.rect):
                other_entity.add_frog()
                self.has_won = True

    def process_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key in self.DIRECT_DICT:
                self.add_next_move(tuple(i * self.speed for i in self.DIRECT_DICT[event.key]))
