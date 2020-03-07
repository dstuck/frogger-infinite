import pygame as pg

from frogger_infinite.screens.frogger_screen import FroggerScreen
from game_engine import SCREEN_SIZE


class GameEngine:
    def __init__(self):
        self.game_name = 'Frogger!'
        self.surface = self.init_pygame(self.game_name)

        self.clock = pg.time.Clock()
        self.fps = 60
        self.elapsed = 0
        self.complete = False
        self.current_screen = None
        self.screens = {
            'frogger_screen': FroggerScreen(self.surface)
        }
        self.set_current_screen('frogger_screen')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pg.quit()

    def init_pygame(self, game_name):
        pg.init()
        pg.display.set_caption(game_name)
        return pg.display.set_mode(SCREEN_SIZE)

    def set_current_screen(self, screen_name):
        self.current_screen = self.screens[screen_name]

    def process_event(self, event):
        self.current_screen.process_event(event)

    def tick(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.complete = True

            self.process_event(event)
        self.current_screen.refresh()

        self.elapsed = self.clock.tick(self.fps)

    def run(self):
        while not self.complete:
            self.tick()
