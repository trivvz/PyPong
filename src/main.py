import sys

import pygame

from src import ball
from src.config import SCREEN_HEIGHT, SCREEN_WIDTH

SCREEN_RECT = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)


def main():
    pygame.init()
    pygame.display.set_caption("PyPong")
    screen = pygame.display.set_mode(SCREEN_RECT.size)
    clock = pygame.time.Clock()

    pygame.draw.circle(screen, (255, 255, 255), (100, 100), 10)

    my_ball = ball.Ball((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), (5, 5))
    my_ball.draw(screen)

    while True:
        # Clear screen
        screen.fill((0, 0, 0))
        my_ball.update()
        my_ball.draw(screen)

        for event in pygame.event.get():

            # Handle quitting via ALT+F4 and window X icon
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(60)
        pygame.display.flip()


if __name__ == '__main__':
    main()
