from abc import abstractmethod

import pygame as pg

class Screen:
    def __init__(self, surface):
        self.surface = surface
        self.entities = []
        self.setup_screen()

    def get_size(self):
        return self.surface.width, self.surface.height

    @abstractmethod
    def setup_screen(self):
        pass

    def process_event(self, event):
        pass

    def refresh(self):
        dirty_rects = self.draw_all()
        self.update(dirty_rects)

    def draw_all(self):
        dirty_rects = []
        for entity in self.entities:
            dirty_rects.extend(entity.update(self.surface))
        return dirty_rects

    def update(self, rectangle_list=[]):
        pg.display.update(rectangle_list)
