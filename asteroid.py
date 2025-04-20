from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        
        for group in Asteroid.containers:
            group.add(self)

    def split(self):
        # Step 1: Kill this asteroid
        self.kill()

        # Step 2: Don't split if already smallest size
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Step 3: Split into two smaller asteroids
        angle = random.uniform(20, 50)

        # Two new vectors rotated left/right from original velocity
        dir1 = self.velocity.rotate(angle) * 1.2
        dir2 = self.velocity.rotate(-angle) * 1.2

        # New radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Spawn two new asteroids
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = dir1

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = dir2

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
