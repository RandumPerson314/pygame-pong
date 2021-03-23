import sys, pygame
from win32api import GetSystemMetrics # pylint: disable=no-name-in-module

# Game intitializations
pygame.init() # pylint: disable=no-member

screen_size = screen_width, screen_height = GetSystemMetrics(0), GetSystemMetrics(1)

screen = pygame.display.set_mode(screen_size)

#* Variables

background_colour = (50, 50, 100)

# Ball varibables
ball_radius = screen_width/96
ball_x, ball_y = (screen_width - ball_radius * 4), (screen_height - ball_radius)/2
ball_x_speed, ball_y_speed = 0 - screen_width/2560, 0 - screen_width/2560

# Paddle variables
paddle_height = screen_height/6
paddle_width = screen_width/48

# Paddle1
paddle1_x = screen_width/38.4 
paddle1_y = screen_height / 2 - (paddle_height / 2)

# Paddle2
paddle2_x = screen_width - paddle1_x - paddle_width
paddle2_y = screen_height / 2 - (paddle_height / 2)

# Middle line variables
middle_line_width = paddle_width / 2
middle_line_x = screen_width / 2 - (middle_line_width / 2)

# Score variables 
user1_points = 0
user2_points = 0
font = pygame.font.Font("freesansbold.ttf", 32)
point1_x = screen_width / 192
point_y = screen_height / 108
point2_x = 0
# Display Variables
pygame.display.set_caption("Pong")
icon = pygame.image.load("ping-pong-bat.png")
pygame.display.set_icon(icon)

#* Game

while 1:
    screen.fill(background_colour)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() # pylint: disable=no-member

    # Draw ball and paddles
    ball = pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), ball_radius)
    paddle1 = pygame.draw.rect(screen, (255, 255, 255), (paddle1_x, paddle1_y, paddle_width, paddle_height))
    paddle2 = pygame.draw.rect(screen, (255, 255, 255), (paddle2_x, paddle2_y, paddle_width, paddle_height))

    # Draw middle line
    middle_line = pygame.draw.rect(screen, (255, 255, 255), (middle_line_x, 0, middle_line_width, screen_height))
    # Draw scores
    score1 = font.render("Score : " + str(user1_points), True, (255, 255, 255))
    score2 = font.render("Score : " + str(user2_points), True, (255, 255, 255))
    score_width = score1.get_width()
    screen.blit(score1, (point1_x, point_y))
    screen.blit(score2, (screen_width - score_width - 10, point_y)) #!find out what blit width is
    
    # Hits paddle1
    if paddle1_x - 1 < (ball_x - ball_radius) < paddle1_x + paddle_width:
        if paddle1_y <= ball_y <= (paddle1_y + paddle_height):
            if ball_y < paddle1_y + (paddle_height / 2):
                ball_y_speed = -(abs(ball_y_speed))
            elif ball_y > paddle1_y + (paddle_height / 2): 
                ball_y_speed = abs(ball_y_speed)
            ball_x_speed = -ball_x_speed

    # Ball bounces on top and bottom of screen
    if ball_y >= screen_height or ball_y <= 0:
        ball_y_speed = -ball_y_speed

    # Move ball
    ball_x += ball_x_speed
    ball_y += ball_y_speed
    
    # Move paddle1 with W and S
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w] and paddle1_y >= 0:
       paddle1_y -= 1
    if pressed[pygame.K_s] and paddle1_y < screen_height - paddle_height:
       paddle1_y += 1

    # Move paddle2 with UP and DOWN arrows
    if pressed[pygame.K_UP] and paddle2_y >= 0:
       paddle2_y -= 1
    if pressed[pygame.K_DOWN] and paddle2_y < screen_height - paddle_height:
       paddle2_y += 1
    
    pygame.display.flip()