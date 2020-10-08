from graphics import *
from time import *

win = GraphWin("Tetris", 500, 500)
circle = Circle(Point(250, 50), 60)
circle.setFill(color_rgb(100, 255, 50))
circle.draw(win)


while True:
    sleep(0.5)
    key = win.checkKey()
    print(key)
    circle.move(0, 10)
    if key == "Up":
        circle.move(0, -10)
    elif key == "Down":
        circle.move(0, 10)
    elif key == "Left":
        circle.move(-10, 0)
    elif key == "Right":
        circle.move(10, 0)
    else:
        pass
