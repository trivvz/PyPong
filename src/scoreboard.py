import pygame


class Scoreboard:
    def __init__(self, pypong_game):
        self.pypong_game = pypong_game
        self.screen = pypong_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = pypong_game.settings
        self.stats = pypong_game.stats

        self.text_color = pygame.Color("white")
        self.font = pygame.font.SysFont(None, 48)

        self._prep()

    def update(self) -> None:
        self._prep()

    def draw(self) -> None:
        self.screen.blit(self.score_image, self.score_rect)

    def _prep(self) -> None:
        self.score_image = self.font.render(
            str(self.stats.score), True, self.text_color, self.settings.bg_color
        )
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = 20
