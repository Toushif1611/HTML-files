import turtle

s=turtle.Screen()
s.bgcolor("black")
s.tracer(0)

b=turtle.Turtle()
b.color("green")
b.pensize(5)
b.speed(0)
b.penup()
b.goto(-320,-320)
b.pendown()
for i in range(4):
    b.forward(630)
    b.left(90)
    b.hideturtle()

a=turtle.Turtle("circle")
a.color("green")
a.speed(0)
a.penup()
a.goto(0, 200)
a.dx = 2
a.dy = 0

gravity = 0.1

while True:
    s.update()
    a.dy -= gravity
    a.setx(a.xcor() + a.dx)
    a.sety(a.ycor() + a.dy)
    #check for a wall collision
    if a.xcor() > 300 or a.xcor() < -300:
        a.dx *=-1
    #check for a bounce
    if a.ycor()<-300:
        a.dy *=-1



s.mainloop()

