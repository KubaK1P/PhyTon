from board import Board
from item import Item
from time import sleep
from os import system

def draw_object(item_inst: Item, board_inst: Board) -> None:
    try:
        if board_inst.get_cell_char(item_inst.x, item_inst.y) != main_board_char:
            return
        board_inst.change_cell_char(item_inst.x, item_inst.y, item_inst.char)
    except Exception as e:
        print(f"Exception: {e}")


def clear_board(board_inst: Board) -> None:
    board_inst.board = [[board_inst.char for i in range(board_inst.width)] for j in range(board_inst.height)]

main_board_char: str = "."
main_board: Board = Board(8, 15, main_board_char)
game_objects: list[Item] = [Item(5.0, 5.0, "O", 0.2)]
iteration: int = 0
global_acceleration: float = 0.2
fps: int = 6

def main():
    # other logic
    clear_board(main_board)

    for item in game_objects:
        if item.is_on_ground(main_board):
            item.step *= -1
        item.y += item.step 
        item.step += global_acceleration
        draw_object(item, main_board)

    main_board.show_board()
    sleep(1 / fps)
    system("cls || clear")


if __name__ == '__main__':
    while iteration < 40:
        main()
        iteration += 1
