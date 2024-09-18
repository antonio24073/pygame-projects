from image import Image


class Player(Image):
    def __init__(self, image, x, y, player):
        super().__init__(image, x, y)
        self.player = player
        self.move_up = False
        self.move_down = False
        self.score = 0

    def move(self, move_up, move_down):

        self.move_up = move_up
        self.move_down = move_down

        if self.move_up:
            self.rect[1] -= 5
        else:
            self.rect[1] -= 0

        if self.move_down:
            self.rect[1] += 5
        else:
            self.rect[1] -= 0

        # print(player1_y)
        if self.rect[1] <= 0:
            self.rect[1] = 0
        elif self.rect[1] >= 575:
            self.rect[1] = 575
    def update_score(self):
        pygame.image.load("assets/score/" + str(player2.score) + ".png")
