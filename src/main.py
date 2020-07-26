import sys, random

import pygame

from src import ball, paddle
from src.config import SCREEN_HEIGHT, SCREEN_WIDTH

SCREEN_RECT = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)


class PyPong:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("PyPong")

        # Create game objects
        self.paddle = paddle.Paddle()
        self.ball = ball.Ball()

    def run_game(self):
        while True:
            self._check_events()

            self.paddle.update()
            self.ball.update(self.paddle)
            self._update_screen()

            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():

            # Handle quitting via ALT+F4 and window X icon
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.paddle.up()
        if event.key == pygame.K_DOWN:
            self.paddle.down()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            self.paddle.stop()

    def _update_screen(self):
        self.screen.fill(pygame.Color("black"))
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    pypong = PyPong()
    pypong.run_game()
