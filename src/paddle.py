import pygame

# TODO: find a way to simplify computation of rectangle sides


class Paddle:
    def __init__(self, pypong_game):
        self.screen = pypong_game.screen
        self.settings = pypong_game.settings
        self.color = self.settings.paddle_color
        self.size = (self.settings.paddle_size_x, self.settings.paddle_size_y)
        self.x = self.settings.paddle_x
        self.speed = self.settings.paddle_speed
        self.y = self.settings.paddle_y_start
        self.is_up = False
        self.is_down = False

    def draw(self) -> None:
        pygame.draw.rect(
            self.screen,
            self.color,
            pygame.Rect(
                self.x - self.size[0] // 2,
                self.y - self.size[1] // 2,
                self.size[0],
                self.size[1],
            ),
        )

    def update(self) -> None:
        if self.is_up and self.y - self.size[1] // 2 >= 0:
            self.y -= self.speed
        elif self.is_down and self.y + self.size[1] // 2 <= self.settings.screen_height:
            self.y += self.speed

        self.y = self.y

    def up(self) -> None:
        self.is_up = True
        self.is_down = False

    def down(self) -> None:
        self.is_up = False
        self.is_down = True

    def stop(self) -> None:
        self.is_up = False
        self.is_down = False
