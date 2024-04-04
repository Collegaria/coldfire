import pygame
import random
import sys
from modules.player import Player
from modules.world import *
from modules.events import *
from button import Button 

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
MAUVE = (224, 176, 255)
WHITE = (255, 255, 255)
# Update colors to use images
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BAR_VALUE = 60
CELL_SIZE = 60
MAP_SIZE = 50


# Load new images for player and obstacles
# Define the target size for your images
TARGET_SIZE = [CELL_SIZE, CELL_SIZE]
TREE_BORDER_SCALE_FACTOR = 4
LARGE_CELL_SIZE = int(CELL_SIZE * TREE_BORDER_SCALE_FACTOR)
# Load and scale images
player_image_left = pygame.transform.scale(pygame.image.load("assets/LincstepsL.png"), TARGET_SIZE)
player_image_right = pygame.transform.scale(pygame.image.load("assets/LincstepsR.png"), TARGET_SIZE)
frosBorder_image = pygame.transform.scale(pygame.image.load("assets/frosBorder.png"), (LARGE_CELL_SIZE, LARGE_CELL_SIZE))
frostree_image = pygame.transform.scale(pygame.image.load("assets/frostree.png"), (LARGE_CELL_SIZE, LARGE_CELL_SIZE))
Stick_image = pygame.transform.scale(pygame.image.load("assets/stick.png"), (LARGE_CELL_SIZE/2, LARGE_CELL_SIZE/2))
dragon_image = pygame.transform.scale(pygame.image.load("assets/Dragon.png"), TARGET_SIZE)

def play():
    global STICKS
    STICKS = 0
    pygame.init()
    center = MAP_SIZE // 2
    BAR_VALUE = 50  # Starting at 100%
    
    pygame.display.set_caption("coldFire")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    player = Player(screen, WHITE, 20, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 5, player_image_left)

    MAP = [[0 if x > 0 and x < MAP_SIZE-1 and y > 0 and y < MAP_SIZE-1 else 1 for x in range(MAP_SIZE)] for y in range(MAP_SIZE)]
    
    # House
    for y in range(center - 1, center + 1):
        for x in range(center - 1, center + 1):
            MAP[y][x] = 3  # Representing the house with a specific image (if needed)
    
    map_width = len(MAP[0]) * CELL_SIZE
    map_height = len(MAP) * CELL_SIZE

    offset_x = (SCREEN_WIDTH - map_width) // 2
    offset_y = (SCREEN_HEIGHT - map_height) // 2

    world = []
    World.spawn_trees_blocks(MAP, 80, 2)
    World.spawn_sticks(MAP, 60, 4)
    for y, row in enumerate(MAP):
        for x, cell in enumerate(row):
            if cell == 1:  # Wall
                world.append(Obstacle(screen, frosBorder_image, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)))
            elif cell == 2:  # Tree
                world.append(Obstacle(screen, frostree_image, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)))
            elif cell == 3:
                world.append(Obstacle(screen, dragon_image, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)))
            elif cell == 4:
                Stick_img = pygame.transform.rotate(Stick_image, random.randint(0, 360))
                
                world.append(Obstacle(screen, Stick_img, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)))

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
            player.current_image = player_image_left
        if keys[pygame.K_RIGHT]:
            dx += player.speed
            player.current_image = player_image_right
        if keys[pygame.K_UP]:
            dy -= player.speed
        if keys[pygame.K_DOWN]:
            dy += player.speed

        # Obstacles
        obstacles_to_remove = []
        for obstacle in world:
            obstacle.rect.x -= dx
            obstacle.rect.y -= dy
            # Apply offset to center the map
            centered_x = obstacle.rect.x + offset_x
            centered_y = obstacle.rect.y + offset_y
            # Draw the obstacle at the new, centered position
            obstacle.draw(centered_x, centered_y, CELL_SIZE)
            
        obstacles_to_remove = []
        for obstacle in world:
            if obstacle.image == Stick_image and player.rect.colliderect(obstacle.rect):
                world.remove(obstacle)  # Remove the stick from the game world
                STICKS += 1  # Increment the STICKS counter
        
        print(STICKS)

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

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()