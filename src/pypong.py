import sys

import pygame

from src import ball, paddle, settings, button, game_stats, scoreboard, sounds


class PyPong:
    def __init__(self):
        pygame.init()
        self.settings = settings.Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("PyPong")

        # Setup sounds
        pygame.mixer.init()
        self.is_sound_enabled = True
        self.sounds = sounds.Sounds()

        self.is_game_active = False  # game is active as long as ball is moving
        self.is_game_restarted = True  # game is restarted after every lost ball
        self.stats = game_stats.GameStats()
        self.scoreboard = scoreboard.Scoreboard(self)

        # Create game objects
        self.ball = ball.Ball(self)
        self.paddle = paddle.Paddle(self)
        self.paddle_ai = paddle.PaddleAI(self)

        self.play_text = button.Button(self, "Play")
        self.pause_text = button.Button(self, "Paused")

    def run_game(self) -> None:
        while True:
            self._check_events()

            if self.is_game_active:
                self.paddle.update()
                self.paddle_ai.update()
                self.ball.update()
                self.scoreboard.update()
                self._check_collisions()

            self._update_screen()

            self.clock.tick(self.settings.ticks_per_sec)

    def _start_game(self) -> None:
        """Start game after selecting Play option (RETURN key)"""
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)
        self.is_game_restarted = False
        self.is_game_active = True
        self.stats.reset_stats()
        self.paddle.center_paddle()
        self.ball.center_ball()

    def _stop_game(self) -> None:
        """Stop game after losing a ball"""
        self.is_game_restarted = True
        self.is_game_active = False
        pygame.mouse.set_visible(True)
        pygame.event.set_grab(False)

    def _check_collisions(self) -> None:
        self._check_ball_wall_collision()
        self._check_ball_paddle_collision()
        self._check_ball_paddle_ai_collision()

    def _check_ball_wall_collision(self) -> None:
        if (
            self.ball.rect.right >= self.screen_rect.right
            or self.ball.rect.left <= self.screen_rect.left
        ):
            self._stop_game()
            print(f"min: {self.paddle.accel_min}\nmax: {self.paddle.accel_max}\n")
            self.paddle.accel_min = 0
            self.paddle.accel_max = 0
        elif self.ball.rect.left <= self.screen_rect.left:
            self.ball.speed_x *= -1
        elif (
            self.ball.rect.top <= self.screen_rect.top
            or self.ball.rect.bottom >= self.screen_rect.bottom
        ):
            self.ball.speed_y *= -1
            self.sounds.hit.play()

    def _check_ball_paddle_collision(self) -> None:
        if (
            pygame.Rect.colliderect(self.ball.rect, self.paddle.rect)
            and self.paddle.rect.left + self.ball.speed_x >= self.ball.rect.right
        ):
            # TODO: replace print with logging if still needed
            print(f"hit: {self.paddle.accel_y}")
            self.ball.speed_x *= -1
            print(f"old speed: {self.ball.speed_y}")
            self.ball.speed_y += round(self.paddle.accel_y / 10, 1)
            print(f"new speed: {self.ball.speed_y}\n")

            self.paddle.accel_max = max(self.paddle.accel_max, self.paddle.accel_y)
            self.paddle.accel_min = min(self.paddle.accel_min, self.paddle.accel_y)

            self.stats.score += 1
            self.scoreboard.update()
            self.sounds.player1.play()

    def _check_ball_paddle_ai_collision(self) -> None:
        if pygame.Rect.colliderect(self.ball.rect, self.paddle_ai.rect):
            self.ball.speed_x *= -1
            self.sounds.player2.play()

    def _check_events(self) -> None:
        for event in pygame.event.get():
            # Handle quitting via ALT+F4 and window X icon
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # LMB
                    if self.is_game_restarted and self.screen_rect.collidepoint(
                        pygame.mouse.get_pos()
                    ):  # clicking anywhere on game screen will start the game
                        self._start_game()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event) -> None:
        if event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_m:
            self.is_sound_enabled = self.sounds.mute(
                self.is_sound_enabled,
                self.sounds.player1,
                self.sounds.player2,
                self.sounds.hit,
            )
        elif event.key == pygame.K_RETURN and self.is_game_restarted:
            self._start_game()
        elif event.key == pygame.K_ESCAPE:  # pause/unpause the game
            self.is_game_active = not self.is_game_active
            if self.is_game_active:
                pygame.mouse.set_visible(False)
                pygame.event.set_grab(True)
            else:
                pygame.mouse.set_visible(True)
                pygame.event.set_grab(False)

    def _update_screen(self) -> None:
        self.screen.fill(self.settings.bg_color)

        if self.is_game_restarted:
            self.play_text.draw()
        elif not self.is_game_active:
            self.pause_text.draw()
            self._draw_dynamic_objects()
        else:
            self._draw_dynamic_objects()

        pygame.display.flip()

    def _draw_dynamic_objects(self) -> None:
        self.paddle.draw()
        self.paddle_ai.draw()
        self.ball.draw()
        self.scoreboard.draw()
