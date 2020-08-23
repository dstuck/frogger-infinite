import pygame as pg

from frogger_infinite import SCREEN_SIZE
from game_engine.grid_utils import get_grid_corner
from game_engine.asset_utils import get_asset_file
from game_engine.screen import Screen


class FroggerVictoryScreen(Screen):
    def setup_screen(self):
        pass

    def load_image(self):
        sprite_sheet = pg.image.load(get_asset_file('bonus_sprites.png'))
        rect = pg.Rect(80, 0, 40, 40)
        image = pg.Surface(SCREEN_SIZE).convert()
        for i in [1, 3, 5, 7, 9]:
            image.blit(sprite_sheet, get_grid_corner(i, 4), rect)
        return image

    def process_event(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
            self.new_screen = 'frogger_start'
