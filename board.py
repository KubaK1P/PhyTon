from math import floor
import os


class Board:
    def __init__(self, width: int, height: int, char: str) -> None:
        self.width = width
        self.height = height
        self.char = char
        self.board = [[char for i in range(width + 1)] for j in range(height)]

    def clear_board(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def show_board(self, kevin_id: int):
        self.clear_board()
        for i in self.board:
            for j in i:
                print(j, end="\t")
            print("")

        for i in range(0, self.width + 1):
            print(i, end="\t")

        print(f"Kevin no. {kevin_id + 1}")
        print("")

    def change_cell_char(self, x: int, y: int, char: str):
        if x < 0 or y < 0 or x > self.width or y > self.height:
            raise IndexError(f"Values are out of bounds {x} {y}")

        self.board[self.height - floor(y) - 1][round(x)] = char

    def get_cell_char(self, x: int, y: int) -> str | None:
        if x < 0 or y < 0 or x > self.width or y > self.height:
            raise IndexError(f"Values are out of bounds {x} {y}")

        return self.board[self.height - floor(y) - 1][round(x)]
