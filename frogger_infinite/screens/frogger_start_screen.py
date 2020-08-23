import pygame as pg

from game_engine.asset_utils import get_asset_file
from game_engine.screen import Screen


class FroggerStartScreen(Screen):
    MAX_TICK_DELAY = 30

    def setup_screen(self):
        self.tick_count = 0

    def update(self):
        self.tick_count += 1
        return self.new_screen

    def load_image(self):
        return pg.image.load(get_asset_file('start_screen.png'))

    def process_event(self, event):
        if (event.type == pg.KEYDOWN) and (self.tick_count > self.MAX_TICK_DELAY):
            self.new_screen = 'frogger_main'
