import pygame, random, time, pygame_menu
from player import Player
from obstacle import *
from constants import *

VERSION = 0.81

pygame.init()

def start_game():
    # Static texts
    score = 0
    score_text = pygame.font.SysFont(None, 150).render("Score: " + str(score), True, black)
    score_text_rect = score_text.get_rect(center=(screen_width // 2, 50))

    level = 1
    level_text = pygame.font.SysFont(None, 100).render("Level: " + str(level), True, black)
    level_text_rect = level_text.get_rect(center=(screen_width // 2, 150))

    # Game Loop
    game_running= True
    camera_x = 0
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
                show_menu(score, level)

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
        ground_image = pygame.image.load("Pictures\ground.png").convert_alpha()
        ground_image = pygame.transform.scale(ground_image, (screen_width, 100))
        screen.blit(ground_image, (0, GROUND_HEIGHT))

        # Increase score and level
        if player.rect.left > obstacle_x_positions[score]:
            score += 1
            score_text = pygame.font.SysFont(None, 150).render("Score: " + str(score), True, black)

            if score >= 30 and score < 60:
                player.set_speed(15)
                player.set_jump_height(15)
                level = 2
            elif score >= 60 and score < 90:
                player.set_speed(14)
                player.set_jump_height(14)
                level = 3
            elif score >= 90 and score < 100:
                player.set_speed(13)
                player.set_jump_height(13)
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
            time.sleep(1)
            new_game(score, level)

        # Victory
        if score >= NUM_OBSTACLES:
            victory_text = pygame.font.SysFont(None, 300).render("Victory!", True, green)
            victory_text_rect = victory_text.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(victory_text, victory_text_rect)
            pygame.display.update()
            time.sleep(5)
            new_game(score, level)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def new_game(score, level):
    global game_running
    game_running = True
    player.rect.center = (PLAYER_START_X, GROUND_HEIGHT)
    obstacle_x_positions = []
    obstacle_group.empty()
    player.set_speed(16)
    player.set_jump_height(16)

    for i in range(NUM_OBSTACLES):
        if i == 0:
            x = OBSTACLE_START_X
        else:
            x = obstacle_x_positions[i - 1] + random.randint(MIN_DISTANCE, MAX_DISTANCE)

        obstacle_x_positions.append(x)
        obstacle_group.add(Obstacle(x, GROUND_HEIGHT))

    pygame.init()
    show_menu(score, level)

def show_menu(score, level):
    menu = pygame_menu.Menu('Hauptmenü', 1300, 800)
    menu.add.button('Spiel starten', start_game, font_color=green, font_size=100)
    menu.add.button('Beenden', pygame_menu.events.EXIT, font_color=red, font_size=100)

    menu.add.label("Score: " + str(score) + "   Level: " + str(level), font_color=white, font_size=50)

    menu.add.label("Version: " + str(VERSION), font_color=black, font_size=25, align=pygame_menu.locals.ALIGN_LEFT)
    menu.add.label("Credits: Clarala für die krassen Zeichnungen", font_color=black, font_size=25, align=pygame_menu.locals.ALIGN_RIGHT)

    menu.mainloop(screen)

# Start Menu
player = Player()
obstacle_group = create_obstacles()
clock = pygame.time.Clock()
score = 0
level = 1
show_menu(score, level)
