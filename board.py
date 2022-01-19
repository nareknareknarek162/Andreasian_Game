import pygame
import os
import sys
#white - black +

def load_image(name):
    fullname = os.path.join(r'C:/Users/gaa16/PycharmProjects/Andreasian_Game', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

class Board:
    def __init__(self):
        self.board = [0] * 24
        print(self.board)
        self.board[0] = -2
        self.board[5] = 5
        self.board[7] = 3
        self.board[11] = -5
        self.board[12] = 5
        self.board[16] = -3
        self.board[18] = -5
        self.board[23] = -2
        all_sprites = pygame.sprite.Group()
        for i in self.board:
            # можно сразу создавать спрайты с указанием группы
            rocks = pygame.sprite.Sprite(all_sprites)
            rocks.image = pygame.transform.scale(load_image('wrock.png'), (100, 100))
            rocks.image = pygame.transform.scale(load_image('brock.png'), (100, 100))
            rocks.rect = rocks.image.get_rect()

            # задаём случайное местоположение бомбочке
            rocks.rect.x = i * 20
            rocks.rect.y = i * 15
