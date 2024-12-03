from Board import Board
from Object import Object
from time import sleep
from os import system


def draw_object(object_inst: Object, board_inst: Board):
    try:
        if board_inst.get_cell_char(object_inst.x, object_inst.y) != main_board_char:
            return
        board_inst.change_cell_char(object_inst.x, object_inst.y, object_inst.char)
    except Exception as e:
        print(f"Exception: {e}")


main_board_char: str = "."
main_board: Board = Board(14, 10, main_board_char)
game_objects: list[Object] = [Object(5, 5, "O")]
iteration: int = 0
fps: int = 6


def main():
    # other logic
    for obj in game_objects:
        draw_object(obj, main_board)

    main_board.show_board()
    sleep(1 / fps)
    system("cls || clear")


if __name__ == '__main__':
    while iteration < 1:
        main()
        iteration += 1
