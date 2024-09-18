from image import Image


class Player(Image):
    def __init__(self, image, x, y = 310):
        super().__init__( image, x, y)
        self.move_up = False
        self.move_down = False

    def move_player(self):
        global player1_y

        if self.move_up:
            player1_y -= 5
        else:
            player1_y -= 0

        if self.move_down:
            player1_y += 5
        else:
            player1_y -= 0

        # print(player1_y)
        if player1_y <= 0:
            player1_y = 0
        elif player1_y >= 575:
            player1_y = 575