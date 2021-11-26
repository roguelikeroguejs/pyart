import pygame
import pygame.gfxdraw
import math

pygame.init()

screenWidth = 800
screenHeight = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))

clock = pygame.time.Clock()

white = (255, 255, 255)
grey = (125, 125, 125)
black = (0, 0, 0)


running = True


def draw_flat_line(screen, x, y, length, color):
    for i in range(length):
        pygame.gfxdraw.pixel(screen, x + i, y, color)


def draw_vertical_line(screen, x, y, length, color):
    for i in range(length):
        pygame.gfxdraw.pixel(screen, x, y + i, color)


def draw_plus_sign(screen, x, y, size, color):
    draw_flat_line(screen, x - (size // 2), y, size, color)
    draw_vertical_line(screen, x, y - (size // 2), size, color)


# set the start points to the center of the screen
plusX = screenWidth // 2
plusY = screenHeight // 2
centerPoint = (screenWidth // 2, screenHeight // 2)

cursorList = []

while running:
    screen.fill(black)

    # every loop, draw the plus sign again at the new position, update the cursor's color
    draw_plus_sign(screen, plusX, plusY, 15, white)

    # loop over every cursor position, if empty, skips
    for i, plusSign in enumerate(cursorList):

        rR = math.sin(i * .01) * 127 + 128
        rG = math.sin(i * .01 + 5) * 127 + 128
        rB = math.sin(i * .01 + 10) * 127 + 128

        # Generate a fader for all colors to be scaled by
        # Want the sin wave to range from 0 to 1, not -1 to 1
        # So we add 1 to our result and then divide by 2
        fader = (math.sin(i * .02) + 1) / 2
        rR = rR * fader
        rB = rB * fader
        rG = rG * fader



        # Change the value below from .005 to 5.2, default .043
        sizer = int(math.sin(i * .043) * 35 + 35)

        draw_plus_sign(screen, plusSign[0], plusSign[1], sizer, (rR, rG, rB))

        # Copy the top left quarter of screen
        cropped = pygame.Surface((screenWidth // 2, screenHeight // 2))
        cropped.blit(screen, (0, 0), pygame.Rect(0, 0, screenWidth // 2, screenHeight // 2))

        # flip that copy on just the y axis, paste below
        belowFlipped = pygame.transform.flip(cropped, False, True)
        screen.blit(belowFlipped, pygame.Rect(0, screenHeight // 2, screenWidth // 2, screenHeight))

        # flip the original copy on just the x-axis, paste to the right
        topRight = pygame.transform.flip(cropped, True, False)
        screen.blit(topRight, pygame.Rect(screenWidth // 2, 0, screenWidth, screenHeight // 2))

        # flip both axis, paste from bottom right
        bottomRight = pygame.transform.flip(cropped, True, True)
        screen.blit(bottomRight, pygame.Rect(screenWidth // 2, screenHeight // 2, screenWidth, screenHeight))

    # get the list of keys that are pressed/not pressed
    key = pygame.key.get_pressed()

    # add check for the space bar and add a new coordinate to have a plus sign, and the selected color
    if key[pygame.K_SPACE]:
        newPlace = [plusX, plusY, white]
        cursorList.append(newPlace)

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






