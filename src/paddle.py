from typing import Tuple

import pygame
import numpy as np

from src.config import SCREEN_HEIGHT, SCREEN_WIDTH

PADDLE_COLOR = (255, 255, 255)
PADDLE_SIZE = (5, 80)
PADDLE_STEP = 10


class Paddle:
    color = PADDLE_COLOR
    size = PADDLE_SIZE
    speed = PADDLE_STEP
    x = int(0.95 * SCREEN_WIDTH)

    def __init__(self, y: float = SCREEN_HEIGHT // 2):
        self.y = round(y, -1)
        self.is_up = False
        self.is_down = False

    def draw(self, screen) -> None:
        pygame.draw.rect(
            screen,
            self.color,
            pygame.Rect(
                self.x - self.size[0] / 2,
                self.y - self.size[1] / 2,
                self.size[0],
                self.size[1],
            ),
        )

    def update(self):
        if self.is_up and self.y - self.size[1] / 2 >= 0:
            self.y -= self.speed
        elif self.is_down and self.y + self.size[1] / 2 <= SCREEN_HEIGHT:
            self.y += self.speed

        self.y = self.y

    def up(self) -> None:
        self.is_up = True
        self.is_down = False

    def down(self) -> None:
        self.is_up = False
        self.is_down = True

    def stop(self) -> None:
        self.is_up = False
        self.is_down = False
