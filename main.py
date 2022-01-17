import os
import sys
import pygame

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


def load_image(name):
    fullname = os.path.join(r'C:/Users/gaa16/PycharmProjects/pythonProject1/Andreasian_Game', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

if __name__ == '__main__':
    im1 = load_image("brock.png")
    im2 = load_image("wrock.png")
    screen.blit(im1, (10, 10))
    screen.blit(im2, (30, 45))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()