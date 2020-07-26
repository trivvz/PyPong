import unittest

from src import ball, pypong


class TestBall(unittest.TestCase):
    def setUp(self):
        self.pypong_game = pypong.PyPong()
        self.settings = self.pypong_game.settings
        self.test_ball = ball.Ball(self.pypong_game)

    def test_ball_speed_x(self):
        self.assertEqual(self.test_ball.speed_x, self.settings.ball_speed_x_start)

    def test_ball_speed_y(self):
        self.assertEqual(self.test_ball.speed_y, self.settings.ball_speed_y_start)
