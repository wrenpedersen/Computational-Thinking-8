# Section 1 - Your code
from utils import *
set_background("summer")

s1 = create_sprite("icecreamcone", 100, 100)
s2 = create_sprite("corgi", -100, 100)
s3 = create_sprite("turtle", -100, -100)
s4 = create_sprite("pineapple", 100, -100)

message1 = create_sprite("alien",-225,175)
message1.color("pink")
message1.write("Wren",font = ("Arial", 60, "bold"))
message1.hideturtle()

message2 = create_sprite("alien",-200,-250)
message2.color("black")
message2.write("Your motto",font = ("Arial", 40, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()