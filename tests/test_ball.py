import unittest

import numpy as np

from src import ball


class TestBall(unittest.TestCase):
    def test_ball_pos_x(self):
        test_ball = ball.Ball((10, 20))
        self.assertEqual(test_ball.pos[0], 10)

    def test_ball_pos_y(self):
        test_ball = ball.Ball((10, 20))
        self.assertEqual(test_ball.pos[1], 20)

    def test_ball_speed_x(self):
        test_ball = ball.Ball((10, 20), (50, 60))
        self.assertEqual(test_ball.speed[0], 50)

    def test_ball_speed_y(self):
        test_ball = ball.Ball((10, 20), (50, 60))
        self.assertEqual(test_ball.speed[1], 60)

    def test_ball_color(self):
        test_ball = ball.Ball()
        self.assertEqual(test_ball.color, ball.BALL_COLOR)

    def test_ball_size(self):
        test_ball = ball.Ball()
        self.assertEqual(test_ball.radius, ball.BALL_SIZE)

    def test_ball_update(self):
        test_ball = ball.Ball((25, 75), (5, -5))
        test_ball.update()
        self.assertEqual(test_ball.pos[0], 30)
        self.assertEqual(test_ball.pos[1], 70)

    def test_ball_update_float(self):
        test_ball = ball.Ball((25, 75), (5.5, -5.1))
        test_ball.update()
        self.assertEqual(test_ball.pos[0], 30.5)
        self.assertEqual(test_ball.pos[1], 69.9)
