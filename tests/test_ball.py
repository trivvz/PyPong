import unittest

import numpy as np

from src import ball, paddle
from src.config import SCREEN_HEIGHT


class TestBall(unittest.TestCase):
    def test_ball_pos_x(self):
        test_ball = ball.Ball((10, 20))
        self.assertEqual(test_ball.x, 10)

    def test_ball_pos_y(self):
        test_ball = ball.Ball((10, 20))
        self.assertEqual(test_ball.y, 20)

    def test_ball_speed_x(self):
        test_ball = ball.Ball((10, 20), (50, 60))
        self.assertEqual(test_ball.speed_x, 50)

    def test_ball_speed_y(self):
        test_ball = ball.Ball((10, 20), (50, 60))
        self.assertEqual(test_ball.speed_y, 60)

    def test_ball_color(self):
        test_ball = ball.Ball()
        self.assertEqual(test_ball.color, ball.BALL_COLOR)

    def test_ball_size(self):
        test_ball = ball.Ball()
        self.assertEqual(test_ball.radius, ball.BALL_SIZE)

    def test_ball_update(self):
        test_ball = ball.Ball((25, 75), (5, -5))
        test_paddle = paddle.Paddle()
        test_ball.update(test_paddle)
        self.assertEqual(test_ball.x, 30)
        self.assertEqual(test_ball.y, 70)

    def test_ball_update_float(self):
        test_ball = ball.Ball((25, 75), (5.5, -5.1))
        test_paddle = paddle.Paddle()
        test_ball.update(test_paddle)
        self.assertEqual(test_ball.x, 30.5)
        self.assertEqual(test_ball.y, 69.9)

    def test_ball_update_change_direction(self):
        test_ball = ball.Ball((0, SCREEN_HEIGHT), (-10, 5))
        test_paddle = paddle.Paddle()
        test_ball.update(test_paddle)
        self.assertEqual(test_ball.x, 10)
        self.assertEqual(test_ball.y, SCREEN_HEIGHT - 5)
