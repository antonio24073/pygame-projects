from image import Image


class Score(Image):
    def __init__(self, window, image, x, y):
        super().__init__(window, image, x, y)
        self.current = 0
