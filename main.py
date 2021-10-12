import pygame
from pygame.constants import K_ESCAPE, KEYDOWN
import constants
import level_editor


# Name of game in window
pygame.display.set_caption('Top-Down RPG')


class Main():
    def __init__(self):
        # Game variables

        # Frames
        self.clock = pygame.time.Clock()
        self.frames_per_second = 60

    def run(self):
        running = True

        # Game Loop
        while running == True:

            # Game frames per second
            self.clock.tick(self.frames_per_second)

            # Exit game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # Escape key
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        return

            # Game window
            constants.SCREEN.fill((0, 0, 0))

            # Call draw grid
            level_editor.Level_Editor().draw_grid()

            # Displays the screen
            pygame.display.flip()


# Runs only main class
if __name__ == '__main__':
    Main().run()
