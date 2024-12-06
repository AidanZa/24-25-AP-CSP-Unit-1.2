import turtle as trtl
import random as rand

# Intialuize Variables
wn = trtl.Screen()
maze_painter = trtl.Turtle()
length = 40
path_width = 30
maze_painter.speed(0)



# setup turtle
maze_painter.left(90)
maze_painter.pensize(5)

# Draw maze
# Process:
# draw line
# turn left
# increment length
# repeat

# randomize location of doors and barriers in wall


def draw_barrier():
    maze_painter.right(90)
    maze_painter.forward(path_width)
    maze_painter.backward(path_width)
    maze_painter.left(90)

for wall in range(21):
    gap_space = rand.randint(0, length - path_width)
    door_space = 0
    maze_painter.forward(gap_space)
    maze_painter.penup()
    maze_painter.forward(path_width)
    maze_painter.pendown()
    if (wall > 5):
        door_space = rand.randint(0, length - path_width - gap_space)
        maze_painter.forward(door_space)
        draw_barrier()
    maze_painter.forward(length - gap_space - path_width - door_space)
    maze_painter.left(90)
    length += 15
    maze_painter.hideturtle()

wn.listen()
wn.mainloop()