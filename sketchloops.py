import turtle

running = True
win = turtle.Screen()
pen = turtle.Turtle()

while running:
    entered = input('Enter triangle, square, pentagon, hexagon, dodecagon or exit:')

    if entered == 'triangle':
        for side in range(3):
            pen.forward(100)
            pen.right(120)

    elif entered == 'square':
        for side in range(4):
            pen.forward(100)
            pen.right(90)

    elif entered == 'pentagon':
        pen.down()
        for side in range(5):
            pen.forward(100)
            pen.right(72)

    elif entered == 'hexagon':
        pen.down()
        for side in range(6):
            pen.forward(100)
            pen.right(60)

    elif entered == 'dodecagon':
        pen.down()
        for side in range(12):
            pen.forward(100)
            pen.right(30)

    elif entered == 'exit':
        pen.up()
        running = False
        print('Goodbye...')
    else:
        print('not a valid command')


