import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("")

running = True        # Переменная для переключения состояния цикла игры

while running:
    pass              # для пропуска запуска цикла

pygame.quit()