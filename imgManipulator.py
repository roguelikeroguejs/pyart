import PIL
from PIL import Image, ImageOps
import argparse
import pygame
from pygame import display
import math
from math import pi


parser = argparse.ArgumentParser(description="Image flipper")
parser.add_argument('-i', '--image', help='Filename of input image', required=True)
parser.add_argument('-o', '--output', help="Output file", default='output.jpg', required=True)

passedIn = parser.parse_args()

display = pygame.display.init()


def rotatePoint(x1, y1, x2, y2, rotate):
    inRadians = math.radians(rotate)
    nx = math.cos(inRadians) * (x1 - x2) - math.sin(inRadians) * (y1 - y2) + x2
    ny = math.sin(inRadians) * (x1 - x2) + math.cos(inRadians) * (y1 - y2) + y2

    return int(nx), int(ny)


newImage = pygame.image.load(passedIn.image)
blankImage = newImage.copy()

# convert images to RGBA so parts can be invisible
newImage = newImage.convert_alpha()
blankImage = blankImage.convert_alpha()


imageWidth = newImage.get_width()
imageHeight = newImage.get_height()

scaler = 10
rotate = float(passedIn.rotate)

for i in range(60):
    scaled = pygame.transform.scale(newImage, [int(imageWidth - math.sqrt(scaler)),
                                               int(imageHeight - math.sqrt(imageHeight))])

    blankImage.blit(pygame.transform.rotate(scaled, math.sqrt(pi * rotate / 180)),
                    rotatePoint(scaler, scaler, imageWidth // 2, imageHeight // 2, math.sqrt(rotate)))
    scaler += 10
    rotate += rotate

    pygame.image.save(blankImage, passedIn.output)

    rotatedScaled = pygame.transform.rotate(scaled, math.sqrt(rotate))
    rotatedCorner = rotatePoint(scaler, scaler, imageWidth // 2, imageHeight // 2, math.sqrt(rotate))




