import pygame
from engine.engine import Engine
from game.board import Board


class Chess:

    def __init__(self):
        self.engine = Engine()
        self.board = Board()
        self.engine.add_entities(self.board)

    def start_game(self):
        self.engine.run()


game = Chess()
game.start_game()
