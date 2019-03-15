import turtle

t = turtle.Pen()
t.speed(10)
turtle.onscreenclick(t.setpos)

for i in range(200):
    t.left(99)
    t.forward(i)