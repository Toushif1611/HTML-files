import turtle

s=turtle.Screen()
s.bgcolor("black")

a=turtle.Turtle()
a.shape("turtle")
a.color("blue")
a.speed(0)
a.penup()

speed=1

c=turtle.Turtle()
c.shape("circle")
c.color("red")
c.speed(0)
c.penup()

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

def increadespeed():
    global speed
    speed+=1

def decreasespeed():
    global speed
    speed-=1

s.listen()
s.onkeypress(turnleft,"Left")
s.onkeypress(turnright,"Right")
s.onkeypress(increadespeed,"Up")
s.onkeypress(decreasespeed,"Down")

while True:
    a.forward(speed)
    c.forward(speed)
    if a.xcor() > 300 or a.xcor() < -300 or a.ycor() > 300 or a.ycor() < -300:
        a.right(100)
    if c.xcor() > 290 or c.xcor() < -290 or c.ycor() > 290 or c.ycor() < -290:
        c.right(100)    






s.mainloop()