
import pygame


class Image:
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        # self.rect = [posX,posY,tamX,tamY]
        self.rect[0] = x
        self.rect[1] = y
