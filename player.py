import pygame
from constants import *

# Version 1.0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Pictures/player.png").convert_alpha()
        self.rect = self.image.get_rect(center=(PLAYER_START_X, GROUND_HEIGHT))
        self.velocity = 0
        self.speed = PLAYER_SPEED
        self.jump_height = JUMP_HEIGHT

    def move(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity
        if self.rect.bottom >= GROUND_HEIGHT:
            self.rect.bottom = GROUND_HEIGHT
            self.velocity = 0

        left_border = pygame.Rect(-50, 0, 10, screen_height)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.rect.left > left_border.right:
                self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE]:
            self.jump()

    def jump(self):
        if self.rect.bottom == GROUND_HEIGHT:
            self.velocity -= self.jump_height

    def set_speed(self, speed):
        self.speed = speed

    def set_jump_height(self, jump_height):
        self.jump_height = jump_height
