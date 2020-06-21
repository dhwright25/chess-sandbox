import pygame
import json

def load_config(filename):
    with open(filename) as f:
        return json.load(f)


class Engine:
    def __init__(self):
        self.config = load_config('../game/config.json')
        self.running = False
        pygame.init()
        self.screen = pygame.display.set_mode((self.config['screen-width'], self.config['screen-height']))
        self.fps = self.config['fps']
        self.font = pygame.font.SysFont(self.config['font'], self.config['font-size'])
        self.controllers = list()

    def update_stats(self, clock):
        fps = str(int(clock.get_fps()))
        fps_text = self.font.render("FPS: " + str(fps), 1, pygame.Color("red"))
        return fps_text

    def add_controller(self, target):
        self.controllers.append(target)

    def run(self):
        self.running = True
        clock = pygame.time.Clock()
        while self.running:
            dt = clock.tick(self.fps) / 1000.
            events = pygame.event.get()
            self.update(dt, events)
            self.draw(self.screen)
            print(self.update_stats(clock))
            #self.screen.blit(self.update_stats(clock), (self.config['stats-x'], self.config['stats-y']))
        pygame.quit()

    def stop(self):
        self.running = False

    def update(self, dt, events):
        for c in self.controllers:
            c.update(dt, events)

    def draw(self, screen):
        screen.fill(pygame.Color("dimgray"))
        for c in self.controllers:
            c.draw(screen)
        pygame.display.flip()



