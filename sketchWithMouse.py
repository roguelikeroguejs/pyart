import pygame
import pygame.gfxdraw
import random


pygame.init()

screenWidth = 800
screenHeight = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))

clock = pygame.time.Clock()

white = (255, 255, 255)
grey = (125, 125, 125)
black = (0, 0, 0)

# Generate a color palette
colorPalette = [(235, 236, 58), (58, 67, 245), (236, 58, 245), (67, 245, 58), (235, 84, 33), (27, 219, 219)]




running = True


class Line():
    def __init__(self):
        self.linePoints = []
        self.draw_mode = 1
        self.color = random.choice(colorPalette)

    def __repr__(self):
        if not self.is_line():
            return "Not a line yet."

        return "Line from %s to %s" % (self.linePoints[0], self.linePoints[-1])

    def is_shape(self):
        if len(self.linePoints) >2:
            return True
        return False

    def is_line(self):
        if len(self.linePoints) > 1:
            return True
        return False

    def add_linepoint(self, x, y):
        self.linePoints.append((x,y))

    def draw_line(self, screen):
        # if not a line yet, don't draw!
        if not self.is_line():
            return
        for place, point in enumerate(self.linePoints):
            # skip the first point, there won't be something before it
            if place == 0:
                continue
            pygame.draw.line(screen, self.color, point, self.linePoints[place - 1])

    def draw_circle(self, screen):
        for point in self.linePoints:
            pygame.draw.circle(screen, self.color, point, 5)

    def draw(self, screen):
        if self.draw_mode == 1:
            self.draw_line(screen)

        elif self.draw_mode == 2:
            self.draw_shape(screen)

        elif self.draw_mode == 3:
            self.draw_circle(screen)

    def draw_shape(self, screen):
        if not self.is_line():
            return
        if not self.is_shape():
            return
        pygame.draw.polygon(screen, self.color, self.linePoints)




# set the start points to the center of the screen
plusX = screenWidth // 2
plusY = screenHeight // 2
centerPoint = (screenWidth // 2, screenHeight // 2)


def draw_flat_line(screen, x1, y1, length, color):
    for x in range(x1, x1 + length):
        pygame.gfxdraw.pixel(screen, x, y1, color)


def draw_vertical_line(screen, x1, y1, length, color):
    for y in range(y1, y1 + length):
        pygame.gfxdraw.pixel(screen, x1, y, color)


def draw_plus_sign(screen, x, y, size, color):
    draw_flat_line(screen, x - (size // 2), y, size, color)
    draw_vertical_line(screen, x, y - (size // 2), size, color)

linePoints = []
lines = [Line()]
DRAW_LINES = 1
DRAW_SHAPE = 2
DRAW_CIRCLE = 3

while running:
    screen.fill(black)

    if pygame.mouse.get_focused():
        plusX, plusY = pygame.mouse.get_pos()

    draw_plus_sign(screen, plusX, plusY, 15, white)

    key = pygame.key.get_pressed()

    if key[pygame.K_1]:
        lines[-1].draw_mode = DRAW_LINES

    if key[pygame.K_2]:
        lines[-1].draw_mode = DRAW_SHAPE

    if key[pygame.K_3]:
        lines[-1].draw_mode = DRAW_CIRCLE


    for line in lines:
        line.draw(screen)
        
    for event in pygame.event.get():
        # our mouse click is checked here
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:# left click
                lines[-1].add_linepoint(plusX, plusY)
            if event.button == 3:
                newLine = Line()
                newLine.add_linepoint(plusX, plusY)
                lines.append(newLine)

    # add check for the space bar and add a new coordinate to have a plus sign, and the selected color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick()






