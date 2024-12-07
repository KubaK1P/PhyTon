import matplotlib.pyplot as plt
import numpy as np
from time import sleep
from board import Board
from items.item import Item
from items.kevin import Kevin
from config import config
from random import randint

MAX_ITERATIONS = config.get("config.loop.iterations")
WIDTH = config.get("config.board.width")
HEIGHT = config.get("config.board.height")
BOARD_CHAR = config.get("config.board.char")

x = []  # arrays to plot
y = []
current_id = 0

board = Board(WIDTH, HEIGHT, BOARD_CHAR)  # the display object

# list of moving objects (kevins)
kevins: list[Item] = [Kevin(6, 12, 0)]


# main code loop
iteration = config.get("config.loop.start")

while True:
    iteration += 1
    if MAX_ITERATIONS >= 0 and iteration > MAX_ITERATIONS:
        break
    for kevin in kevins:
        try:
            # clear the position after kevin
            board.change_cell_char(kevin.pos[0], kevin.pos[1], ".")
            # draw kevin
            kevin.propagate(iteration)

            # kevin dies on the floor => a new one is born
            if 0 < kevin.v[1] < 0.1 and kevin.pos[1] < 1:
                kevins.pop()
                current_id += 1
                kevins.append(Kevin(randint(1, WIDTH), HEIGHT - 3, current_id))
            else:
                board.change_cell_char(kevin.pos[0], kevin.pos[1], "K")

        # handlen't errors
        except IndexError as e:
            print(f"Index error: {e}")

        except Exception as e:
            raise e

    board.show_board(kevins[0].id)
    sleep(1./float(config.get("config.loop.fps")))

    x.append(iteration)
    y.append(kevin.pos[0])
print(kevins)

plt.plot(np.array(x), np.array(y))
plt.show()
