import matplotlib.pyplot as plt
import numpy as np
from time import sleep
from board import Board
from items.item import Item
from items.kevin import Kevin
from config import config

x = []  # arrays to plot
y = []

MAX_ITERATIONS = config.get("config.loop.iterations")

board = Board(10, 10, ".")  # the display object
# list of moving objects (kevins)
kevins: list[Item] = [Kevin(4, 8), Kevin(6, 6)]


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
            board.change_cell_char(kevin.pos[0], kevin.pos[1], "K")

        # handlen't errors
        except IndexError as e:
            print(f"Index error: {e}")

        except Exception as e:
            raise e

    board.show_board()
    sleep(1./float(config.get("config.loop.fps")))

    x.append(iteration)
    y.append(kevin.pos[1])


plt.plot(np.array(x), np.array(y))
plt.show()
