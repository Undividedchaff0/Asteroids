import pygame

import circleshape
from constants import LINES_WIDTH


class Asteroid(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface, color: tuple[int, int, int] = (255, 255, 255), width: int = LINES_WIDTH) -> None:
        pygame.draw.circle(screen, color, self.position, self.radius, width)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
