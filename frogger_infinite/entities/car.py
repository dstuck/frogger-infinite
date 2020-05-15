from frogger_infinite.entities.constant_motion_entity import ConstantMotionEntity


class Car(ConstantMotionEntity):
    def __init__(self, init_position, direction=None, image_name=None, speed=1, *groups):
        image_name = image_name or 'car_R'
        direction = direction or (1, 0)
        super().__init__(init_position, direction, image_name, speed, *groups)

    def is_deadly(self):
        return True
