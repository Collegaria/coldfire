import pygame

class Player:
    def __init__(self, screen, color, radius, x, y, speed):
        self.screen = screen
        self.color = color
        self.radius = radius
        self.x = x
        self.y = y
        self.speed = speed

    def draw(self):
        side_length = self.size * 2  # Example conversion, adjust as needed
        square_rect = pygame.Rect(self.x - self.size, self.y - self.size, side_length, side_length)
        pygame.draw.rect(self.screen, self.color, square_rect)
        
    def pick_sticker(self):
        self.sticks_collected += 1  # Assuming sticks_collected is the counter for sticks
        global BAR_VALUE  # Assuming BAR_VALUE is accessible globally or passed to the Player
        BAR_VALUE += 3  # Increase the top bar by 3
        if BAR_VALUE > 100:  # Ensure the bar value does not exceed 100%
            BAR_VALUE = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy