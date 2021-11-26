import pygame
import pygame.gfxdraw
import random

pygame.init()

screenWidth = 800
screenHeight = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

running = True


def draw_flat_line(screen, x, y, length, color):
    for i in range(length):
        pygame.gfxdraw.pixel(screen, x + i, y, color)


def draw_vertical_line(screen, x, y, length, color):
    for i in range(length):
        pygame.gfxdraw.pixel(screen, x, y + i, color)


def draw_cross_line(screen, x, y, length, color):
    for i in range(length):
        pygame.gfxdraw.pixel(screen, x + i, y, color)
        pygame.gfxdraw.pixel(screen, x, y + i, color)


def draw_empty_boxes(screen, left, top, width, height, color):
    rect = (left, top, width, height)
    for i in range(screenWidth):
        pygame.gfxdraw.rectangle(screen, rect, color)


def draw_boxes(screen, left, top, width, height, color):
    rect = (left, top, width, height)
    for i in range(screenHeight):
        pygame.gfxdraw.box(screen, rect, color)


def draw_plus_sign(screen, x, y, size, color):
    draw_flat_line(x - (size // 2), y, size, color)
    draw_vertical_line(x, y - (size // 2), size, color)



while running:
    screen.fill(black)

    for i in range(100):
        thisX = random.randrange(0, screenWidth)
        thisY = random.randrange(0, screenHeight)
        thisX2 = random.randrange(0, screenWidth * .8)
        thisY2 = random.randrange(0, screenHeight * .8)
        thisLength = random.randrange(0, 100)
        thisWidth = random.randrange(0, 50)
        thisHeight = random.randrange(0, 50)
        thisWidth2 = random.randrange(0, 80)
        thisHeight2 = random.randrange(0, 80)
        #draw_flat_line(screen, thisX, thisY, thisLength, white)
        #draw_vertical_line(screen, thisX, thisY, thisLength, white)
        #draw_cross_line(screen, thisX, thisY, thisLength, white)
        #draw_empty_boxes(screen, thisX, thisY, thisWidth, thisHeight, red)
        #draw_boxes(screen, thisX2, thisY2, thisWidth2, thisHeight2, white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
