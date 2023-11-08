import turtle

s=turtle.Screen()
s.bgcolor("black")

a=turtle.Turtle("circle")
a.color("green")
a.speed(0)
a.penup()
a.goto(0, 200)
a.dy = 0

gravity = 0.1

while True:
    a.dy -= gravity
    a.sety(a.ycor() + a.dy)
    #check for a bounce
    if a.ycor()<-300:
        a.dy *=-1



s.mainloop()

