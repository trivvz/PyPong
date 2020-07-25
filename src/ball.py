from typing import Tuple

import pygame
import numpy as np

from src.config import SCREEN_HEIGHT, SCREEN_WIDTH

BALL_COLOR = (255, 255, 255)
BALL_SIZE = 5


class Ball:
    color = BALL_COLOR
    radius = BALL_SIZE

    def __init__(self, pos: tuple = (0, 0), speed: tuple = (1, 1)):
        self.pos = np.array(pos, dtype=np.float64)
        self.speed = np.array(speed, dtype=np.float64)

    def draw(self, screen) -> None:
        pygame.draw.circle(
            screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.radius
        )

    def update(self) -> None:
        if self.pos[0] <= 0 or self.pos[0] >= SCREEN_WIDTH:
            self.speed[0] *= -1
        if self.pos[1] <= 0 or self.pos[1] >= SCREEN_HEIGHT:
            self.speed[1] *= -1

        self.pos += self.speed
