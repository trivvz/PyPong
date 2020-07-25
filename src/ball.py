BALL_COLOR = "black"
BALL_SIZE = 5


class Ball:
    color = BALL_COLOR
    size = BALL_SIZE

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

