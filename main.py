import pygame
import random
import sys
from modules.player import Player
from modules.world import Obstacle
from modules.events import *
from button import Button 

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("C:/Users/Dell/Downloads/Menu-System-PyGame-main/Menu-System-PyGame-main/assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("C:/Users/Dell/Downloads/Menu-System-PyGame-main/Menu-System-PyGame-main/assets/font.ttf", size)


SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
MAUVE = (224, 176, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BAR_VALUE = 50  # Starting at 100%
CELL_SIZE = 20
MAP_SIZE = 100

def play():
    pygame.init()
    center = MAP_SIZE // 2
    
    pygame.display.set_caption("coldFire")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    player = Player(screen, WHITE, 20, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 5)

    MAP = [[0 if x > 0 and x < MAP_SIZE-1 and y > 0 and y < MAP_SIZE-1 else 1 for x in range(MAP_SIZE)] for y in range(MAP_SIZE)]
    
    # House
    for y in range(center - 2, center + 2):
        for x in range(center - 2, center + 2):
            MAP[y][x] = 3  # Representing the blue block
    
    
    map_width = len(MAP[0]) * CELL_SIZE
    map_height = len(MAP) * CELL_SIZE

    offset_x = (SCREEN_WIDTH - map_width) // 2
    offset_y = (SCREEN_HEIGHT - map_height) // 2


    world = []
    Obstacle.spawn_trees_blocks(MAP, 80, 2)
    Obstacle.spawn_sticks(MAP, 20, 4)
    for y, row in enumerate(MAP):
        for x, cell in enumerate(row):
            if cell == 1:  # Wall
                world.append(Obstacle(screen, BLACK, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)))
            elif cell == 2:  # Tree
                world.append(Obstacle(screen, GREEN, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)))
            elif cell == 3:
                world.append(Obstacle(screen, BLUE, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)))
            elif cell == 4:
                world.append(Obstacle(screen, BROWN, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)))

    # Timer Bar Variables
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

        # Obstacles
        for obstacle in world:
            obstacle.rect.x -= dx
            obstacle.rect.y -= dy
            # Apply offset to center the map
            centered_x = obstacle.rect.x + offset_x
            centered_y = obstacle.rect.y + offset_y
            # Draw the obstacle at the new, centered position
            obstacle.draw(centered_x, centered_y, CELL_SIZE)

        # Timer Bar
        current_time = pygame.time.get_ticks()
        last_update_time, BAR_VALUE = update_timer_bar(last_update_time, current_time, BAR_VALUE)
        
        # Draw the timer bar
        bar_width = 400  # Example width of the bar
        bar_height = 20  # Example height of the bar
        bar_x = (SCREEN_WIDTH - bar_width) // 2  # Center the bar
        bar_y = 10  # Position the bar at the top of the screen

        # Calculate the width of the bar based on the current value
        current_bar_width = (BAR_VALUE / 100) * bar_width

        # Draw the background of the bar (optional, for visual contrast)
        pygame.draw.rect(screen, BLACK, [bar_x, bar_y, bar_width, bar_height], 0)
        # Draw the current value of the bar
        pygame.draw.rect(screen, GREEN, [bar_x, bar_y, current_bar_width, bar_height], 0)

        player.draw()

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("C:/Users/Dell/Downloads/Menu-System-PyGame-main/Menu-System-PyGame-main/assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("C:/Users/Dell/Downloads/Menu-System-PyGame-main/Menu-System-PyGame-main/assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("C:/Users/Dell/Downloads/Menu-System-PyGame-main/Menu-System-PyGame-main/assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()