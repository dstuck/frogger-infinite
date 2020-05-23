from frogger_infinite.entities.constant_motion_entity import ConstantMotionEntity


class Log(ConstantMotionEntity):
    def __init__(self, init_position, direction, image_name, speed=1, *groups):
        super().__init__(init_position, direction, image_name, speed, *groups)

    def is_deadly(self):
        return False

    def is_solid(self):
        return False

    def is_ridable(self):
        return True
