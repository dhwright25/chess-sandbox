from Piece import Piece

starting_positions = {
    "black": [Piece(1, 1, "r"), Piece(1, 2, "n"), Piece(1, 3, "b"), Piece(1, 4, "k"), Piece(1, 5, "q"),
              Piece(1, 6, "b"), Piece(1, 7, "n"), Piece(1, 8, "r"),
              Piece(2, 1, "p"), Piece(2, 2, "p"), Piece(2, 3, "p"), Piece(2, 4, "p"), Piece(2, 5, "p"),
              Piece(2, 6, "p"), Piece(2, 7, "p"), Piece(2, 8, "p")],
    "white": [Piece(8, 1, "r"), Piece(8, 2, "n"), Piece(8, 3, "b"), Piece(8, 4, "k"), Piece(8, 5, "q"),
              Piece(8, 6, "b"), Piece(8, 7, "n"), Piece(8, 8, "r"),
              Piece(7, 1, "p"), Piece(7, 2, "p"), Piece(7, 3, "p"), Piece(7, 4, "p"), Piece(7, 5, "p"),
              Piece(7, 6, "p"), Piece(7, 7, "p"), Piece(7, 8, "p")]
}


class Player:
    def __init__(self, color):
        self.color = color
        if self.color == "b":
            self.pieces = starting_positions["black"]
        else:
            self.pieces = starting_positions["white"]

    def __repr__(self):
        return f"Player({self.color}, {self.pieces})"
