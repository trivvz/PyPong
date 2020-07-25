import unittest

from src.ball import Ball, BALL_SIZE, BALL_COLOR


class TestBall(unittest.TestCase):
    def test_ball_x(self):
        ball = Ball(10, 20)
        self.assertEqual(ball.x, 10)

    def test_ball_y(self):
        ball = Ball(10, 20)
        self.assertEqual(ball.y, 20)

    def test_ball_color(self):
        ball = Ball()
        self.assertEqual(ball.color, BALL_COLOR)

    def test_ball_size(self):
        ball = Ball()
        self.assertEqual(ball.size, BALL_SIZE)
