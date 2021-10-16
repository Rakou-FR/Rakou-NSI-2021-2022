import pygame
from pygame.locals import QUIT


screen = pygame.display.set_mode((640, 640))
pygame.init()


def breaak():
    pygame.quit()

while True:
    for event in pygame.event.get():
        print(event)
        breaak()
