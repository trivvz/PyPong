from typing import Tuple

import  pygame
import numpy as np

BALL_COLOR = (255, 255, 255)
BALL_SIZE = 5


class Ball:
    color = BALL_COLOR
    radius = BALL_SIZE

    def __init__(self, pos: Tuple[int, int] = (0, 0), speed: Tuple[int, int] = (1, 1)):
        self.pos = np.array(pos)
        self.speed = np.array(speed)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

    def update(self) -> None:
        self.pos += self.speed
