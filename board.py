from math import floor

class Board:
    def __init__(self, width: int, height: int, char: str) -> None:
        self.width = width
        self.height = height
        self.char = char
        self.board = [[char for i in range(width)] for j in range(height)]

    def show_board(self):
        for i in self.board:
            for j in i:
                print(j, end="\t")
            print("")
        for i in range(1, self.width + 1):
            print(i, end="\t")
        print("")

    def change_cell_char(self, x: int, y: int, char: str):
        if x <= 0 or y <= 0 or len(char) != 1 or x > self.width or y > self.height:
            raise Exception(f"Values are out of bounds {x} {y}")
        self.board[floor(y) - 1][floor(x) - 1] = char

    def get_cell_char(self, x: int, y: int) -> str | None:
        if x <= 0 or y <= 0 or x > self.width or y > self.height:
            raise Exception(f"Values are out of bounds {x} {y}")
        return self.board[floor(y) - 1][floor(x) - 1]