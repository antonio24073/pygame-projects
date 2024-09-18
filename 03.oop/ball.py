from image import Image


class Ball(Image):
    def __init__(self,  image, x=617, y=337):
        super().__init__( image, x, y)
        self.move_up = False
        self.move_down = False
        self.dir_x = -10
        self.dir_y = 8

    def move(self, player1, player2):
        self.rect[0] += self.dir_x
        self.rect[1] += self.dir_y

        self.rect[0] += self.dir_x
        self.rect[1] += self.dir_y
    
        if self.rect[0] < 120:
            if player1.rect[1] < self.rect[1] + 23:
                if player1.rect[1] + 146 > self.rect[1]:
                    self.dir_x *= -1
    
        if self.rect[0] > 1100:
            if player2.rect[1] < self.rect[1] + 23:
                if player2.rect[1] + 146 > self.rect[1]:
                    self.dir_x *= -1
    
        if self.rect[1] > 680:
            self.dir_y *= -1
        elif self.rect[1] <= 40:
            self.dir_y *= -1
    
        # # teste fazer a bola rebater se passar do goleiro
        # if self.rect[0] < 0:
        #     self.dir_x *= -1
        # if self.rect[0] > 1280:
        #     self.dir_x *= -1
    
        if self.rect[0] < -50:  # caso jogador um perder
            self.rect[0] = 617
            self.rect[1] = 337
            self.dir_y *= -1  # inverter lado da bola ao reiniciar
            self.dir_x *= -1  # inverter lado da bola ao reiniciar
            player2.score += 1
        elif self.rect[0] > 1320:  # caso jogador dois perder
            self.rect[0] = 617
            self.rect[1] = 337
            self.dir_y *= -1
            self.dir_x *= -1
            player1.score += 1