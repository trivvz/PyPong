import sys

import pygame

from src import ball, paddle
from src.config import SCREEN_HEIGHT, SCREEN_WIDTH

SCREEN_RECT = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)


def main():
    pygame.init()
    pygame.display.set_caption("PyPong")
    screen = pygame.display.set_mode(SCREEN_RECT.size)
    clock = pygame.time.Clock()

    pygame.draw.circle(screen, (255, 255, 255), (100, 100), 10)

    my_ball = ball.Ball((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), (5, 5))
    my_paddle = paddle.Paddle()

    while True:
        # Clear screen
        screen.fill((0, 0, 0))
        my_paddle.update()
        my_ball.update(my_paddle)

        for event in pygame.event.get():

            # Handle quitting via ALT+F4 and window X icon
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    my_paddle.up()

                if event.key == pygame.K_DOWN:
                    my_paddle.down()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    my_paddle.stop()

        clock.tick(60)

        my_paddle.draw(screen)
        my_ball.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
