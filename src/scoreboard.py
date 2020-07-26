import pygame


class Scoreboard:
    def __init__(self, pypong_game):
        self.pypong_game = pypong_game
        self.screen = pypong_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = pypong_game.settings
        self.stats = pypong_game.stats

        # Font settings for scoring information.
        self.text_color = pygame.Color("white")
        self.font = pygame.font.SysFont(None, 48)

        self.score_image, self.score_rect = None, None

        self.prep_score()

    def prep_score(self) -> None:
        # Prepare the initial images.
        self.score_image = self.font.render(
            str(self.stats.score), True, self.text_color, self.settings.bg_color
        )
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = 20

    def draw(self) -> None:
        self.screen.blit(self.score_image, self.score_rect)
