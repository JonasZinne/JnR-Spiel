import pygame

pygame.init()

# Window settings
screen_width, screen_height = 1300, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jump and Run Game - Made by Jonas")

# constants
GROUND_HEIGHT = 700

PLAYER_SPEED = 16 # Level 1
JUMP_HEIGHT = 16 # Level 1
GRAVITY = 0.7
PLAYER_START_X = 100

NUM_OBSTACLES = 101
MIN_DISTANCE = 150
MAX_DISTANCE = 500
OBSTACLE_START_X = 800

# colours
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
