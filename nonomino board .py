import turtle
turtle.speed(10000)

def drawSquare(t, squareSize):

    for i in range(4):
        t.forward(squareSize)
        t.right(90)
drawSquare(turtle.Turtle(), 4)
def drawpiece1(t, height, squareSize):

    for i in range(height):
        t.fillcolor("indigo")
        t.begin_fill()
        drawSquare(t, squareSize)
        t.forward(squareSize)
        t.end_fill()
def drawpiece2(t, height, squareSize):

    for i in range(height):
        t.fillcolor("blue")
        t.begin_fill()
        drawSquare(t, squareSize)
        t.forward(squareSize)
        t.end_fill()

def drawGrid(t, size, squareSize):

    for i in range(size):
        drawRow(myTurtle, size, squareSize)
        t.left(180)
        t.forward(squareSize*size)
        t.left(90)
        t.forward(squareSize)
        t.left(90)



#drawpiece1(turtle.Turtle(),3,20)
#drawpiece2(turtle.Turtle(),1,20)


def drawNonomino(t, squareSize):
    
        for i in range(3):
            t.fillcolor("red")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        for i in range(6):
            t.fillcolor("blue")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        t.left(180)
        t.forward(squareSize*9)
        t.left(90)
        t.forward(squareSize)
        t.left(90)
        for i in range(3):
            t.fillcolor("red")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        for i in range(3):
            t.fillcolor("green")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        for i in range(3):
            t.fillcolor("blue")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        t.left(180)
        t.forward(squareSize*9)
        t.left(90)
        t.forward(squareSize)
        t.left(90)
        for i in range(1):
            t.fillcolor("orange")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        for i in range(3):
            t.fillcolor("red")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        for i in range(5):
            t.fillcolor("green")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        t.left(180)
        t.forward(squareSize*9)
        t.left(90)
        t.forward(squareSize)
        t.left(90)
        for i in range(2):
            t.fillcolor("orange")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        for i in range(2):
            t.fillcolor("pink")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        for i in range(4):
            t.fillcolor("purple")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        for i in range(1):
            t.fillcolor("green")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        t.left(180)
        t.forward(squareSize*9)
        t.left(90)
        t.forward(squareSize)
        t.left(90)
        for i in range(3):
            t.fillcolor("orange")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        for i in range(2):
            t.fillcolor("pink")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        for i in range(4):
            t.fillcolor("purple")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        t.left(180)
        t.forward(squareSize*9)
        t.left(90)
        t.forward(squareSize)
        t.left(90)
        for i in range(3):
            t.fillcolor("orange")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        for i in range(1):
            t.fillcolor("pink")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        for i in range(4):
            t.fillcolor("magenta")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        for i in range(1):
            t.fillcolor("purple")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        t.left(180)
        t.forward(squareSize*9)
        t.left(90)
        t.forward(squareSize)
        t.left(90)
        for i in range(2):
            t.fillcolor("cyan")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        for i in range(2):
            t.fillcolor("pink")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        for i in range(4):
            t.fillcolor("magenta")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        for i in range(1):
            t.fillcolor("yellow")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        t.left(180)
        t.forward(squareSize*9)
        t.left(90)
        t.forward(squareSize)
        t.left(90)
        for i in range(3):
            t.fillcolor("cyan")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        for i in range(2):
            t.fillcolor("pink")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        for i in range(1):
            t.fillcolor("magenta")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
        for i in range(3):
            t.fillcolor("yellow")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
            t.end_fill()
        t.left(180)
        t.forward(squareSize*9)
        t.left(90)
        t.forward(squareSize)
        t.left(90)
        for i in range(4):
            t.fillcolor("cyan")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
            t.end_fill()
        for i in range(5):
            t.fillcolor("yellow")
            t.begin_fill()
            drawSquare(t, squareSize)
            t.forward(squareSize)
            t.end_fill()
            t.end_fill()

#drawNonomino(turtle.Turtle(), 20)



print(3)
