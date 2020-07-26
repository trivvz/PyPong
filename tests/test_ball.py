import unittest

import pygame

from src import ball, paddle, settings, pypong


class TestBall(unittest.TestCase):
    def setUp(self):
        self.pypong_game = pypong.PyPong()
        self.settings = self.pypong_game.settings
        self.test_ball = ball.Ball(self.pypong_game)

    def test_ball_speed_x(self):
        self.assertEqual(self.test_ball.speed_x, self.settings.ball_speed_x_start)

    def test_ball_speed_y(self):
        self.assertEqual(self.test_ball.speed_y, self.settings.ball_speed_y_start)

    # def test_ball_update(self):
    #     test_ball = ball.Ball((25, 75), (5, -5))
    #     test_paddle = paddle.Paddle()
    #     test_ball.update(test_paddle)
    #     self.assertEqual(test_ball.x, 30)
    #     self.assertEqual(test_ball.y, 70)
    #
    # def test_ball_update_float(self):
    #     test_ball = ball.Ball((25, 75), (5.5, -5.1))
    #     test_paddle = paddle.Paddle()
    #     test_ball.update(test_paddle)
    #     self.assertEqual(test_ball.x, 30.5)
    #     self.assertEqual(test_ball.y, 69.9)
    #
    # def test_ball_update_change_direction(self):
    #     test_ball = ball.Ball((0, SCREEN_HEIGHT), (-10, 5))
    #     test_paddle = paddle.Paddle()
    #     test_ball.update(test_paddle)
    #     self.assertEqual(test_ball.x, 10)
    #     self.assertEqual(test_ball.y, SCREEN_HEIGHT - 5)
