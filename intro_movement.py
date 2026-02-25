import time, turtle, random
from utils import *
# Section 1: Setup
set_background("castle")
s1 = create_sprite("character1",0,-200)
s2 = create_sprite("turtle", 0, )

# Section 2: define controls
def move_up():
    x = s1.xcor()
    y = s1.ycor() + 30
    s1.goto(x,y)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor() - 30
    s1.goto(x,y)
    
def move_left():
    x = s1.xcor() - 30
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right(): 
    x = s1.xcor() + 30
    y = s1.ycor() 
    s1.goto(x,y)

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")

def draw ():
    s1.pendown ()
window.onkeypress(draw, "c")  
def stop_drawing ():
    s1.penup
window.onkeypress(stop_drawing, "b") 
def erase():
    s1.clear()
window.onkeypress(erase, "e") 
def red_pen():
    s1.color("red")
window.onkeypress(red_pen, "r") 
def green_pen():
    s1.color("green")
window.onkeypress(green_pen, "g") 
def reset():
    s1.goto(0,0)
window.onkeypress(reset, "z") 

def move_up2():
    x = s2.xcor()
    y = s2.ycor() + 20
    s2.goto(x,y)
        
def move_down2():
    x = s2.xcor()
    y = s2.ycor() - 20
    s2.goto(x,y)
    
def move_left2():
    x = s2.xcor() - 20
    y = s2.ycor() 
    s2.goto(x,y)
    
def move_right2(): 
    x = s2.xcor() + 20
    y = s2.ycor() 
    s2.goto(x,y)

window.onkeypress(move_up2, "Up")
window.onkeypress(move_down2, "Down")
window.onkeypress(move_left2, "Left")
window.onkeypress(move_right2, "Right")

# Section 3: define other controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")

# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()