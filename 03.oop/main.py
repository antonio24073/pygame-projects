import pygame
from obj import Obj

window = pygame.display.set_mode([1280,720])
title = pygame.display.set_caption("Futebol")

campo = Obj("assets/field.png", 0, 0)
campo.draw(window)

player1 = Obj("assets/player1.png", 50, 300)
player1.draw(window)

player2 = Obj("assets/player2.png", 1150, 300)
player2.draw(window)

loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
    pygame.display.update()