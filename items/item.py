import numpy as np


class Item:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = np.array([x, y], dtype=float)
        self.v = np.array([0., 0.])
        self.a = np.array([0., 0.])

    def propagate(self, iteration: int):
        pass
