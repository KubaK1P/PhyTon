from Board import Board
from Object import Object
from time import sleep
from os import system


def draw_object(object_inst: Object, board_inst: Board) -> None:
    try:
        if board_inst.get_cell_char(object_inst.x, object_inst.y) != main_board_char:
            return
        board_inst.change_cell_char(object_inst.x, object_inst.y, object_inst.char)
    except Exception as e:
        print(f"Exception: {e}")


def clear_board(board_inst: Board) -> None:
    board_inst.board = [[board_inst.char for i in range(board_inst.width)] for j in range(board_inst.height)]

main_board_char: str = "."
main_board: Board = Board(8, 15, main_board_char)
game_objects: list[Object] = [Object(5, 5, "O", 1)]
iteration: int = 0
fps: int = 3

def main():
    # other logic
    clear_board(main_board)

    for obj in game_objects:
        if obj.is_on_ground(main_board):
            obj.step *= -1
        obj.y += obj.step 
        obj.step + 1
        draw_object(obj, main_board)

    main_board.show_board()
    sleep(1 / fps)
    system("cls || clear")


if __name__ == '__main__':
    while iteration < 40:
        main()
        iteration += 1
