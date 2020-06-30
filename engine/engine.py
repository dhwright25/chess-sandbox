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
        pygame.display.set_caption(self.config['title'])
        self.fps = self.config['fps']
        self.font = pygame.font.SysFont(self.config['font'], self.config['font-size'])
        self.show_stats = True
        self.entities = list()

    def toggle_stats(self):
        self.show_stats = False if self.show_stats else True

    def update_stats(self, clock):
        fps = str(int(clock.get_fps()))
        fps_text = self.font.render("FPS: " + str(fps), 1, pygame.Color(self.config['stats-color']))
        return fps_text

    def add_entities(self, *target):
        self.entities.append(*target)

    def run(self):
        self.running = True
        clock = pygame.time.Clock()
        while self.running:
            dt = clock.tick(self.fps) / 1000.
            events = pygame.event.get()
            self.key_listener(events)
            self.update(dt, events)
            self.draw(self.screen)
            if self.show_stats:
                self.screen.blit(self.update_stats(clock), (self.config['stats-x'], self.config['stats-y']))
                pygame.display.update()
        pygame.quit()

    def stop(self):
        self.running = False

    def update(self, dt, events):
        for c in self.entities:
            c.update(dt, events)

    def draw(self, screen):
        screen.fill(pygame.Color(self.config['background-color']))
        for c in self.entities:
            c.draw(screen)
        pygame.display.flip()

    def key_listener(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.stop()
            if event.type == pygame.KEYDOWN:
                char = chr(event.key)
                if char in self.config['key-binds'].keys():
                    getattr(self, self.config['key-binds'][char])()





