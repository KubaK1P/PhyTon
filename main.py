import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from kevin import Kevin
from time import sleep
from board import Board
from os import system, name

x = []
y = []

board = Board(10, 10, ".")
kevins = [Kevin(4, 8)]

for thing in kevins:
    thing.a = np.array([0., -0.2])
    thing.v = np.array([0., 0.])

for iteration in range(100):
    for thing in kevins:   
        board.change_cell_char(thing.pos[0], thing.pos[1], ".") 
        thing.v += thing.a
        thing.pos += thing.v
        if thing.pos[1] < 0:
            thing.v *= -0.93
            thing.pos[1] = 0
        board.change_cell_char(thing.pos[0], thing.pos[1], "K")
    
    board.show_board()
    sleep(1./24.)
    if name == "nt":
        system("cls")
    else:
        system("clear")
        x.append(iteration)
        y.append(thing.pos[1])
    

plt.plot(np.array(x), np.array(y))
plt.show()