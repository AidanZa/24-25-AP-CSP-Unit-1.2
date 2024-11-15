#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
ground_height = 0
apple_letter_x_offest = -25
apple_letter_y_offest = -50

wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = trtl.Turtle()
apple.penup()
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def drop_apple():
  apple.goto(apple.xcor(), ground_height)
  apple.hideturtle()
  apple.color("white")
  apple.write("A", font=("Arial", 74, "bold"))


#-----function calls-----
draw_apple(apple)
wn.onkeypress(drop_apple, "a")

wn.listen()
wn.mainloop()