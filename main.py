from turtle import Turtle,Screen
import turtle as t
turobj=Turtle()

def  rotate_clockwise():
    #turobj.right(90)
    turobj.circle(-100,22.5)
def rotate_anti_clockwise():
    #turobj.left(90)
    turobj.circle(100,22.5)
def turn_left():
    new_head=turobj.heading() + 10
    turobj.setheading(new_head)
def turn_right():
    new_head=turobj.heading() - 10
    turobj.setheading(new_head)
def forward_onclick():
    return turobj.forward(10)
def backward_onclick():
    return turobj.backward(10)
def clear():
    turobj.clear()
    turobj.penup()
    turobj.home()

scr=Screen()
### W key press to  move forward
scr.listen()
scr.onkeypress(key="w",fun=forward_onclick)
#### A Key press to move backward
scr.onkeypress(key='a',fun=backward_onclick)
#### S key press to rotate clockwise
scr.onkeypress(key='s',fun=rotate_clockwise)
#### D key press to rotate anti clockwise
scr.onkeypress(key='d',fun=rotate_anti_clockwise)
scr.onkeypress(key='c',fun=turobj.clearstamps)
scr.onkeypress(key='l',fun=turn_left)
scr.onkeypress(key='r',fun=turn_right)
scr.onkeypress(key='c',fun=clear)




scr.exitonclick()



