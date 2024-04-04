import pygame

class Player:
    def __init__(self, screen, color, size, x, y, speed, image):
        self.screen = screen
        self.color = color  # This might be unused if you're switching to image rendering
        self.size = size
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image  # New attribute for the player's image

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
        
    def pick_sticker(self):
        self.sticks_collected += 1  # Assuming sticks_collected is the counter for sticks
        global BAR_VALUE  # Assuming BAR_VALUE is accessible globally or passed to the Player
        BAR_VALUE += 3  # Increase the top bar by 3
        if BAR_VALUE > 100:  # Ensure the bar value does not exceed 100%
            BAR_VALUE = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy