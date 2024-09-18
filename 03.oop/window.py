import pygame


class Window:

    def __init__(self, sizex, sizey, title):

        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)

        self.loop = True

        self.items_to_draw = []

        self.init_commands()

    def init_commands(self):

        self.player1_moveup = False
        self.player1_movedown = False
        self.player1_moveup = False
        self.player1_movedown = False

        self.player2_moveup = False
        self.player2_movedown = False
        self.player2_moveup = False
        self.player2_movedown = False


    def add_item_to_draw(self, image):
        self.items_to_draw.append(image)


    def draw(self):
        for item in self.items_to_draw:
            self.window.blit(item.image, (item.rect[0], item.rect[1]))
            if hasattr(item, 'player'):
                if item.player == 1:
                    item.move(self.player1_moveup, self.player1_movedown)
                elif item.player == 2:
                    item.move(self.player2_moveup, self.player2_movedown)

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_w:
                    self.player1_moveup = True
                if events.key == pygame.K_s:
                    self.player1_movedown = True
            if events.type == pygame.KEYUP:
                if events.key == pygame.K_w:
                    self.player1_moveup = False
                if events.key == pygame.K_s:
                    self.player1_movedown = False

            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_UP:
                    self.player2_moveup = True
                if events.key == pygame.K_DOWN:
                    self.player2_movedown = True
            if events.type == pygame.KEYUP:
                if events.key == pygame.K_UP:
                    self.player2_moveup = False
                if events.key == pygame.K_DOWN:
                    self.player2_movedown = False

    def update(self):
        while self.loop:
            self.draw()
            self.events()
            pygame.display.update()
