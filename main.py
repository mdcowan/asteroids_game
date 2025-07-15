import sys
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import everything from the module
# constants.py into the current file
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # initializing imported module
    pygame.init()

    # Setting name for the game window
    pygame.display.set_caption('Asteroids')

    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create an object to help track time
    clock = pygame.time.Clock()
    dt = 0

    # create game groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # set the group containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # create the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteriod_field = AsteroidField()

    # Game loop
    # keep game running till running is true
    while True:  
        # Check for event if user has pressed te close button
        for event in pygame.event.get():            
            # if event is of type quit then exit the program
            if event.type == pygame.QUIT:
                return
        
        # fill the screen with a solid "black" color.
        screen.fill("black")

        # update the player position
        updatable.update(dt)

        # check for player collisions with the asteroids
        for asteroid in asteroids:
            if player.check_for_collision(asteroid):
                sys.exit("Game over!")
            

        #render everything on the screeen
        for thing in drawable:
            thing.draw(screen)
        
        # refresh the screen
        pygame.display.flip()

        # pause the game loop until 1/60th of a second has passed using .tick()
        # this returns the amount of time that has passed since
        # the last time it was called: the delta time
        # convert the delta time from milliseconds to seconds and save the result
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
