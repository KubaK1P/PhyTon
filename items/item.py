import numpy as np


class Item:
    def __init__(self, x: float, y: float, id: int):
        self.x = x
        self.y = y
        self.id = id
        self.pos = np.array([x, y], dtype=float)
        self.v = np.array([0., 0.])
        self.a = np.array([0., 0.])

    def propagate(self, iteration: int):
        pass
