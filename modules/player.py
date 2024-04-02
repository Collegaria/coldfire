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
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
        
    def pick_sticker(self, stick):
        return 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy