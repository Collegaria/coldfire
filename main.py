import pygame
import sys

class Circle:
    def __init__(self, screen, color, radius, x, y, speed):
        self.screen = screen
        self.color = color
        self.radius = radius
        self.x = x
        self.y = y
        self.speed = speed

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class BackgroundElement:
    def __init__(self, screen, color, rect):
        self.screen = screen
        self.color = color
        self.rect = rect

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class Obstacle:
    def __init__(self, screen, color, rect):
        self.screen = screen
        self.color = color
        self.rect = rect

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def main():
    pygame.init()

    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 400
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Moving Circle")

    MAUVE = (224, 176, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)

    circle_radius = 20
    circle_x = SCREEN_WIDTH // 2
    circle_y = SCREEN_HEIGHT // 2
    circle_speed = 5
    circle = Circle(screen, WHITE, circle_radius, circle_x, circle_y, circle_speed)

    MAP = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    CELL_SIZE = 40
    obstacles = []
    for y, row in enumerate(MAP):
        for x, cell in enumerate(row):
            if cell == 1:  # Wall
                obstacles.append(Obstacle(screen, BLACK, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)))
            elif cell == 2:  # Tree
                obstacles.append(Obstacle(screen, GREEN, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)))

    running = True
    while running:
        screen.fill(MAUVE)
        running = handle_events()

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx -= circle.speed
        if keys[pygame.K_RIGHT]:
            dx += circle.speed
        if keys[pygame.K_UP]:
            dy -= circle.speed
        if keys[pygame.K_DOWN]:
            dy += circle.speed

        circle.move(dx, dy)

        # circle.x = SCREEN_WIDTH // 2
        # circle.y = SCREEN_HEIGHT // 2
        
        for obstacle in obstacles:
            obstacle.draw()

        circle.draw()

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()