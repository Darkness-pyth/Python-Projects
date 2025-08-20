import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AC inductor Sine Wave")

# Colors
BACKGROUND = (0, 0, 0)
WAVE_COLOR_ONE = (51, 255, 51)
WAVE_COLOR_TWO = (255,0,0)

# Wave parameters
amplitude = 100
frequency = 0.01
speed = 0.1
phase_one = 0
phase_two = math.pi / 2

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    
    # Fill the screen  with Background Color
    screen.fill(BACKGROUND)
    
    # Update phase for animation
    phase_one += speed
    phase_two += speed
    
    # Draw sine wave
    points_one = []
    points_two = []

    for x in range(WIDTH):
        # Calculate y position using sine function
        y = HEIGHT // 2.3 + amplitude * math.sin(frequency * x + phase_one)
        b = HEIGHT // 2 + amplitude * math.sin(frequency * x + phase_two)
        points_one.append((x, y))
        points_two.append((x,b))
        
    
    # Draw the wave
    if len(points_one) > 1:
        pygame.draw.lines(screen, WAVE_COLOR_ONE, False, points_one, 5)
        pygame.draw.lines(screen, WAVE_COLOR_TWO, False, points_two, 5)
    
    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()