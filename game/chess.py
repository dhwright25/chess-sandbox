import json
import pygame
from game.player import Player

with open('game/config.json') as f:
    config = json.load(f)


def create_board(size, tile_size):
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


def load_pieces(filename, width, height, x_offset=0, y_offset=0):
    sheet = pygame.image.load(filename)
    pieces = [{}, {}]
    for i, rank in enumerate(["r", "n", "b", "q", "k", "p"]):
        for side in range(2):
            pieces[side][rank] = sheet.subsurface((i * width) + x_offset, (side * height) + y_offset, width, height)
    return pieces


def test_drawing_pieces(screen, pieces, width, height):
    piece_list = list(list(side.values()) for side in pieces)
    pieces = [piece for side in piece_list for piece in side]
    for i, piece in enumerate(pieces):
        screen.blit(piece, (i * width, 50, width, height))


screen = None
clock = None
font = None
FPS = None
piece_sprites = None


def init():
    global screen
    global clock
    global font
    global FPS
    global piece_sprites
    pygame.init()
    pygame.display.set_caption('Chess Sandbox')
    screen = pygame.display.set_mode((config['screen-width'], config['screen-height']))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 18)
    FPS = config['fps']
    piece_sprites = load_pieces(config['pieces-filename'], config['piece-width'], config['piece-height'])


def loop():
    play_1 = Player("b")
    print(play_1)
    while True:
        clock.tick(FPS)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(pygame.Color("dimgray"))  # clear screen
        board = create_board(config['board-size'], config['tile-size'])
        screen.blit(board, board.get_rect(center=(config['board-center-x'], config['board-center-y'])))
        screen.blit(update_stats(), (config['stats-x'], config['stats-y']))
        test_drawing_pieces(screen, piece_sprites, config['piece-width'], config['piece-height'])
        pygame.display.update()


init()
loop()
