import pygame as pg

from frogger_infinite.entities.car import Car
from frogger_infinite.entities.lilly_pad import LillyPad
from frogger_infinite.entities.log import Log
from frogger_infinite.entities.truck import Truck
from game_engine.asset_utils import get_asset_file
from game_engine.grid_utils import get_grid_center
from game_engine.screen import Screen


class FroggerMainScreen(Screen):
    def setup_screen(self):
        self.adjacent_screens['south'] = 'frogger_fields'
        self.dynamic_entities.extend([
            Car(
                get_grid_center(*coord),
                direction=(-1, 0),
                image_name="car_L",
            ) for coord in [(2, 13), (6, 13), (10, 13)]
        ])
        self.dynamic_entities.extend([
            Car(
                get_grid_center(*coord),
                direction=(1, 0),
                image_name="car_R",
            ) for coord in [(1, 12), (4.5, 12), (8, 12)]
        ])
        self.dynamic_entities.extend([
            Car(
                get_grid_center(*coord),
                direction=(-1, 0),
                image_name="car_L2",
            ) for coord in [(1, 11), (4.5, 11), (8, 11)]
        ])
        self.dynamic_entities.extend([
            Car(
                get_grid_center(*coord),
                direction=(1, 0),
                speed=3,
                image_name="car_R2",
            ) for coord in [(1, 10)]
        ])
        self.dynamic_entities.extend([
            Truck(
                get_grid_center(*coord),
            ) for coord in [(3, 9), (8, 9)]
        ])
        self.dynamic_entities.extend([
            Log(
                get_grid_center(*coord),
                direction=(-1, 0),
                image_name="turtle_3",
            ) for coord in [(1, 7), (4, 7), (7, 7), (10, 7)]
        ])
        self.dynamic_entities.extend([
            Log(
                get_grid_center(*coord),
                direction=(1, 0),
                image_name="tree_1",
                clear_color=(255, 255, 255),
            ) for coord in [(2, 6), (6, 6), (10, 6)]
        ])
        self.dynamic_entities.extend([
            Log(
                get_grid_center(*coord),
                direction=(1, 0),
                image_name="tree_2",
                speed=2,
                clear_color=(255, 255, 255),
            ) for coord in [(2, 5), (8, 5)]
        ])
        self.dynamic_entities.extend([
            Log(
                get_grid_center(*coord),
                direction=(-1, 0),
                image_name="turtle_2",
            ) for coord in [(1, 4), (4, 4), (7, 4), (10, 4)]
        ])
        self.dynamic_entities.extend([
            Log(
                get_grid_center(*coord),
                direction=(1, 0),
                image_name="tree_3",
                speed=1.5,
                clear_color=(255, 255, 255),
            ) for coord in [(2, 3), (6, 3), (10, 3)]
        ])
        self.dynamic_entities.extend([
            LillyPad(
                get_grid_center(*coord),

            ) for coord in [(0, 2), (2.5, 2), (5, 2), (7.5, 2), (10, 2)]
        ])
    def load_image(self):
        return pg.image.load(get_asset_file('background.png'))
