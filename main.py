# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import everything from the module
# constants.py into the current file
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS

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
        
        # refresh the screen
        pygame.display.flip()



if __name__ == "__main__":
    main()
