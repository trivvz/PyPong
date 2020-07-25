from typing import Tuple

import  pygame
import numpy as np

BALL_COLOR = (255, 255, 255)
BALL_SIZE = 5


class Ball:
    color = BALL_COLOR
    radius = BALL_SIZE

    def __init__(self, pos: Tuple[int, int] = (0, 0), speed: Tuple[int, int] = (1, 1)):
        self.pos = np.array(pos, dtype=np.float64)
        self.speed = np.array(speed, dtype=np.float64)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.radius)

    def update(self) -> None:
        self.pos += self.speed
