from window import Window
from image import Image
from player import Player
from ball import Ball
from score import Score


class Game:
    def __init__(self):

        self.window = Window(1280, 720, "Pong Football")


        self.bg = Image("assets/field.png", 0, 0)
        self.window.add_item_to_draw(self.bg)
        self.window.add_item_to_draw_win(self.bg)

        self.player1 = Player("assets/player1.png", 50, 300, 1)
        self.window.add_item_to_draw(self.player1)

        self.player2 = Player("assets/player2.png", 1150, 300, 2)
        self.window.add_item_to_draw(self.player2)

        self.ball = Ball("assets/ball.png", 617, 337)
        self.window.add_item_to_draw(self.ball)

        self.score1 = Score("assets/score/0.png", 500, 50)
        self.window.add_item_to_draw(self.score1)

        self.score2 = Score("assets/score/0.png", 710, 50)
        self.window.add_item_to_draw(self.score2)

        self.win = Image("assets/win.png", 300, 330)
        self.window.add_item_to_draw_win(self.win)

        self.window.set_move_function(self.move_function)


        self.window.update()

    def move_function(self, item):
        if hasattr(item, 'player'):
            if item.player == 1:
                item.move(self.window.player1_moveup, self.window.player1_movedown)
            elif item.player == 2:
                item.move(self.window.player2_moveup, self.window.player2_movedown)
        if isinstance(item, Ball):
            self.window.is_running(
                item.move(self.player1, self.player2, self.score1, self.score2)
            )
