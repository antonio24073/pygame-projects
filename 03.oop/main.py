from window import Window
from image import Image
from player import Player
from ball import Ball


class Game:
    def __init__(self):
        self.window = Window(1280, 720, "Pong Football")
        self.bg = Image( "assets/field.png", 0, 0)
        self.window.add_item_to_draw(self.bg)

        self.player1 = Player( "assets/player1.png", 50)
        self.window.add_item_to_draw(self.player1)

        self.player2 = Player( "assets/player2.png", 1150)
        self.window.add_item_to_draw(self.player2)

        self.ball = Ball("assets/ball.png", 617, 337)
        self.window.add_item_to_draw(self.ball)

        self.window.update()

Game()
