import pygame
from constants import *
from asteroid import Asteroid 
from asteroid_field import AsteroidField
from player import Player
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable,shots)
    Shot.containers = (updatable, drawable,shots)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT / 2)

    dt = 0 #Delta-Time

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill("black")
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

            if player.collision(asteroid):
                print("GAME OVER!")
                exit(0)
        
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
