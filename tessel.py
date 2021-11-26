
import math
from math import cos, sin, radians, fabs
import pygame
import pygame.gfxdraw

pygame.init()

screenWidth = 800
screenHeight = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))

running = True

red = (255, 0, 0)
white = (255, 255, 255)
grey = (125, 125, 125)
black = (0, 0, 0)


def rotate_points(toTurn, pivot, degrees):
    translate = [toTurn[0] - pivot[0], toTurn[1] - pivot[1]]
    rads = math.radians(degrees)
    ourCos = cos(rads)
    ourSin = sin(rads)

    x = translate[0] * ourCos - translate[1] * ourSin
    y = translate[0] * ourSin + translate[1] * ourCos

    return [x + pivot[0], y + pivot[1]]


def create_centered_triangle(center, radius):
    C1 = [center[0], center[1] - radius]

    r120 = {'cos': cos(radians(120)), 'sin': sin(radians(120))}

    r240 = {'cos': cos(radians(240)), 'sin': sin(radians(240))}

    rX = [C1[0] - center[0], C1[1] - center[1]]
    rL, rR = [0, 0], [0, 0]
    rL[0] = rX[0] * r120['cos'] - rX[1] * r120['sin']
    rL[1] = rX[0] * r120['sin'] - rX[1] * r120['cos']
    rR[0] = rX[0] * r240['cos'] - rX[1] * r240['sin']
    rR[1] = rX[0] * r240['sin'] - rX[1] * r240['cos']

    left = [rL[0] + center[0], rL[1] + center[1]]
    right = [rR[0] + center[0], rR[1] + center[1]]
    return [left, right, C1]


def translate_points(points, x, y):
    newArray = []
    for point in points:
        newArray.append([point[0] + x, point[1] + y])
    return newArray
 pygame.draw.create_centered_triangle([0, 0], 10)

triangy = create_centered_triangle((screenWidth // 2, screenHeight // 2), T_SIZE, 0)
theDistance = fabs(triangy[0][0] - triangy[1][0])


while running:
    screen.fill(black)
    pygame.draw.polygon(screen, red, translate_points() )


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.display.flip()




