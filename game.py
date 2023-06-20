import pygame, random, time
from player import Player
from obstacle import *
from constants import *

VERSION = 0.7

pygame.init()

# Static texts
start_text = pygame.font.SysFont(None, 100).render("Klicke, um das Spiel zu starten", True, black)
start_text_rect = start_text.get_rect(center=(screen_width // 2, screen_height // 2))

version_text = pygame.font.SysFont(None, 25).render("Version: " + str(VERSION), True, black)
version_text_rect = version_text.get_rect(topright=(screen_width - 10, 10))

score = 0
score_text = pygame.font.SysFont(None, 150).render("Score: " + str(score), True, black)
score_text_rect = score_text.get_rect(center=(screen_width // 2, 50))

level = 1
level_text = pygame.font.SysFont(None, 100).render("Level: " + str(level), True, black)
level_text_rect = level_text.get_rect(center=(screen_width // 2, 150))

# Game Loop
game_running, game_started = True, False
camera_x = 0
player = Player()
obstacle_group = create_obstacles()
clock = pygame.time.Clock()

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_started:
            game_started = True

    if not game_started:
        screen.fill((173, 216, 230))
        screen.blit(start_text, start_text_rect)
        screen.blit(version_text, version_text_rect)
        pygame.display.update()
        continue

    # Game-Update
    screen.fill((173, 216, 230)) # Background
    player.move()

    # Contact with obstacle
    if pygame.sprite.spritecollide(player, obstacle_group, False):
        game_running = False

    # Camera-Update
    if player.rect.right > screen_width // 2:
        camera_x = -(player.rect.right - (screen_width // 2))
    elif player.rect.left < PLAYER_START_X:
        camera_x = PLAYER_START_X - player.rect.left
    else:
        camera_x = 0

    for obstacle in obstacle_group:
        screen.blit(obstacle.image, obstacle.rect.move(camera_x, 0))
    screen.blit(player.image, player.rect.move(camera_x, 0))

    # Ground
    ground_image = pygame.image.load("ground.png").convert_alpha()
    ground_image = pygame.transform.scale(ground_image, (screen_width, 100))
    screen.blit(ground_image, (0, GROUND_HEIGHT))

    # Increase score and level
    if player.rect.left > obstacle_x_positions[score]:
        score += 1
        score_text = pygame.font.SysFont(None, 150).render("Score: " + str(score), True, black)
        
        if score >= 30 and score < 60:
            PLAYER_SPEED = 15
            JUMP_HEIGHT = 15
            level = 2    
        elif score >= 60 and score < 90:
            PLAYER_SPEED = 14
            JUMP_HEIGHT = 14
            level = 3
        elif score >= 90 and score < 100:
            PLAYER_SPEED = 13
            JUMP_HEIGHT = 13
            level = 4 
        level_text = pygame.font.SysFont(None, 100).render("Level: " + str(level), True, black)

    screen.blit(score_text, score_text_rect)
    screen.blit(level_text, level_text_rect)

    # Game Over
    if not game_running:
        game_over_text = pygame.font.SysFont(None, 300).render("Game Over", True, red)
        game_over_text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(game_over_text, game_over_text_rect)
        pygame.display.update()
        time.sleep(2)

        # Start new game
        game_running, game_started = True, False
        player.rect.center = (PLAYER_START_X, GROUND_HEIGHT)
        obstacle_x_positions = []
        obstacle_group.empty()
        score = 0
        level = 1
        PLAYER_SPEED = 16
        JUMP_HEIGHT = 16

        if event.type == pygame.QUIT:  # Close window
            game_running = False

        for i in range(NUM_OBSTACLES):
            if i == 0:
                x = OBSTACLE_START_X
            else:
                x = obstacle_x_positions[i - 1] + random.randint(MIN_DISTANCE, MAX_DISTANCE)

            obstacle_x_positions.append(x)
            obstacle_group.add(Obstacle(x, GROUND_HEIGHT))

    # Victory
    if score >= NUM_OBSTACLES:
        victory_text = pygame.font.SysFont(None, 300).render("Victory!", True, green)
        victory_text_rect = victory_text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(victory_text, victory_text_rect)
        pygame.display.update()
        time.sleep(5)

        # Start new game
        game_running, game_started = True, False
        player.rect.center = (PLAYER_START_X, GROUND_HEIGHT)
        obstacle_x_positions = []
        obstacle_group.empty()
        score = 0
        level = 1
        PLAYER_SPEED = 16
        JUMP_HEIGHT = 16

        if event.type == pygame.QUIT:  # Close window
            game_running = False

        for i in range(NUM_OBSTACLES):
            if i == 0:
                x = OBSTACLE_START_X
            else:
                x = obstacle_x_positions[i - 1] + random.randint(MIN_DISTANCE, MAX_DISTANCE)

            obstacle_x_positions.append(x)
            obstacle_group.add(Obstacle(x, GROUND_HEIGHT))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
