import unittest
from random import random

from .commands import RotateCommand, MoveCommand
from .adapters import RotableAdapter, MovableAdapter
from .entities import Tank

from numpy import array, allclose


class MainTests(unittest.TestCase):
    def test_rotate(self):
        tank = Tank()
        tank.set_value('direction', array([random(), random()]))
        tank.set_value('angular_velocity', array([random(), random()]))
        tank_adapter = RotableAdapter(tank)
        result = tank_adapter.get_direction() + tank_adapter.get_angular_velocity()
        RotateCommand(tank_adapter).execute()
        self.assertTrue(allclose(result, tank_adapter.get_direction()))

    def test_move(self):
        tank = Tank()
        tank.set_value('position', array([random(), random()]))
        tank.set_value('velocity', array([random(), random()]))
        tank_adapter = MovableAdapter(tank)
        result = tank_adapter.get_position() + tank_adapter.get_velocity()
        MoveCommand(tank_adapter).execute()
        self.assertTrue(allclose(result, tank_adapter.get_position()))


if __name__ == "__main__":
    unittest.main()
