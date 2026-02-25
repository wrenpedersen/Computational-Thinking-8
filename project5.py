import turtle, math, time, random
from utils import *

# Section 1: Setup
# TODO - create your player character and any other sprites
# TODO - set your background
# TODO - set the starting value for your variables
sprite_list = []
lives = 5
set_background("summer") 
s1 = create_sprite("trutle2")
#s2 = create_sprite("popsicle")
# Section 2: Controls
# TODO - define your controls
# TODO - pick keys for each control
def move_up():
    x=s1.xcor()
    y=s1.ycor() + 8
    s1.goto(x,y)

def move_down():
    x=s1.xcor()
    y=s1.ycor() - 8
    s1.goto(x,y)

def move_left():
    x=s1.xcor() - 8 
    y=s1.ycor() 
    s1.goto(x,y)

def move_right():
    x=s1.xcor() + 8
    y=s1.ycor() 
    s1.goto(x,y)
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeypress(move_down, "Down")
window.onkeypress(move_up, "Up")



# Section 3: Game Loop
window.listen()
for i in range(10000000000):

    if i % 50 == 0:
        x = random.randint(-300,300)
        item = create_sprite("popsicle", x, 400)
        item.setheading(270)
        sprite_list.append(item)
    for item in sprite_list:
        # item.forward(5)
        item.goto(item.xcor(), item.ycor()-0.1)
        if get_distance(s1,item) < 100:
            lives -= 1
    if lives <= 0:
        print("You lose")
        break
    
    
    
   # popsicle_sprite.goto(random.randint)
    # TODO - add code for automatic actions


    # TODO - make an if statement for ending the game

    
    time.sleep(0.01)
    window.update()
    

	
print("Game Over")