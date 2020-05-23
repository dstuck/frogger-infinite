import pygame as pg

from frogger_infinite.entities.entity import Entity
from frogger_infinite import GridStruct
from game_engine.asset_utils import get_asset_file


class Player(Entity):
    IMAGE_SIZE = (GridStruct.GRID_SIZE, GridStruct.GRID_SIZE)

    def __init__(self, init_position, speed=GridStruct.GRID_SIZE, *groups):
        self.speed = speed
        self.is_dead = False
        super().__init__(init_position, *groups)

    def load_image(self):
        image = pg.image.load(get_asset_file('player.png'))
        image.set_colorkey((0, 0, 0))
        return image

    def propose_move(self):
        if self.next_move:
            new_position = self.move(*self.next_move, inplace=False)
            self.proposed_rect = self.rect.copy()
            self.proposed_rect.center = new_position
            self.next_move = None
            return self.proposed_rect

    def collide(self, other_entity):
        self.make_dirty()
        if other_entity.is_deadly():
            self.is_dead = True
        if other_entity.is_rideable() and self.fits_on_rect(other_entity.rect):
            self.add_next_move(other_entity.is_rideable())

    def process_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key in self.DIRECT_DICT:
                self.add_next_move(tuple(i * self.speed for i in self.DIRECT_DICT[event.key]))
