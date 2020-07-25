import unittest

from src import ball


class TestBall(unittest.TestCase):
    def test_ball_x(self):
        test_ball = ball.Ball(10, 20)
        self.assertEqual(test_ball.x, 10)

    def test_ball_y(self):
        test_ball = ball.Ball(10, 20)
        self.assertEqual(test_ball.y, 20)

    def test_ball_color(self):
        test_ball = ball.Ball()
        self.assertEqual(test_ball.color, ball.BALL_COLOR)

    def test_ball_size(self):
        test_ball = ball.Ball()
        self.assertEqual(test_ball.size, ball.BALL_SIZE)
