from .interfaces import IRotable, IMovable
from .entities import GameObject

from numpy import array


class MovableAdapter(IMovable):
    def __init__(self, obj: GameObject) -> None:
        self._object = obj

    def get_position(self) -> array:
        return getattr(self._object, "position")

    def set_position(self, new_position: array) -> None:
        setattr(self._object, "position", new_position)

    def get_velocity(self) -> array:
        return getattr(self._object, "velocity")


class RotableAdapter(IRotable):
    def __init__(self, obj: GameObject):
        self._object = obj

    def get_direction(self) -> array:
        return getattr(self._object, "direction")

    def set_direction(self, new_direction: array) -> None:
        setattr(self._object, "direction", new_direction)

    def get_angular_velocity(self) -> array:
        return getattr(self._object, "angular_velocity")



