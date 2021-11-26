import cairo, sys, argparse, copy, math, random

float_gen = lambda a, b: random.uniform(a,b) #used to generate random colors

colors = []
for i in range(15):  #loop to create random RGB values
    colors.append((float_gen(.4, .75), float_gen(.4, .75),float_gen(.4, .75), ))

def octagon(x_orig, y_orig, side):   #octogon function will return an array of points
    x = x_orig   # x axis origin point
    y = y_orig   # y axis origin point
    d = side / math.sqrt(2) #diagonal lines for sides
    
    oct = []
    oct.append((x,y))
    
    x+= side #top of octogon followed by each side clockwise
    oct.append((x,y))
    
    x += d 
    y += d
    oct.append((x,y))
    
    y += side
    oct.append((x,y))
    
    x -= d
    y += d
    oct.append((x,y))
    
    x -= side
    oct.append((x,y))
    
    x -= d
    y -= d
    oct.append((x,y))
    
    y -= side 
    oct.append((x,y))
    
    x += d 
    y -= d
    oct.append((x,y))
    
    return oct

def deform (shape, iterations, variance): #moves midpoint given variance to create deformations 
    for i in range(iterations):
        for j in range(len (shape)-1, 0, -1): #moving backward through array 
            midpoint = ((shape[j-1][0]+ shape[j][0])/2 + float_gen(-variance, variance), (shape[j-1][1]+ shape[j][1])/2 + float_gen(-variance, variance))
            shape.insert(j,midpoint)
    return shape


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", default= 1000, type=int)
    parser.add_argument("--height", default= 1500, type=int)
    parser.add_argument("-i","--initial", default= 120, type=int) #sets the initial deformation on the shape 
    parser.add_argument("-d","--deviation", default= 50, type=int) #deviation for the layers
    parser.add_argument("-bd","--basedeforms", default= 1, type=int) #how many times the octogon is deformed before it is layered
    parser.add_argument("-fd","--finaldeforms", default= 3, type=int) #number of times the octogan is deformed as it is layered
    parser.add_argument("-mins","--minshapes", default= 20, type=int) #min number of shapes deformed 
    parser.add_argument("-maxs","--maxshapes", default= 25, type=int) #max number of shapes deformed 
    parser.add_argument("-sa","--shapealpha", default= .02, type=float) #how transparent the octagon will be, the higher the number the less transparency
    args = parser.parse_args()
    
    width, height = args.width, args.height 
    initial = args.initial
    deviation = args.deviation 
    
    basedeforms = args.basedforms
    finaldeforms = args.finaldeforms
    
    minshapes = args.minshapes
    maxshapes = args.maxshapes
    
    shapealpha = args.shapealpha
    
    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height) #image surface
    cr = cairo.Context(ims)
    
    cr.set_source_rgb(.9, .9, .9)  #white background
    cr.rectangle(0, 0, width, height)
    cr.fill()
    
    cr.set_line_width(1)
    
    for octo in range(-int(height*.2), int(height*1.2), 60):
        cr.set_source_rgba(random.choice(colors)[0], random.choice(colors)[1],random.choice(colors)[2], shapealpha)   #color and transparency 
        shape = octagon(random.randit(-100, width+100), octo, random.randint(100, 300))
        baseshape = deform(shape, basedeforms, initial)
        for layr in range(random.randint(minshapes, maxshapes)):
            tempshape = copy.deepcopy(baseshape)
            layer = deform(tempshape, finaldeforms, deviation)
            
            for i in range(len(layer)):
                cr.line_to(layer[i][0], layer[i][1])
            cr.fill()
    ims.write_to_png('watercolor.png')

if __name__ == "__main__":
    main()
            
            