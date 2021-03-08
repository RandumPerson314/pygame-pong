import sys, pygame
pygame.init() # pylint: disable=no-member
from win32api import GetSystemMetrics # pylint: disable=no-name-in-module

print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))


size = width, height = 1920, 1080

screen = pygame.display.set_mode(size)

while 1: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() # pylint: disable=no-member

    pygame.display.flip()