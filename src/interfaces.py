from abc import ABC, abstractmethod
from numpy import array


class IMovable(ABC):
    @abstractmethod
    def get_position(self) -> array:
        pass

    @abstractmethod
    def set_position(self, new_position: tuple) -> array:
        pass

    @abstractmethod
    def get_velocity(self) -> array:
        pass


class IRotable(ABC):
    @abstractmethod
    def get_direction(self) -> array:
        pass

    @abstractmethod
    def set_direction(self, value: array) -> None:
        pass

    @abstractmethod
    def get_angular_velocity(self) -> array:
        pass



