import turtle

speed=1

s=turtle.Screen()
s.bgcolor("black")

a=turtle.Turtle()
a.color("blue")
a.penup()
a.speed(0)

b=turtle.Turtle()
b.color("green")
b.pensize(5)
b.speed(0)
b.penup()
b.goto(-300,-300)
b.pendown()
for i in range(4):
    b.forward(600)
    b.left(90)
    b.hideturtle()

def turnleft():
    a.left(30)

def turnright():
    a.right(30)

s.listen()
s.onkeypress(turnleft,"Left")
s.onkeypress(turnright,"Right")

while True:
    a.forward(speed)

    
turtle.mainloop()