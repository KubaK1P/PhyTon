from board import Board

class Item:
    def __init__(self, x: float, y: float, char: str, step: float) -> None:
        self.x = x
        self.y = y
        self.char = char
        self.step = step

    def is_on_ground(self, board_inst: Board) -> bool:
        return self.y > board_inst.height 
