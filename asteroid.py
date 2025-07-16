import pygame
import random
from circleshape import CircleShape
from constants import *

# Sub-class for asteroid objects
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else: 
            # generate a random angle between 20 and 50 degrees.
            random_angle = random.uniform(20, 50)
            # create 2 new vectors, that are rotated
            new_velocity_1 = self.velocity.rotate(random_angle)
            new_velocity_2 = self.velocity.rotate(-random_angle)
            # lower the radius
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            # Create two new Asteroid objects at the current asteroid position with the new radius
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            # Set the new velocity
            new_asteroid_1.velocity = new_velocity_1 * 1.2
            new_asteroid_2.velocity = new_velocity_2 * 1.2


