import turtle, time, random
from utils import *

# Section 1 - setup
# TODO - set a background using 
set_background("spring")

# TODO - create at least two variables and set their starting value. ex: cookies = 0
sprite1 = create_sprite("flower", -100, 100)
# sprite2 = create_sprite("Flowerbouquet")
Flower = 0
cost = 0

# OPTIONAL: use this invisible alien to say a message
#message_sprite = t1("flower", -200,200)
#message_sprite.hideturtle



# Section 2 - controls
# TODO - define an action. ex: def my_control()
def make_Flower ():
    global Flower
    Flower += 1
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    create_sprite("flower",x,y)
# TODO - choose a key to do the action. ex: 
window.onkeypress(make_Flower, "space")

# TODO - make a second control
def make_flower_bouquet (): 
    global cost, flower_bouquet
    if Flower >= 10:
        cost = cost * 2
        flower_bouquet += 1
        Flower -= 10
        
        x = 400 + 120*flower_bouquet
        y = -250
        create_sprite ("flower_bouquet",x,y)
window.onkeypress(make_flower_bouquet, "c")




# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    # message_sprite.clear()
    # message_sprite.write("Hello")

    time.sleep(0.01)
    window.update()