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
player2_y = 310

ball = pygame.image.load("assets/ball.png")
ball_x = 617
ball_y = 337
ball_dir = -10
ball_dir_y = 8

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

def move_player2():
    global player2_y
    player2_y = ball_y # fazendo segundo jogador defender todas

def move_ball():
    global ball_x
    global ball_y
    global ball_dir
    global ball_dir_y

    ball_x += ball_dir
    ball_y += ball_dir_y

    if ball_x < 120:
        if player1_y < ball_y + 23:
            if player1_y + 146 > ball_y:
                ball_dir *= -1

    if ball_x > 1100:
        if player2_y < ball_y + 23:
            if player2_y + 146 > ball_y:
                ball_dir *= -1

    if ball_y > 680:
        ball_dir_y *= -1
    elif ball_y <= 40:
        ball_dir_y *= -1

    # # teste fazer a bola rebater se passar do goleiro
    # if ball_x < 0:
    #     ball_dir *= -1
    # if ball_x > 1280:
    #     ball_dir *= -1

    if ball_x < -50: # caso jogador um perder
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1 # inverter lado da bola ao reiniciar
        ball_dir *= -1 # inverter lado da bola ao reiniciar
    elif ball_x > 1320: # caso jogador dois perder
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1

def draw():
    window.blit(field, (0,0))
    window.blit(player1, (50, player1_y))
    window.blit(player2, (1150, player2_y))
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
    move_player2()
    draw()
    move_ball()
    pygame.display.update()