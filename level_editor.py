import pygame
import constants


class Level_Editor():
    def __init__(self):
        # Grid variables
        self.ROWS = 18
        self.COLS = 32
        # Double division returns only integers
        self.TILE_SIZE = constants.HEIGHT // self.ROWS

    # Draw Grid
    def draw_grid(self):
        # Vertical lines
        for c in range(self.COLS + 1):
            pygame.draw.line(constants.SCREEN, constants.WHITE, (c *
                             self.TILE_SIZE, 0), (c * self.TILE_SIZE, constants.HEIGHT))
        # Horizontal lines
        for r in range(self.ROWS + 1):
            pygame.draw.line(constants.SCREEN, constants.WHITE, (0, r *
                             self.TILE_SIZE), (constants.WIDTH, r * self.TILE_SIZE))
