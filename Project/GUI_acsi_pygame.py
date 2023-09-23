import pygame
from pygame.locals import *
from pygame import mixer
import sys
import threading
import _thread
import datetime
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)

# Create the main Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('DiabePie')

# Load images and sounds
background_image = pygame.image.load('background.png')
cheri_image = pygame.image.load('CherriElOtorongo.png')
processing_image = pygame.image.load('processing.png')
loading_images = [pygame.image.load(f'cargando_{i}.png') for i in range(1, 12)]

# Initialize mixer for sound effects
mixer.init()

# Global variables
lang = "English"
current_image = None

def display_text(text, position, color=BLACK):
    text_surface = FONT.render(text, True, color)
    screen.blit(text_surface, position)

def display_image(image, position):
    screen.blit(image, position)

def select_language():
    global lang
    # Your language selection code here

def open_image():
    global current_image
    # Your image opening code here
    current_image = pygame.image.load('your_selected_image.png')

def process_image():
    # Your image processing code here
    pass

def save_image():
    # Your image saving code here
    pass

def main_menu():
    global current_image
    screen.blit(background_image, (0, 0))
    display_image(cheri_image, (WIDTH - 269, HEIGHT - 269))
    display_text('DiabePie', (200, 200), RED)
    display_text('Start program', (200, 400), RED)
    display_text('Select language', (200, 480), RED)
    display_text('Credits', (200, 560), RED)
    pygame.display.flip()
    current_image = None

def processing_menu():
    screen.blit(processing_image, (0, 0))
    display_text('Processing...', (200, 200), RED)
    pygame.display.flip()

def loading_menu():
    screen.blit(background_image, (0, 0))
    display_text('Loading...', (200, 200), RED)
    pygame.display.flip()
    for i in range(11):
        screen.blit(loading_images[i], (300, 300))
        pygame.display.flip()
        pygame.time.delay(100)

def results_menu():
    screen.blit(background_image, (0, 0))
    display_text('Results', (200, 200), RED)
    display_image(current_image, (400, 300))
    display_text('End', (200, 700), RED)
    display_text('Save image', (600, 700), RED)
    pygame.display.flip()

current_menu = main_menu

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if current_menu == main_menu:
                if 200 <= x <= 600 and 400 <= y <= 440:
                    current_menu = processing_menu
                    process_image()
                    loading_menu()
                    current_menu = results_menu
                elif 200 <= x <= 600 and 480 <= y <= 520:
                    select_language()
                elif 200 <= x <= 600 and 560 <= y <= 600:
                    # Display credits
                    pass
            elif current_menu == results_menu:
                if 200 <= x <= 400 and 700 <= y <= 740:
                    current_menu = main_menu
                elif 600 <= x <= 800 and 700 <= y <= 740:
                    save_image()
    current_menu()
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
