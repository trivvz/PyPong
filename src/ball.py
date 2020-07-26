from typing import Tuple

import pygame
import numpy as np

from src.config import SCREEN_HEIGHT, SCREEN_WIDTH

BALL_SIZE = 5


class Ball:
    color = pygame.Color("white")
    radius = BALL_SIZE
    x_init = SCREEN_WIDTH // 2
    y_init = SCREEN_HEIGHT // 2
    speed_x_init = 5
    speed_y_init = 5

    def __init__(
        self, pos: tuple = None, speed: tuple = None,
    ):
        self.x = self.x_init if pos is None else pos[0]
        self.y = self.y_init if pos is None else pos[1]
        self.speed_x = self.speed_x_init if speed is None else speed[0]
        self.speed_y = self.speed_y_init if speed is None else speed[1]
        self.is_over = False

    def reset(self, pos, speed):
        self.x = self.x_init if pos is None else pos[0]
        self.y = self.y_init if pos is None else pos[1]
        self.speed_x = self.speed_x_init if speed is None else speed[0]
        self.speed_y = self.speed_y_init if speed is None else speed[1]
        self.is_over = False

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self, paddle) -> None:
        if self.x >= SCREEN_WIDTH:
            self.is_over = True
        if self.x <= 0 or (
            paddle.x + paddle.size[0] / 2 >= self.x >= paddle.x - paddle.size[0] / 2
            and paddle.y + paddle.size[1] / 2 >= self.y >= paddle.y - paddle.size[1]
        ):
            self.speed_x *= -1
        if self.y <= 0 or self.y >= SCREEN_HEIGHT:
            self.speed_y *= -1

        self.x += self.speed_x
        self.y += self.speed_y
