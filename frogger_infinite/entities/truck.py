from frogger_infinite import GridStruct
from frogger_infinite.entities.car import Car


class Truck(Car):
    IMAGE_SIZE = (61, GridStruct.GRID_SIZE)

    def __init__(self, init_position, speed=1.5, *groups):
        super().__init__(
            init_position=init_position,
            direction=(-1, 0),
            image_name='truck',
            speed=speed,
            *groups,
        )

    def load_image(self):
        image = super().load_image()
        image.set_colorkey((255, 255, 255))
        return image
