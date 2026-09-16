import turtle

def drawStar(t):

 for _ in range(5):
    t.forward(150)
    t.right(144)



star_turtle = turtle.Turtle()
star_turtle.speed(3)



drawStar(star_turtle)

x = ""
input(x)