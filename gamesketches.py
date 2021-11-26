import pygame
import pygame.gfxdraw

pygame.init()

screenWidth = 800
screenHeight = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))
white = (255, 255, 255)

black = (0, 0, 0)

running = True

while running:
    screen.fill(black)

    for i in range(0, screenWidth):
        pygame.gfxdraw.pixel(screen, i, i, white)
        pygame.gfxdraw.pixel(screen, i, screenHeight - i, white)
        pygame.gfxdraw.pixel(screen, i, 199, white)
        pygame.gfxdraw.pixel(screen, i, 599, white)
        pygame.gfxdraw.pixel(screen, 199, i, white)
        pygame.gfxdraw.pixel(screen, 599, i, white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

