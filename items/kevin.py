import numpy as np
from items.item import Item
from random import random
from config import config

GRAVITY = config.get("config.physics.gravity")
RANDOM = config.get("config.behavior.random")
FRICTION = config.get("config.physics.friction")
WIDTH = config.get("config.board.width")


class Kevin(Item):
    def __init__(self, x: float, y: float, id: int):
        self.x = x
        self.y = y
        self.id = id
        self.lf = 0
        self.pos = np.array([x, y], dtype=float)
        if not RANDOM:
            self.v = np.array([0., 0.])
        else:
            self.v = np.array([(random() - 0.5) / 2.0, (random() - 0.2) / 2.0])
        self.a = np.array([0., -GRAVITY])

    def propagate(self, iteration: int):
        self.lf += 1
        self.v += self.a
        self.pos += self.v

        for e in config.get("config.events"):
            if e["iteration"] == iteration:
                match e["type"]:
                    case "boost":
                        self.v += np.array([0., float(e["strength"])])

        if self.pos[1] < 0:
            self.v[1] *= -FRICTION
            self.pos[1] = 0
            self.v[0] *= FRICTION

        if self.pos[0] > WIDTH:
            self.v[0] *= -FRICTION
            self.pos[0] = WIDTH

        if self.pos[0] <= 0:
            self.v[0] *= -FRICTION
            self.pos[0] = 0

        print(f"acc: {self.a}, vel: {self.v}, pos: {self.pos}")
