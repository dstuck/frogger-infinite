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
        return self.surface.width, self.surface.height

    def set_player(self, player):
        self.player = player

    @abstractmethod
    def setup_screen(self):
        pass

    def process_event(self, event):
        for entity in self.entities:
            entity.process_event(event)

    def update(self):
        for entity in self.entities:
            entity.update(self.surface)

    def draw(self):
        self.draw_screen()
        dirty_rects = []
        for entity in self.entities:
            dirty_rects.extend(entity.draw(self.surface))
        pg.display.update(dirty_rects)

    def draw_screen(self):
        self.surface.fill((0, 0, 0))

    def check_boundaries(self, entity):
        self.check_collisions(entity)

