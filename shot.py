# shot.py
import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    containers = []

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        for group in Shot.containers:
            group.add(self)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 0),  # yellow bullets
            (int(self.position.x), int(self.position.y)),
            self.radius,
            2
        )
