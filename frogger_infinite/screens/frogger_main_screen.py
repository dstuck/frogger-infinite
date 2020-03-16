import pygame as pg

from frogger_infinite.entities.car import Car
from game_engine.screen import Screen


class FroggerMainScreen(Screen):
    def setup_screen(self):
        self.adjacent_screens['south'] = 'frogger_fields'
        screen_x, screen_y = self.get_size()
        self.dynamic_entities.extend([
            Car((screen_x * 0.9, screen_y * 0.3))
        ])

    def load_image(self):
        image = pg.Surface(self.get_size())
        image.fill((0, 0, 40))
        return image
