import pygame
import pygame.freetype
import os
import sys
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

    # Score
    score = 0

    # score_surface = pygame.surface.Surface((10,10))
    score_font = pygame.freetype.SysFont("Comic Sans",18)
    
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
                    score += 1
                    asteroid.split()

            if player.collision(asteroid):
                print("GAME OVER!")
                exit(0)
        
        for item in drawable:
            item.draw(screen)

        
        score_font_text = score_font.render(f"SCORE:{score}", (200, 226, 232))
        screen.blit(score_font_text[0], (SCORE_TEXT_POS[0],SCORE_TEXT_POS[1]))
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
