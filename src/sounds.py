import pygame


class Sounds:
    def __init__(self):
        self.player1 = pygame.mixer.Sound("sounds/player1.wav")
        self.player2 = pygame.mixer.Sound("sounds/player2.wav")
        self.hit = pygame.mixer.Sound("sounds/hit.wav")
