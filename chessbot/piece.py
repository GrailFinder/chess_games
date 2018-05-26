class Piece:
    _piece_position = dict()
    _piece_value = {"p": 1, "n": 3, "b": 3, "r": 5, "q": 9, "k": float("inf")}

    def __init__(self, x: int, y: int, piece_type: str, is_white: bool):
        """defines piece coordinates"""
        self.x = x
        self.y = y
        self.type = piece_type
        self.is_white = is_white

        self._piece_position[self.get_position()] = self.type

    def __str__(self):
        return f"{self.type}, at {self.x, self.y}, is white: {self.is_white}"

    def get_value(self):
        return self._piece_value[self.type]

    def get_position(self):
        return self.x, self.y

    def move(self, x: int, y: int):
        piece_type = self._piece_position[self.get_position()].pop()
        self._piece_position[x, y] = piece_type
        self.x, self.y = x, y
