# import the turtle module
import turtle
import time

# set up the screen
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("green")

# create the snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# define the main game loop
while True:
    win.update()

    # move the snake
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

    # set up a delay
    time.sleep(0.1)

# start the game
turtle.mainloop()
