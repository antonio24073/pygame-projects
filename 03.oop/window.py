import pygame


class Window:

    def __init__(self, sizex, sizey, title):

        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)

        self.loop = True

        self.items_to_draw = []

    def add_item_to_draw(self, item):
        self.items_to_draw.append(item)

    def draw(self):
        for item in self.items_to_draw:
            self.window.blit(item.image, (item.rect[0], item.rect[1]))

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False

    def update(self):
        while self.loop:
            self.draw()
            self.events()
            pygame.display.update()
