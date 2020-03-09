from abc import abstractmethod

import pygame as pg

class Screen:
    def __init__(self, surface):
        self.surface = surface
        self.setup_screen()
        self.adjacent_screens = {}
        self.player = None
        self.static_entities = []
        self.dynamic_entities = []

    @property
    def entities(self):
        return [self.player, *self.static_entities, *self.dynamic_entities]

    def get_size(self):
        return self.surface.get_width(), self.surface.get_height()

    def set_player(self, player):
        self.player = player

    @abstractmethod
    def setup_screen(self):
        pass

    def process_event(self, event):
        for entity in self.entities:
            entity.process_event(event)

    def update(self):
        new_rect = self.player.propose_move()
        if new_rect:
            if self.in_bounds(new_rect):
                self.player.set_rect(new_rect)
            else:
                print('out of bounds')
        for entity in self.entities:
            entity.update()

    def draw(self):
        self.draw_screen()
        dirty_rects = []
        for entity in self.entities:
            dirty_rects.extend(entity.draw(self.surface))
        pg.display.update(dirty_rects)

    def draw_screen(self):
        self.surface.fill((0, 0, 0))

    def in_bounds(self, new_rect):
        is_past_left = new_rect.left < 0
        is_past_right = new_rect.right > self.get_size()[0]
        is_past_up = new_rect.top < 0
        is_past_down = new_rect.bottom > self.get_size()[1]
        return not (is_past_left or is_past_right or is_past_up or is_past_down)


