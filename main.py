import pygame
import os
import sys
import random
#white - black +

def load_image(name):
    fullname = os.path.join(r'C:/Users/gaa16/PycharmProjects/Andreasian_Game', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


all_sprites = pygame.sprite.Group()
class Board:
    def __init__(self):
        self.board = [0] * 24
        self.board[0] = -2
        self.board[5] = 5
        self.board[7] = 3
        self.board[11] = -5
        self.board[12] = 5
        self.board[16] = -3
        self.board[18] = -5
        self.board[23] = -2
        for i in range(len(self.board)):
            rocks = pygame.sprite.Sprite(all_sprites)
            rocks.image = pygame.transform.scale(load_image('brock.png'), (80, 80))
            rocks.rect = rocks.image.get_rect()
            for j in range(abs(self.board[i])):
                rocks.rect.x = 22 + (i + 1) * 85
                rocks.rect.y = 25 + (abs(j) + 1) * 85

def terminate():
    pygame.quit()
    sys.exit()

def load_image(name):
    fullname = os.path.join(r'C:/Users/gaa16/PycharmProjects/Andreasian_Game', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

def start_screen():
    intro_text = ["Нарды короткие"]

    fon = pygame.transform.scale(load_image('background.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 70)
    text_coord = 200
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('#964B00'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 280
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

def rules_screen():
    intro_text = ["Правила игры", "",
                  "Цель игры - первым принести в 'дом' свои шашки и  собрать их с поля(15 штук)",
                  "дом - часть поля куда приходят все шашки в конце своего пути",
                  "Белые движутся по часовой стрелке, Чёрные против часовой стрелки",
                  "Количество производимых шашкой ходов определяется броском кубика",
                  "Осуществлять передвижение можно только в пустые ячейки, ячейки со своими шашками",
                  "Также можно занимать ячейки с 1 шашкой соперника. В этом случае шашка соперника выходит из ячейки.",
                  "Своё движение подбитая шашка начинает с начала поля. Место определяется игральной костью",
                  "Ячейки в домах пронумерованы от 1(самая правая ячейка) до 6(самая левая) как на кубиках",
                  "Когда все шашки дома их начинают выводить исходя из чисел на кубиках(цифра 1 выводим 1 шашку из первой лунки)",
                  "Вывод происходит исходя по старшинству. Если выпала 5 но все шашки в пятой лунке(и более страших пустые",
                  "то выводят из самой старшей лунки которая осталась"
                  "Если числа на кубиках одинаковые то количество ходов удваивается с 2 до 4",
                  "Если все места на которые может сделать ход игрок заблокированы противником, то ход пропускается"]
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 50
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 800
    screen = pygame.display.set_mode(size)
    rules_flag = True
    start_screen()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if rules_flag:
                    rules_screen()
                    if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                        rules_flag = False
                else:
                    back = pygame.transform.scale(load_image('board_pic.png'), (width, height))
                    screen.blit(back, (0, 0))
                    board = Board()
                    all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()