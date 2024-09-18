from image import Image


class Ball(Image):
    def __init__(self,  image, x=617, y=337):
        super().__init__( image, x, y)
        self.move_up = False
        self.move_down = False
        self.dir_x = -10
        self.dir_y = 8

    def move(self):
        self.rect[0] += self.dir_x
        self.rect[1] += self.dir_y