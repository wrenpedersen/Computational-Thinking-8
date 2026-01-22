import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 =-325
y1 =100
x2 =-325
y2 =-150
x3 =-325
y3 =200
x4 =-325
y4 =-25


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("summer")
t1 = create_sprite("icecream2",x2,y3)
t2 = create_sprite("pineapple",x2,y2)
t3 = create_sprite("popsicle",x2,y4)
t4 = create_sprite("cool_dog",x2,y1)
 

# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
#The ice cream sprite is fastest beacuse 13 is the greatest number and the pineapple ius slowest because 6 is the smallest number. 

for i in range(100):
      x1 += (10)
      x2 += (6) 
      x3 += (13)
      x4 += (8)

      t1.goto(x1, y1)
      t2.goto(x2, y2)
      t3.goto(x3, y3)
      t4.goto(x4, y4)

      window.update()
      time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
      print("player 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
      print("player 2 wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
      print("player 3 wins!")
elif x4 >= x1 and x4 >= x3 and x4 >= x2:
      print("player 4 wins!")


turtle.exitonclick()