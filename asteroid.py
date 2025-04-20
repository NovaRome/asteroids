from circleshape import CircleShape
from constants import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        
        for group in Asteroid.containers:
            group.add(self)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(self.position.x), int(self.position.y)),
            self.radius,
            2
        )

    def collision(self,other):
        distance = self.position.distance_to(other.position)
        return distance < (self.radius + other.radius)
