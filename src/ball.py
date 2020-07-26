import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, pypong_game):
        super(Ball, self).__init__()
        self.screen = pypong_game.screen
        self.settings = pypong_game.settings
        self.screen_rect = pypong_game.screen.get_rect()
        self.color = self.settings.ball_color

        self.rect = pygame.Rect(
            0, 0, self.settings.ball_radius, self.settings.ball_radius
        )

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.speed_x = self.settings.ball_speed_x_start
        self.speed_y = self.settings.ball_speed_y_start

        self.is_over = False

    def reset(self, pos, speed):
        pass

    def draw(self) -> None:
        pygame.draw.circle(
            self.screen, self.color, self.rect.center, self.settings.ball_radius,
        )

    def update(self, paddle) -> None:
        if self.rect.right >= self.screen_rect.right:
            self.is_over = True
        if self.rect.left <= self.screen_rect.left or (
            paddle.rect.right >= self.rect.right >= paddle.rect.left
            and paddle.rect.bottom >= self.rect.bottom >= paddle.rect.top
        ):
            self.speed_x *= -1
        if (
            self.rect.top <= self.screen_rect.top
            or self.rect.bottom >= self.screen_rect.bottom
        ):
            self.speed_y *= -1

        self.x += self.speed_x
        self.y += self.speed_y

        self.rect.x = self.x
        self.rect.y = self.y
