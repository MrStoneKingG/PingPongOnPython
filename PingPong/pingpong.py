from pygame import *
from time import thread_time

mw = display.set_mode((1200, 800))
display.set_caption("Window")
BG = transform.scale(image.load("soccer-field.png"), (1200, 800))

clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, x, y, w, h, filename, speed=0):
        super().__init__()
        self.image = transform.scale(image.load(filename), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

'''class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.y < 800:
            self.rect.x += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.y < 800:
            self.rect.x += self.speed
'''

class PlayerOne(sprite.Sprite):
    def __init__(self, c1, c2, c3, x, y, width, height, speed=0):
        super().__init__()
        self.c1 = c1
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((c1, c2, c3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 550:
            self.rect.y += self.speed

class PlayerTwo(sprite.Sprite):
    def __init__(self, c1, c2, c3, x, y, width, height, speed=0):
        super().__init__()
        self.c1 = c1
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((c1, c2, c3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        keys = key.get_pressed()
        if keys[K_o] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_k] and self.rect.y < 550:
            self.rect.y += self.speed


player1 = PlayerOne(10, 80, 200, 50, 270, 35, 250, 5)

player2 = PlayerTwo(10, 80, 200, 1115, 270, 35, 250, 5)

run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        mw.blit(BG, (0, 0))

        player1.reset()
        player1.update()

        player2.reset()
        player2.update()

    display.update()
    clock.tick(60)