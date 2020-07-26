import pygame


class Button:
    def __init__(self, pypong_game, msg):
        self.screen = pypong_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = pypong_game.settings

        self.width = 200
        self.height = 50
        self.text_color = pygame.Color("white")
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep(msg)

    def draw(self) -> None:
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def _prep(self, msg) -> None:
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.settings.bg_color
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
