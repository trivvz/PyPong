from typing import Tuple

import pygame
import numpy as np

from src.config import SCREEN_HEIGHT, SCREEN_WIDTH

PADDLE_COLOR = (255, 255, 255)
PADDLE_SIZE = (5, 50)
PADDLE_STEP = 15


class Paddle:
    color = PADDLE_COLOR
    size = PADDLE_SIZE
    x = int(0.9 * SCREEN_WIDTH)

    def __init__(self, y: float = SCREEN_HEIGHT // 2):
        self.y = y
        self.speed = 0

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
        self.y += self.speed

    def up(self) -> None:
        self.speed = -PADDLE_STEP

    def down(self) -> None:
        self.speed = PADDLE_STEP

    def stop(self) -> None:
        self.speed = 0
