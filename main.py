import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from kevin import Kevin
from time import sleep
from board import Board

x = []
y = []

board = Board(10, 10, ".")
kevins = [Kevin(5, 5)]

for thing in kevins:
    thing.a = np.array([0., -0.2])
    thing.v = np.array([0., 0.])

for iteration in range(200):
    for thing in kevins:    
        thing.v += thing.a
        thing.pos += thing.v
        if thing.pos[1] < 0:
            thing.v *= -0.95
            thing.pos[1] = 0
        board.change_cell_char(thing.pos[0], thing.pos[1], "K")
    
    board.show_board()
    sleep(1./6.)
        # x.append(iteration)
        # y.append(thing.pos[1])
    

# plt.plot(np.array(x), np.array(y))
# plt.show()