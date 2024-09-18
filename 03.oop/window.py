import pygame


class Window:

    def __init__(self, sizex, sizey, title):

        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)

        self.loop = True

        self.list_obj = []

    def add_obj(self, item):
        self.list_obj.append(item)

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False

    def update(self):
        while self.loop:
            self.events()
            pygame.display.update()
