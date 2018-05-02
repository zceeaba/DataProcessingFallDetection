import turtle
def generateSquarePoints(i):
    """ generate points for a square of any size """
    return [(i, 0), (i, i), (0, i), (0, 0)]

def drawPolyLine(start, points, lineColour, fillColour):
    """ draw shapes using a list of coordinates """
    turtle.pencolor(lineColour)
    turtle.fillcolor(fillColour)

    turtle.penup()

    turtle.goto(start)  # make the turtle go to the start position

    turtle.pendown()
    turtle.begin_fill()

    x, y = start

    for point in points:  # go through a list of (relative) points
        dx, dy = point
        turtle.goto(x + dx, y + dy)
    turtle.goto(start)  # connect them to start to form a closed shape

    turtle.end_fill()
    turtle.penup()

if __name__ == "__main__":

    def testPolyLines():
        """ test shapes shape drawing functions """
        # First square

        squareShape = [(4,164),(103,164),(103,451),(4,451)]
        #squareShape = [(4,4),(20,4),(20,20),(4,20)]
        drawPolyLine((-200, -200), squareShape,"black","yellow")
        pointshape=[[57,312],[57,312],[57,312],[57,312]]
        drawPolyLine((-200,-200),pointshape,"black","black")
    """
        # Second square
        biggerSquareShape = generateSquarePoints(100)
        drawPolyLine((-200, 200), biggerSquareShape, lineColour="green")

        # A triangle
        triangleShape = [(200, 0), (100, 100), (0, 0)]
        drawPolyLine((100, -100), triangleShape, fillColour="green")

    """
    def main():
        testPolyLines()
        turtle.done()

    main()
