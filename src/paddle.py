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
        self.y: int = 0  # only defined here, value assigned in _prep()
        self._prep()

    def center_paddle(self) -> None:
        self._prep()

    def update(self) -> None:
        # TODO: take paddle acceleration into account using mouse.get_rel()
        self.y = pygame.mouse.get_pos()[1]
        self.rect.centery = self.y
        if self.rect.top < self.screen_rect.top:
            self.rect.top = self.screen_rect.top
        elif self.rect.bottom > self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.bottom

    def draw(self) -> None:
        pygame.draw.rect(
            self.screen, self.color, self.rect,
        )

    def _prep(self) -> None:
        self.rect.centery = self.screen_rect.centery
        self.y = self.rect.y
