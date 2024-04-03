import pygame
import random
import pygame

class Obstacle:
    def __init__(self, screen, color, rect):
        self.screen = screen
        self.color = color
        self.rect = rect
    def draw(self, centered_x, centered_y, CELL_SIZE):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(centered_x, centered_y, CELL_SIZE, CELL_SIZE))

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