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

    def center_ball(self) -> None:
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.speed_x = self.settings.ball_speed_x_start
        self.speed_y = self.settings.ball_speed_y_start

    def draw(self) -> None:
        pygame.draw.circle(
            self.screen, self.color, self.rect.center, self.settings.ball_radius,
        )

    def update(self) -> None:
        self.x += self.speed_x
        self.y += self.speed_y

        self.rect.x = self.x
        self.rect.y = self.y
