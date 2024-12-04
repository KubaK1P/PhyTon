from Board import Board

class Object:
    def __init__(self, x: int, y: int, char: str, step: int) -> None:
        self.x = x
        self.y = y
        self.char = char
        self.step = step

    def is_on_ground(self, board_inst: Board) -> bool:
        return self.y - 1 >= board_inst.height
