import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height = 600)
wn.tracer(0) # Turns of the scree updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)


# Main game loop
while True:
    wn.update() 
    move()

wn.mainloop()
