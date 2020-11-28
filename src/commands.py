from .interfaces import IMovable, IRotable


class RotateCommand:
    def __init__(self, rotable: IRotable):
        self._rotable = rotable

    def execute(self):
        self._rotable.set_direction(self._rotable.get_direction() + self._rotable.get_angular_velocity())


class MoveCommand:
    def __init__(self, movable: IMovable):
        self._movable = movable

    def execute(self):
        self._movable.set_position(self._movable.get_position() + self._movable.get_velocity())



