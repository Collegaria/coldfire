import pygame

class Obstacle:
    def __init__(self, screen, color, rect):
        self.screen = screen
        self.color = color
        self.rect = rect

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)