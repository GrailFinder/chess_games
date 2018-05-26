from piece import Piece


class Pawn(Piece):
    def __init__(self, x: int, is_white: bool):
        Piece.__init__(self, x=x, y=2, piece_type="p", is_white=is_white)

    def check_avaliable_moves(self):
        self.x, self.y = self.get_position()
        if not (self.x, self.y + 1) in self._piece_position:
            return self.x, self.y + 1
        else:
            print(f"field {self.x, self.y+1} is ocupaid")
