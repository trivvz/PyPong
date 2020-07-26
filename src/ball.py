from typing import Tuple

import pygame


class Ball:
    def __init__(self, pypong_game):
        self.screen = pypong_game.screen
        self.settings = pypong_game.settings
        self.color = self.settings.ball_color
        self.radius = self.settings.ball_radius
        self.x = self.settings.ball_x_start
        self.y = self.settings.ball_y_start
        self.speed_x = self.settings.ball_speed_x_start
        self.speed_y = self.settings.ball_speed_y_start
        self.is_over = False

    def reset(self, pos, speed):
        pass

    def draw(self) -> None:
        pygame.draw.circle(
            self.screen, self.color, (int(self.x), int(self.y)), self.radius
        )

    def update(self, paddle) -> None:
        if self.x >= self.settings.screen_width:
            self.is_over = True
        if self.x <= 0 or (
            paddle.x + paddle.size[0] / 2 >= self.x >= paddle.x - paddle.size[0] / 2
            and paddle.y + paddle.size[1] / 2 >= self.y >= paddle.y - paddle.size[1]
        ):
            self.speed_x *= -1
        if self.y <= 0 or self.y >= self.settings.screen_height:
            self.speed_y *= -1

        self.x += self.speed_x
        self.y += self.speed_y
