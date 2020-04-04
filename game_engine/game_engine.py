import pygame as pg

from frogger_infinite.entities.player import Player
from frogger_infinite.screens.frogger_fields_screen import FroggerFieldsScreen
from frogger_infinite.screens.frogger_main_screen import FroggerMainScreen
from frogger_infinite import SCREEN_SIZE
import game_engine.game_states as game_states
from game_engine.grid_utils import get_grid_center


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
            'frogger_main': FroggerMainScreen(self.surface),
            'frogger_fields': FroggerFieldsScreen(self.surface),
        }
        self.reset_player()
        self.state = game_states.RUNNING

    def reset_player(self):
        init_position = get_grid_center(5, 14)
        self.player = Player(init_position)
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
        self.current_screen.refresh_screen()

    def process_event(self, event):
        self.current_screen.process_event(event)

    def tick(self):
        if self.state == game_states.RUNNING:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.complete = True

                self.process_event(event)
            new_screen = self.current_screen.update()
            if new_screen:
                self.set_current_screen(new_screen)

            self.current_screen.draw()
            if self.current_screen.new_state:
                self.state = self.current_screen.new_state
                self.current_screen.new_state = None

        elif self.state == game_states.DEAD:
            self.reset_player()
            self.state = game_states.RUNNING

        self.elapsed = self.clock.tick(self.fps)

    def run(self):
        while not self.complete:
            self.tick()
