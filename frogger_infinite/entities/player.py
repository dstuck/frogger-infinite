from typing import List

import pygame as pg

from game_engine.asset_utils import get_asset_file


class Player(pg.sprite.Sprite):
    IMAGE_SIZE = (53, 39)

    def __init__(self, init_position, speed, *groups):
        self.speed = speed
        self.dirty_rects = []

        self.image = pg.image.load(get_asset_file('player.png'))
        self.rect = self.image.get_rect()
        self.position = init_position

    @property
    def position(self):
        return self.rect.center

    @position.setter
    def position(self, value):
        self.dirty_rects.append(self.rect.copy())
        self.rect.center = value

    def get_size(self):
        return self.image.width, self.image.height

    def update(self, surface: pg.Surface) -> List[pg.Rect]:
        if self.dirty_rects:
            surface.blit(self.image, self.rect)
            return self.get_rects_to_update()
        return []

    def get_rects_to_update(self):
        rects_to_update = self.dirty_rects
        rects_to_update.append(self.rect.copy())
        self.dirty_rects = []
        return rects_to_update
