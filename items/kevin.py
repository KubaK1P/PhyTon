import numpy as np
from items.item import Item

from config import config


class Kevin(Item):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = np.array([x, y], dtype=float)
        self.v = np.array([0., 0.])
        self.a = np.array([0., -config.get("config.physics.gravity")])

    def propagate(self, iteration: int):
        self.v += self.a
        self.pos += self.v

        for e in config.get("config.events"):
            if e["iteration"] == iteration:
                match e["type"]:
                    case "boost":
                        self.v += np.array([0.2, float(e["strength"])])

        if self.pos[1] < 0:
            self.v[1] *= -config.get("config.physics.friction")
            self.pos[1] = 0
            self.v[0] *= config.get("config.physics.friction")

        if self.pos[0] > config.get("config.board.width"):
            self.v[0] *= -config.get("config.physics.friction")
            self.pos[0] = config.get("config.board.width")

        if self.pos[0] < 0:
            self.v[0] *= -config.get("config.physics.friction")
            self.pos[0] = 0
