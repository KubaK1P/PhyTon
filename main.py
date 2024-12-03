from Board import Board
from Object import Object
from time import sleep
from os import system


def draw_object(object_inst: Object, board_inst: Board):
    try:
        board_inst.change_cell(object_inst.x, object_inst.y, object_inst.char)
    except Exception as e:
        print(f"Exception: {e}")


main_board: Board = Board(14, 10, ".")
main_object: Object = Object(5, 5, "O")
iteration: int = 0
fps: int = 6

draw_object(main_object, main_board)


def main():
    # other logic
    main_board.show_board()
    sleep(1 / fps)
    system("cls || clear")


if __name__ == '__main__':
    while iteration < 1:
        main()
        iteration += 1

