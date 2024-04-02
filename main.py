import pygame
import sys
from modules.player import Player
from modules.world import Obstacle
from modules.events import *

def main():
    pygame.init()

    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 600
    MAUVE = (224, 176, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    CELL_SIZE = 20
    
    pygame.display.set_caption("Moving Circle")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    player = Player(screen, WHITE, 20, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 5)
    player.x = SCREEN_WIDTH // 2
    player.y = SCREEN_HEIGHT // 2

    MAP = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 0, 2, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 2, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    
    map_width = len(MAP[0]) * CELL_SIZE
    map_height = len(MAP) * CELL_SIZE

    offset_x = (SCREEN_WIDTH - map_width) // 2
    offset_y = (SCREEN_HEIGHT - map_height) // 2


    world = []
    for y, row in enumerate(MAP):
        for x, cell in enumerate(row):
            if cell == 1:  # Wall
                world.append(Obstacle(screen, BLACK, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)))
            elif cell == 2:  # Tree
                world.append(Obstacle(screen, GREEN, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)))

    # Timer Bar Variables
    bar_value = 100  # Starting at 100%
    last_update_time = pygame.time.get_ticks()  # Get the initial time
    running = True

    while running:
        screen.fill(MAUVE)
        running = handle_events()

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx -= player.speed
        if keys[pygame.K_RIGHT]:
            dx += player.speed
        if keys[pygame.K_UP]:
            dy -= player.speed
        if keys[pygame.K_DOWN]:
            dy += player.speed

        #! Obstacles
        for obstacle in world:
            obstacle.rect.x -= dx
            obstacle.rect.y -= dy
            # Apply offset to center the map
            centered_x = obstacle.rect.x + offset_x
            centered_y = obstacle.rect.y + offset_y
            # Draw the obstacle at the new, centered position
            pygame.draw.rect(screen, obstacle.color, pygame.Rect(centered_x, centered_y, CELL_SIZE, CELL_SIZE))

        #! Timer Bar
        current_time = pygame.time.get_ticks()
        last_update_time, bar_value = update_timer_bar(last_update_time, current_time, bar_value)
        
        # Draw the timer bar
        bar_width = 400  # Example width of the bar
        bar_height = 20  # Example height of the bar
        bar_x = (SCREEN_WIDTH - bar_width) // 2  # Center the bar
        bar_y = 10  # Position the bar at the top of the screen

        # Calculate the width of the bar based on the current value
        current_bar_width = (bar_value / 100) * bar_width

        # Draw the background of the bar (optional, for visual contrast)
        pygame.draw.rect(screen, BLACK, [bar_x, bar_y, bar_width, bar_height], 0)
        # Draw the current value of the bar
        pygame.draw.rect(screen, GREEN, [bar_x, bar_y, current_bar_width, bar_height], 0)


        player.draw()

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
