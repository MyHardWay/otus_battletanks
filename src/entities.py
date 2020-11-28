from abc import ABC


class GameObject(ABC):

    def get_value(self, field: str):
        return getattr(self, field)

    def set_value(self, field: str, value):
        setattr(self, field, value)


class Tank(GameObject):
    pass
