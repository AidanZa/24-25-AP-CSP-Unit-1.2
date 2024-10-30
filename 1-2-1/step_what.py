# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
score=0

#-----game configuration----
spot_color = "red"
spot_size = 2
spot_shape = "circle"

#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)

#-----game functions--------
def change_position():
    spot.penup()
    new_xpos=rand.randint(-400,400)
    new_ypos=rand.randint(-300,300)
    spot.goto(new_xpos,new_ypos)
    update_score_for_spot(new_xpos,new_ypos)

def spot_clicked(x,y):
    change_position()

def update_score_for_spot(x,y):
    global score
    score += 1
    print(score)

#-----events----------------
spot.onclick(spot_clicked)
spot.onclick(update_score_for_spot)
wn = trtl.Screen()
wn.mainloop()