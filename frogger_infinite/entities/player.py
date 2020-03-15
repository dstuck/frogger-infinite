from typing import List

import pygame as pg

from frogger_infinite.entities.entity import Entity
from game_engine.asset_utils import get_asset_file


class Player(Entity):
    IMAGE_SIZE = (53, 39)

    def __init__(self, init_position, speed=25, *groups):
        self.speed = speed
        super().__init__(init_position, *groups)

    def load_image(self):
        return pg.image.load(get_asset_file('player.png'))

    def propose_move(self):
        if self.next_move:
            new_position = (
                self.position[0] + self.next_move[0],
                self.position[1] + self.next_move[1]
            )
            self.proposed_rect = self.rect.copy()
            self.proposed_rect.center = new_position
            self.next_move = None
            return self.proposed_rect

    def process_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key in self.DIRECT_DICT:
                self.next_move = tuple(i * self.speed for i in self.DIRECT_DICT[event.key])
