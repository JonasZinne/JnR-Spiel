import pygame
import random
from constants import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("obstacle.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y - 100))

obstacle_x_positions = []

def create_obstacles():
    obstacle_group = pygame.sprite.Group()

    for i in range(NUM_OBSTACLES):
        if i == 0:
            x = OBSTACLE_START_X
        else:
            x = obstacle_x_positions[i - 1] + random.randint(MIN_DISTANCE, MAX_DISTANCE)

        obstacle_x_positions.append(x)
        obstacle_group.add(Obstacle(x, GROUND_HEIGHT))

    return obstacle_group