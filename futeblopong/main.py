import pygame

pygame.init()

window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption("Futebol pong")

field = pygame.image.load("assets/field.png")

player1 = pygame.image.load("assets/player1.png")
player1_y = 310
player1_moveup = False
player1_movedown = False

player2 = pygame.image.load("assets/player2.png")

ball = pygame.image.load("assets/ball.png")
ball_x = 617
ball_y = 337
ball_dir = -2

def move_player():
    global player1_y

    if player1_moveup:
        player1_y -= 5
    else:
        player1_y -= 0

    if player1_movedown:
        player1_y += 5
    else:
        player1_y -= 0

    # print(player1_y)
    if player1_y <= 0:
        player1_y = 0
    elif player1_y >= 575:
        player1_y = 575

def move_ball():
    global ball_x
    global ball_y
    global ball_dir

    ball_x += ball_dir

    if ball_x < 120:
        if player1_y < ball_y + 23:
            if player1_y + 146 > ball_y:
                ball_dir *= -1


def draw():
    window.blit(field, (0,0))
    window.blit(player1, (50, player1_y))
    window.blit(player2, (1150, 310))
    window.blit(ball, (ball_x, ball_y))

ball = pygame.image.load("assets/ball.png")

loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                player1_moveup = True
            if events.key == pygame.K_s:
                player1_movedown = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                player1_moveup = False
            if events.key == pygame.K_s:
                player1_movedown = False

    # testando colisão primeiro jogador e bola
    # if ball_x < 120:
    #     print("jogador %s %s: " % ( player1_y,(player1_y + 146) ))
    #     print("bola    %s %s: " % (ball_y, (ball_y + 23)))
    #     loop = False

    move_player()
    draw()
    move_ball()
    pygame.display.update()