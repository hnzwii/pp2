import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
posX = 640
posY = 360
move = 20

running = True

while running:

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, 'Red', (posX, posY), 25)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and posX > 25:
        posX -= move
    elif keys[pygame.K_RIGHT] and posX < 1255:
        posX += move
    elif keys[pygame.K_UP] and posY > 25:
        posY -= move
    elif keys[pygame.K_DOWN] and posY < 695:
        posY += move

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(20)
