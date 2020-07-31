import pygame


class Sounds:
    def __init__(self):
        self.player1 = pygame.mixer.Sound("sounds/player1.wav")
        self.player2 = pygame.mixer.Sound("sounds/player2.wav")
        self.hit = pygame.mixer.Sound("sounds/hit.wav")

    @staticmethod
    def mute(is_enabled, *sounds) -> bool:
        """Mute/unmute any given sounds."""
        for sound in sounds:
            if is_enabled:
                sound.set_volume(0)
            else:
                sound.set_volume(1)
        return not is_enabled
