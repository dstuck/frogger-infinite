import pygame as pg

from game_engine.asset_utils import get_asset_file
from game_engine.screen import Screen


class FroggerStartScreen(Screen):
    def setup_screen(self):
        pass

    def load_image(self):
        return pg.image.load(get_asset_file('start_screen.png'))

    def process_event(self, event):
        if event.type == pg.KEYDOWN:
            self.new_screen = 'frogger_main'
