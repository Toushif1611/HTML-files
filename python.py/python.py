import turtle
s=turtle.Screen()
s.bgcolor("black")

a=turtle.Turtle()
a.color("blue")
a.penup()
a.speed(0)

speed=1

def turnleft():
    a.left(30)

def turnright():
    a.right(30)

s.listen()
s.onkeypress(turnleft,"Left")
s.onkeypress(turnright,"Right")

while True:
    a.forward("speed")

    
turtle.mainloop()