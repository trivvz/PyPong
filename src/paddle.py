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
        self.y: float

    def center_paddle(self) -> None:
        pygame.mouse.set_pos(pygame.mouse.get_pos()[0], self.screen_rect.centery)

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
