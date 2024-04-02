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


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def main():
    # Initialize Pygame
    pygame.init()

    # Set up screen
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 400
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Moving Circle")

    # Colors
    MAUVE = (224, 176, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Create circle
    circle_radius = 20
    circle_x = SCREEN_WIDTH // 2
    circle_y = SCREEN_HEIGHT // 2
    circle_speed = 5
    circle = Circle(screen, WHITE, circle_radius, circle_x, circle_y, circle_speed)

    # Create background elements
    background_elements = [
        BackgroundElement(screen, BLACK, pygame.Rect(100, 100, 50, 50)),
        BackgroundElement(screen, BLACK, pygame.Rect(300, 200, 70, 70)),
        BackgroundElement(screen, BLACK, pygame.Rect(500, 50, 40, 40))
    ]

    # Main game loop
    running = True
    while running:
        screen.fill(MAUVE)

        # Handle events
        running = handle_events()
        if not running:
            break

        # Get the state of all keyboard keys
        keys = pygame.key.get_pressed()

        # Move the circle based on arrow key presses
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx -= circle.speed
        if keys[pygame.K_RIGHT]:
            dx += circle.speed
        if keys[pygame.K_UP]:
            dy -= circle.speed
        if keys[pygame.K_DOWN]:
            dy += circle.speed

        # Move the circle
        circle.move(dx, dy)

        # Move the background elements with the circle/player
        for element in background_elements:
            element.rect.move_ip(-dx, -dy)

        # Adjust circle position to keep it centered
        circle.x = SCREEN_WIDTH // 2
        circle.y = SCREEN_HEIGHT // 2

        # Draw the background elements
        for element in background_elements:
            element.draw()

        # Draw the circle
        circle.draw()

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(60)

    # Quit Pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
