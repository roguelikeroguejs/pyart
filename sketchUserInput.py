import pygame
import pygame.gfxdraw
import random

pygame.init()

screenWidth = 800
screenHeight = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))

clock = pygame.time.Clock()

hue = 0
white = (255, 255, 255)
grey = (125, 125, 125)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
colorList = [white, black, blue, red, green]

running = True


# change the color by incrementing the index of the colorlist
def color_change():
    global hue
    if hue < 4:
        hue = hue + 1
    else:
        hue = 0


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
    draw_flat_line(screen, x - (size // 2), y, size, color)
    draw_vertical_line(screen, x, y - (size // 2), size, color)


# set the start points to the center of the screen
plusX = screenWidth // 2
plusY = screenHeight // 2

cursorList = []

while running:
    screen.fill(grey)

    # every loop, draw the plus sign again at the new position, update the cursor's color
    draw_plus_sign(screen, plusX, plusY, 15, colorList[hue])
    # loop over every cursor position, if empty, skips
    for plusSign in cursorList:
        draw_plus_sign(screen, plusSign[0], plusSign[1], 10, plusSign[2])

    #for i, plusSign in enumerate(cursorList):
    #    draw_plus_sign(screen, plusSign[0], plusSign[1], 10, (i % 255, i% 255, i % 255))

    # get the list of keys that are pressed/not pressed
    key = pygame.key.get_pressed()

    # add check for the space bar and add a new coordinate to have a plus sign, and the selected color
    if key[pygame.K_SPACE]:
        newPlace = [plusX, plusY, colorList[hue]]
        cursorList.append(newPlace)
    #  change the cursor's color by calling color change and redrawing the plus sign
    if key[pygame.K_LSHIFT]:
        color_change()
        draw_plus_sign(screen, plusX, plusY, 10, colorList[hue])

    if key[pygame.K_UP]:
        plusY = plusY - 1
    elif key[pygame.K_DOWN]:
        plusY = plusY + 1
    if key[pygame.K_LEFT]:
        plusX = plusX - 1
    elif key[pygame.K_RIGHT]:
        plusX = plusX + 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(90)
