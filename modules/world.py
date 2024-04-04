import pygame
import random
import pygame

import pygame

class Obstacle:
    def __init__(self, screen, image, rect):
        self.screen = screen
        self.image = image  # Image for the obstacle
        self.rect = rect  # pygame.Rect object for position and size

    def draw(self, x, y, cell_size):
        # Adjust the position based on the given x, y, and cell size
        # Note: Assuming the image size matches the cell size. If not, you might need to scale the image.
        self.screen.blit(self.image, (x, y))

    def spawn_trees_blocks(map, num_blocks, block_value=2):
        rows = len(map)
        cols = len(map[0])
        for _ in range(num_blocks):
            placed = False
            while not placed:
                x = random.randint(0, cols - 1)
                y = random.randint(0, rows - 1)
                if map[y][x] == 0:
                    map[y][x] = block_value
                    placed = True
    
    def spawn_sticks(map, num_sticks, block_value=4):
        rows = len(map)
        cols = len(map[0])
        for _ in range(num_sticks):
            placed = False
            while not placed:
                x = random.randint(0, cols - 1)
                y = random.randint(0, rows - 1)
                if map[y][x] == 0:  # Check if the position is empty
                    map[y][x] = block_value  # 4 represents a stick (brown rectangle)
                    placed = True