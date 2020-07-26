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
        self._prep()

        # Movement flags
        self.is_moving_up = False
        self.is_moving_down = False

    def center_paddle(self) -> None:
        self._prep()

    def update(self) -> None:
        if self.is_moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.paddle_speed
        if self.is_moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.paddle_speed

        self.rect.y = self.y

    def draw(self) -> None:
        pygame.draw.rect(
            self.screen, self.color, self.rect,
        )

    def _prep(self) -> None:
        self.rect.centery = self.screen_rect.centery
        self.y = float(self.rect.y)
