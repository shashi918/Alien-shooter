import pygame
import os

# Initialize Pygame
pygame.init()

# Set up the display window (optional)
screen = pygame.display.set_mode((1920, 1080))

# Set the directory containing your image files

# Specify the filename of the PNG image
filename = "rain.png"

# Construct the full path to the image file

# Load the image
image = pygame.image.load("rain.png")

# Blit the image onto the screen (optional)
screen.blit(image, (0, 0))

# Update the display (optional)
pygame.display.update()

# Main loop (optional, if you want to keep the window open)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()