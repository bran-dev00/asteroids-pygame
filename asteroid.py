import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)

         # Random Angle they will go in oposite directions
            vector_1 = self.velocity.rotate(angle)
            vector_2 = self.velocity.rotate(-angle)
        
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid_1 = Asteroid(self.position[0],self.position[1],new_radius)
            new_asteroid_2 = Asteroid(self.position[0],self.position[1],new_radius)

            new_asteroid_1.velocity = vector_1 * 2
            new_asteroid_2.velocity = vector_2 * 1.2
        
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        

        

