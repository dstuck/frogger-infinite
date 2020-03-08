from typing import List

import pygame as pg

from game_engine.asset_utils import get_asset_file


class Player(pg.sprite.Sprite):
    DIRECT_DICT = {pg.K_LEFT: (-1, 0),
                   pg.K_RIGHT: (1, 0),
                   pg.K_UP: (0, -1),
                   pg.K_DOWN: (0, 1)}

    IMAGE_SIZE = (53, 39)

    def __init__(self, init_position, speed=25, *groups):
        self.speed = speed
        self.dirty_rects = []

        self.image = pg.image.load(get_asset_file('player.png'))
        self.rect = self.image.get_rect()
        self.position = init_position
        self.next_move = None

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
        if self.next_move:
            self.move(self.next_move)
            self.next_move = None
        if self.dirty_rects:
            surface.blit(self.image, self.rect)
            return self.get_rects_to_update()
        return []

    def move(self, move_coord):
        new_position = (self.position[0] + move_coord[0], self.position[1] + move_coord[1])
        self.position = new_position

    def get_rects_to_update(self):
        rects_to_update = self.dirty_rects
        rects_to_update.append(self.rect.copy())
        self.dirty_rects = []
        return rects_to_update

    def process_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key in self.DIRECT_DICT:
                self.next_move = tuple(i * self.speed for i in self.DIRECT_DICT[event.key])
