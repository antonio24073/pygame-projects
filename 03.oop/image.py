import pygame


class Image:
    def __init__(self, image, x, y):
        self.update_image(image)
        self.rect = self.image.get_rect()
        # self.rect = [posX,posY,tamX,tamY]
        self.rect[0] = x
        self.rect[1] = y

    def move(self):
       pass


    def update_image(self, path):
        self.image = pygame.image.load(path)