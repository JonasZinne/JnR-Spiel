import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert_alpha()
        self.rect = self.image.get_rect(center=(PLAYER_START_X, GROUND_HEIGHT))
        self.velocity = 0

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
                self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_SPACE]:
            self.jump()

    def jump(self):
        if self.rect.bottom == GROUND_HEIGHT:
            self.velocity -= JUMP_HEIGHT