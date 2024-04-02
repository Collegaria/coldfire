import pygame
import sys
from modules.player import Player
from modules.world import Obstacle

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def main():
    pygame.init()

    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Moving Circle")

    MAUVE = (224, 176, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(screen, WHITE, 20, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 5)


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

    CELL_SIZE = 20
    world = []
    for y, row in enumerate(MAP):
        for x, cell in enumerate(row):
            if cell == 1:  # Wall
                world.append(Obstacle(screen, BLACK, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)))
            elif cell == 2:  # Tree
                world.append(Obstacle(screen, GREEN, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)))

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


        player.x = SCREEN_WIDTH // 2
        player.y = SCREEN_HEIGHT // 2
        
        for obstacle in world:
            obstacle.rect.x -= dx
            obstacle.rect.y -= dy
            obstacle.draw()

        player.draw()

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
