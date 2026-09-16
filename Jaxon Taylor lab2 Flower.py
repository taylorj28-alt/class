import turtle
t = turtle.Turtle()


def drawsquare(t, sideLength):
 for i in range(4):
    t.forward(sideLength)
    t.speed(20)
    t.right(90)
   
    
def drawFlower(numSquares):
 flower_turtle = turtle.Turtle()
 angle = 360 / numSquares
#change the amout of petle in the flower
 for j in range(numSquares):
    drawsquare(flower_turtle, 100)
    flower_turtle.right(angle)

numSquares = 50
#change the number of Squares in the flower
drawFlower(numSquares)

drawsquare(t, 100)


x = ""
input(x)
#this is here just to stop it the drawing to desapier