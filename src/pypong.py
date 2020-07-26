import sys

import pygame

from src import ball, paddle, settings, button, game_stats, scoreboard


class PyPong:
    def __init__(self):
        pygame.init()
        self.settings = settings.Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("PyPong")

        self.is_game_active = False
        self.stats = game_stats.GameStats()
        self.scoreboard = scoreboard.Scoreboard(self)

        # Create game objects
        self.paddle = paddle.Paddle(self)
        self.ball = ball.Ball(self)

        self.play_button = button.Button(self, "Play")

    def run_game(self) -> None:
        while True:
            self._check_events()

            if self.is_game_active:
                self.paddle.update()
                self.ball.update()
                self.scoreboard.update()
                self._check_collisions()

            self._update_screen()

            self.clock.tick(self.settings.ticks_per_sec)

    def _start_game(self) -> None:
        self.is_game_active = True
        self.stats.reset_stats()
        self.paddle.center_paddle()
        self.ball.center_ball()

    def _check_collisions(self) -> None:
        self._check_ball_wall_collision()
        self._check_ball_paddle_collision()

    def _check_ball_wall_collision(self) -> None:
        if self.ball.rect.right >= self.ball.screen_rect.right:
            self.is_game_active = False
        elif self.ball.rect.left <= self.ball.screen_rect.left:
            self.ball.speed_x *= -1
        elif (
            self.ball.rect.top <= self.ball.screen_rect.top
            or self.ball.rect.bottom >= self.ball.screen_rect.bottom
        ):
            self.ball.speed_y *= -1

    def _check_ball_paddle_collision(self) -> None:
        if (
            self.paddle.rect.right >= self.ball.rect.right >= self.paddle.rect.left
            and self.paddle.rect.bottom >= self.ball.rect.bottom >= self.paddle.rect.top
        ):
            self.ball.speed_x *= -1
            self.stats.score += 1
            self.scoreboard.update()

    def _check_events(self) -> None:
        for event in pygame.event.get():

            # Handle quitting via ALT+F4 and window X icon
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event) -> None:
        if event.key == pygame.K_UP:
            self.paddle.is_moving_up = True
        elif event.key == pygame.K_DOWN:
            self.paddle.is_moving_down = True
        elif event.key == pygame.K_RETURN and not self.is_game_active:
            self._start_game()

    def _check_keyup_events(self, event) -> None:
        if event.key == pygame.K_UP:
            self.paddle.is_moving_up = False
        elif event.key == pygame.K_DOWN:
            self.paddle.is_moving_down = False

    def _update_screen(self) -> None:
        self.screen.fill(self.settings.bg_color)

        if not self.is_game_active:
            self.play_button.draw()
        else:
            self.paddle.draw()
            self.ball.draw()
            self.scoreboard.draw()

        pygame.display.flip()
