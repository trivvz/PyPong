from dataclasses import dataclass

import pygame


@dataclass
class Settings:
    screen_width = 1280
    screen_height = 720

    paddle_x = 0.95 * screen_width
    paddle_y_start = screen_height // 2
    paddle_size_x = 5
    paddle_size_y = 80
    paddle_color = pygame.Color("white")
    paddle_speed = 15

    ball_radius = 5
    ball_color = pygame.Color("white")
    ball_x_start = screen_width // 2
    ball_y_start = screen_height // 2
    ball_speed_x_start = 5
    ball_speed_y_start = 5
