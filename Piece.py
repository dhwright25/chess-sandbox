class Piece:
    def __init__(self, x, y, rank):
        self.x = x
        self.y = y
        self.rank = rank

    def __repr__(self):
        return f"Piece({self.x}, {self.y}, {self.rank})"

