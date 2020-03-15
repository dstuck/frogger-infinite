from abc import abstractmethod
from typing import List

import pygame as pg


class Entity(pg.sprite.Sprite):
    DIRECT_DICT = {pg.K_LEFT: (-1, 0),
                   pg.K_RIGHT: (1, 0),
                   pg.K_UP: (0, -1),
                   pg.K_DOWN: (0, 1)}

    def __init__(self, init_position, *groups):
        self.dirty_rects = []

        self.image = self.load_image()
        self.rect = self.image.get_rect()
        self.proposed_rect = None
        self.position = init_position
        self.next_move = None

    @property
    def position(self):
        return self.rect.center

    @position.setter
    def position(self, value):
        self.dirty_rects.append(self.rect.copy())
        self.rect.center = value

    @abstractmethod
    def load_image(self):
        pass

    def get_size(self):
        return self.image.width, self.image.height

    def update(self):
        pass

    def draw(self, surface: pg.Surface) -> List[pg.Rect]:
        if self.dirty_rects:
            surface.blit(self.image, self.rect)
            return self.get_rects_to_update()
        return []

    def set_rect(self, rect):
        self.dirty_rects.append(self.rect.copy())
        self.rect = rect

    def get_rects_to_update(self):
        rects_to_update = self.dirty_rects
        rects_to_update.append(self.rect.copy())
        self.dirty_rects = []
        return rects_to_update

    def process_event(self, event):
        pass