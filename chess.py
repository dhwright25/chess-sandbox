import json
import random
import pygame

with open('config.json') as f:
    config = json.load(f)

color = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'grey': (84, 84, 84)
}


def create_board(size, tile_size):
    board = pygame.Surface((tile_size * size, tile_size * size))
    board.fill(color['white'])
    tile_count = 0
    for x in range(size):
        for y in range(size):
            if tile_count % 2 == 0:
                pygame.draw.rect(board, color['black'], (x * tile_size, y * tile_size, tile_size, tile_size))
            else:
                pygame.draw.rect(board, color['white'], (x * tile_size, y * tile_size, tile_size, tile_size))
            tile_count += 1
        tile_count -= 1
    return board

pygame.init()
pygame.display.set_caption('Chess Sandbox')
screen = pygame.display.set_mode((config['screen-width'], config['screen-height']))
running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    screen.fill(color['grey'])  # clear screen
    board = create_board(config['board-size'], config['tile-size'])
    screen.blit(board, board.get_rect(center=(config['board-center-x'], config['board-center-y'])))
    pygame.display.update()

pygame.quit()
quit()
