import pygame as pg

from game_engine.screen import Screen


class FroggerFieldsScreen(Screen):
    def setup_screen(self):
        self.adjacent_screens['north'] = 'frogger_main'

    def load_image(self):
        image = pg.Surface(self.get_size())
        image.fill((0, 100, 0))
        return image
