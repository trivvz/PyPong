import sys

import pygame

from src import ball


SCREEN_RECT = pygame.Rect(0, 0, 1280, 720)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_RECT.size)

    while True:
        for event in pygame.event.get():

            # Handle quitting via ALT+F4 and window X icon
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
