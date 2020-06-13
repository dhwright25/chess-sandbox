import json
import pygame

with open('config.json') as f:
    config = json.load(f)

def create_board(size, tile_size):
    chessboard = pygame.Surface((tile_size * size, tile_size * size))
    chessboard.fill(pygame.Color("white"))
    tile_count = 0
    for x in range(size):
        for y in range(size):
            if tile_count % 2 == 0:
                pygame.draw.rect(chessboard, pygame.Color("black"), (x * tile_size, y * tile_size, tile_size, tile_size))
            else:
                pygame.draw.rect(chessboard, pygame.Color("white"), (x * tile_size, y * tile_size, tile_size, tile_size))
            tile_count += 1
        tile_count -= 1
    return chessboard


def update_stats():
    fps = str(int(clock.get_fps()))
    fps_text = font.render("FPS: " + str(fps), 1, pygame.Color("red"))
    return fps_text


pygame.init()
pygame.display.set_caption('Chess Sandbox')
screen = pygame.display.set_mode((config['screen-width'], config['screen-height']))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)
FPS = config['fps']
running = True

while running:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color("dimgray"))  # clear screen
    board = create_board(config['board-size'], config['tile-size'])
    screen.blit(board, board.get_rect(center=(config['board-center-x'], config['board-center-y'])))
    screen.blit(update_stats(), (config['stats-x'], config['stats-y']))
    pygame.display.update()

pygame.quit()
quit()
