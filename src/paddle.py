import pygame


class Paddle(pygame.sprite.Sprite):
    def __init__(self, pypong_game):
        super(Paddle, self).__init__()
        self.screen = pypong_game.screen
        self.settings = pypong_game.settings
        self.screen_rect = pypong_game.screen.get_rect()
        self.color = self.settings.paddle_color

        self.rect = pygame.Rect(
            0, 0, self.settings.paddle_size_x, self.settings.paddle_size_y
        )

        self.rect.centerx = self.settings.paddle_x
        self.y: float = 0.0
        self.accel_y: int = 0

        self.accel_max = 0
        self.accel_min = 0

    def center_paddle(self) -> None:
        pygame.mouse.set_pos(pygame.mouse.get_pos()[0], self.screen_rect.centery)

    def update(self) -> None:
        self.y = pygame.mouse.get_pos()[1]
        self.accel_y = pygame.mouse.get_rel()[1]

        self.rect.centery = self.y
        if self.rect.top < self.screen_rect.top:
            self.rect.top = self.screen_rect.top
        elif self.rect.bottom > self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.bottom

    def draw(self) -> None:
        pygame.draw.rect(
            self.screen, self.color, self.rect,
        )


class PaddleAI(Paddle):
    def __init__(self, pypong_game):
        super(PaddleAI, self).__init__(pypong_game)
        self.ball = pypong_game.ball
        self.rect.centerx = self.settings.paddle_x_ai

    def update(self) -> None:
        self.y = self.ball.y
        self.rect.centery = self.y
        if self.rect.top < self.screen_rect.top:
            self.rect.top = self.screen_rect.top
        elif self.rect.bottom > self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.bottom
