# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import everything from the module
# constants.py into the current file
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS, PLAYER_RADIUS
from player import Player

def main():
    # initializing imported module
    pygame.init()

    # Setting name for the game window
    pygame.display.set_caption('Asteroids')

    # creating a bool value which checks 
    # if the game is running
    running = True

    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create an object to help track time
    clock = pygame.time.Clock()
    dt = 0

    # create the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

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
        player.update(dt)

        #render the player
        player.draw(screen)
        
        # refresh the screen
        pygame.display.flip()

        # pause the game loop until 1/60th of a second has passed using .tick()
        # this returns the amount of time that has passed since
        # the last time it was called: the delta time
        # convert the delta time from milliseconds to seconds and save the result
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
