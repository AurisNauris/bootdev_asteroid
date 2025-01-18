import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatables, drawables)

    AsteroidField.containers = (updatables)
    asteroidfield = AsteroidField()

    shots = pygame.sprite.Group()
    # Maybe ?
    Shot.containers = (shots, updatables, drawables)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for item in updatables:
            item.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                return
        screen.fill((200,200,200))
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

        

if __name__ == "__main__":
    main()