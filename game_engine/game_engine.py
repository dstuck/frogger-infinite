import pygame as pg

from frogger_infinite.entities.player import Player
from frogger_infinite.screens.frogger_fields_screen import FroggerFieldsScreen
from frogger_infinite.screens.frogger_main_screen import FroggerMainScreen
from game_engine import SCREEN_SIZE


class GameEngine:
    def __init__(self):
        self.game_name = 'Frogger!'
        self.surface = self.init_pygame(self.game_name)

        self.clock = pg.time.Clock()
        self.fps = 60
        self.elapsed = 0
        self.complete = False
        init_position = (
            self.surface.get_size()[1]*0.5,
            self.surface.get_size()[0] - Player.IMAGE_SIZE[0] * 0.5,
        )
        self.player = Player(init_position)
        self.current_screen = None
        self.screens = {
            'frogger_main': FroggerMainScreen(self.surface),
            'frogger_fields': FroggerFieldsScreen(self.surface),
        }
        self.set_current_screen('frogger_main')

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
        self.current_screen.set_player(self.player)

    def process_event(self, event):
        self.current_screen.process_event(event)

    def tick(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.complete = True

            self.process_event(event)
        new_screen = self.current_screen.update()
        if new_screen:
            self.set_current_screen(new_screen)

        self.current_screen.draw()

        self.elapsed = self.clock.tick(self.fps)

    def run(self):
        while not self.complete:
            self.tick()
