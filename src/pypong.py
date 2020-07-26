import sys, random

import pygame

from src import ball, paddle, settings


class PyPong:
    def __init__(self):
        pygame.init()
        self.settings = settings.Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("PyPong")

        # Create game objects
        self.paddle = paddle.Paddle(self)
        self.ball = ball.Ball(self)

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
            self.paddle.is_moving_up = True
        elif event.key == pygame.K_DOWN:
            self.paddle.is_moving_down = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.paddle.is_moving_up = False
        elif event.key == pygame.K_DOWN:
            self.paddle.is_moving_down = False

    def _update_screen(self):
        self.screen.fill(pygame.Color("black"))
        self.paddle.draw()
        self.ball.draw()

        pygame.display.flip()
