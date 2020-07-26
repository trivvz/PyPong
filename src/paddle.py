import pygame

# TODO: find a way to simplify computation of rectangle sides


class Paddle(pygame.sprite.Sprite):
    def __init__(self, pypong_game):
        super(Paddle, self).__init__()
        self.screen = pypong_game.screen
        self.settings = pypong_game.settings
        self.screen_rect = pypong_game.screen.get_rect()
        self.color = self.settings.paddle_color

        # Get the paddle rect
        self.rect = pygame.Rect(
            0, 0, self.settings.paddle_size_x, self.settings.paddle_size_y
        )

        # Place the rect
        self.rect.centerx = self.settings.paddle_x
        self.rect.centery = self.screen_rect.centery

        self.y = float(self.rect.y)

        # Movement flags
        self.is_moving_up = False
        self.is_moving_down = False

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

    def up(self) -> None:
        self.is_moving_up = True
        self.is_moving_down = False

    def down(self) -> None:
        self.is_moving_up = False
        self.is_moving_down = True

    def stop(self) -> None:
        self.is_moving_up = False
        self.is_moving_down = False

    def center_paddle(self) -> None:
        self.rect.centery = self.screen_rect.centery
        self.y = float(self.rect.y)
