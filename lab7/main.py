import pygame
from math import *
from datetime import *

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
body = pygame.image.load("images/clock.png")
minute = pygame.image.load("images/right_hand.png")
seconds = pygame.image.load("images/left_hand.png")
bodyRect = body.get_rect(center=(500, 500))

running = True

while running:

    current = datetime.now()

    secondsAngle = current.second * 6
    minuteAngle = (current.minute * 6) + (current.second / 10)

    rotatedSecond = pygame.transform.rotate(seconds, -secondsAngle)
    rotatedMinute = pygame.transform.rotate(minute, -minuteAngle)

    rotatedRectMin = rotatedMinute.get_rect(center=bodyRect.center)
    rotatedRectSec = rotatedSecond.get_rect(center=bodyRect.center)

    screen.blit(body, bodyRect)
    screen.blit(rotatedSecond, rotatedRectSec)
    screen.blit(rotatedMinute, rotatedRectMin)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(60)
