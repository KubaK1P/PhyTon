import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from kevin import Kevin
from time import sleep
from board import Board
from os import system, name

x = [] # arrays to plot
y = []

board = Board(10, 10, ".") # the display object
kevins = [Kevin(4, 8), Kevin(6, 6)] # list of moving objects (kevins)


# initialize kevins with some acceleration and velocity
for kevin in kevins:
    kevin.a = np.array([0., -0.2])
    kevin.v = np.array([0., 0.])


# main code loop 
for iteration in range(200):
    for kevin in kevins:   
        try:
            # clear the position after kevin
            board.change_cell_char(kevin.pos[0], kevin.pos[1], ".")

            # update kevins' velocity and position 
            kevin.v += kevin.a
            kevin.pos += kevin.v
        
            if iteration == 100:
                # add some variation in the 100th iteration
                kevin.v += np.array([0., 2.])

            if kevin.pos[1] < 0:
                # make kevins bouncy
                kevin.v *= -0.93
                kevin.pos[1] = 0

            # draw kevin
            board.change_cell_char(kevin.pos[0], kevin.pos[1], "K")
            
        # handlen't errors
        except IndexError as e:
            print(f"Index error: {e}")

        except Exception as e:
            raise e
    
    board.show_board()
    sleep(1./24.)
    
    # clear thy screen
    if name == "nt":
        system("cls")
    else:
        system("clear")
    
    x.append(iteration)
    y.append(kevin.pos[1])
    

plt.plot(np.array(x), np.array(y))
plt.show()