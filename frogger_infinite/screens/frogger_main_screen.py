import pygame as pg

from frogger_infinite.entities.car import Car
from frogger_infinite.entities.truck import Truck
from game_engine.asset_utils import get_asset_file
from game_engine.screen import Screen


class FroggerMainScreen(Screen):
    def setup_screen(self):
        self.adjacent_screens['south'] = 'frogger_fields'
        screen_x, screen_y = self.get_size()
        self.dynamic_entities.extend([
            Car(
                (screen_x * 0.1, screen_y * 0.2),
                direction=(1, 0),
                image_name="car_R",
            ),
            Car(
                (screen_x * 0.5, screen_y * 0.2),
                direction=(1, 0),
                image_name="car_R",
            ),
            Truck(
                (screen_x * 0.9, screen_y * 0.4),
            ),
            Car(
                (screen_x * 0.4, screen_y * 0.6),
                direction=(1, 0),
                image_name="car_R2",
            ),
        ])

    def load_image(self):
        return pg.image.load(get_asset_file('background.png'))
