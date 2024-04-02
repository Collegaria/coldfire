import pygame

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def update_timer_bar(last_update_time, current_time, bar_value):
    if current_time - last_update_time >= 2000:  # 2000 milliseconds = 2 seconds
        bar_value = max(0, bar_value - 2)  # Decrease by 1%, ensuring it doesn't go below 0
        last_update_time = current_time
    return last_update_time, bar_value  # Return False to indicate no update was needed