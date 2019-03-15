
import turtle as vaughan


t = vaughan.Pen()
vaughan.bgcolor("black")
sides = 4
colors = ["green", "yellow", "red", "blue", "purple", "orange"]

yourName = vaughan.textinput("Enter your name, please...", "What is your name?")
for x in range(360):
    t.pencolor(colors[x%sides])
    t.penup()
    t.forward(x*sides)
    t.pendown()
    t.write(yourName, font = ("Arial", int((x+4)/4), "bold"))
    t.left(360/sides + 2)
    #t.width(x*sides/200)


"""
import turtle as vaughan


t = vaughan.Pen()
#t.pencolor("red")
sides = 5
colors = ["green", "yellow", "red", "blue", "purple", "orange"]
#数组定义格式  ["", ""]
#t.    这里的. 是调用对象的函数的符号
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)

"""
"""
import turtle
t = turtle.Pen()
for x in range(4):
    t.circle(100)
    t.left(90)
"""

"""
import turtle as vaughan


t = vaughan.Pen()
#t.pencolor("red")
colors = ["green", "yellow", "red", "blue", "purple", "black", "white"]
for x in range(300):
    t.pencolor(colors[x%7])
    t.circle(x)
    t.left(150)

"""


"""

import turtle

t = turtle.Pen()
for x in range(100):
    t.forward(x)
    t.left(91)
"""