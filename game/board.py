import pygame
from engine.engine import load_config

config = load_config('config.json')


class Board:
    def __init__(self):
        self.board = self.create(config['board-size'], config['tile-size'])

    def draw(self, screen):
        screen.blit(self.board, self.board.get_rect(center=(config['board-center-x'], config['board-center-y'])))

    def create(self, size, tile_size):
        chessboard = pygame.Surface((tile_size * size, tile_size * size))
        chessboard.fill(pygame.Color("white"))
        tile_count = 0
        for x in range(size):
            for y in range(size):
                if tile_count % 2 == 0:
                    pygame.draw.rect(chessboard, pygame.Color("black"),
                                     (x * tile_size, y * tile_size, tile_size, tile_size))
                else:
                    pygame.draw.rect(chessboard, pygame.Color("white"),
                                     (x * tile_size, y * tile_size, tile_size, tile_size))
                tile_count += 1
            tile_count -= 1
        return chessboard

    def update(self, dt, events):
        pass