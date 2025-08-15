import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):            
        pygame.draw.circle(screen, "white", tuple(map(int, self.position)), self.radius, width=2)

    def update(self, dt):
      self.position += (self.velocity * dt)
      return self.position

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)
            vector_one = self.velocity.rotate(rand_angle)
            vector_two = self.velocity.rotate(rand_angle * -1)
            self.radius -= ASTEROID_MIN_RADIUS
            ast_one = Asteroid(self.position.x, self.position.y, self.radius)
            ast_two = Asteroid(self.position.x, self.position.y, self.radius)
            ast_one.velocity = vector_one * 1.2
            ast_two.velocity = vector_two * 1.2
