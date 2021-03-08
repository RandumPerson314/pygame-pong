import sys, pygame
from win32api import GetSystemMetrics # pylint: disable=no-name-in-module

# Game intitializations
pygame.init() # pylint: disable=no-member

screen_size = screen_width, screen_height = GetSystemMetrics(0), GetSystemMetrics(1)

screen = pygame.display.set_mode(screen_size)

black = (0, 0, 0)

# Things in game
ball_radius = 20
ball_x, ball_y = (screen_width - ball_radius)/2, (screen_height - ball_radius)/2
ball_x_speed, ball_y_speed = 0.5, 0.5

while 1:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() # pylint: disable=no-member

    ball = pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), ball_radius)

    if ball_x >= screen_width or ball_x <= 0:
        ball_x_speed = -ball_x_speed

    if ball_y >= screen_height or ball_y <= 0:
        ball_y_speed = -ball_y_speed

    ball_x += ball_x_speed
    ball_y += ball_y_speed

    pygame.display.flip()