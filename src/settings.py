from dataclasses import dataclass

import pygame


@dataclass
class Settings:
    screen_width = 1280
    screen_height = 720

    paddle_color = pygame.Color("white")
    paddle_size_x = 5
    paddle_size_y = 80
    paddle_speed = 15
    paddle_x = int(0.95 * screen_width)

    ball_color = pygame.Color("white")
    ball_radius = 5
    ball_speed_x_start = 5
    ball_speed_y_start = 5
