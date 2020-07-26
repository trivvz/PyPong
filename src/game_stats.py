from dataclasses import dataclass


@dataclass
class GameStats:
    score = 0

    def reset_stats(self) -> None:
        self.score = 0
