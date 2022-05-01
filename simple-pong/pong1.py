import turtle

win = turtle.getscreen()

# win = turtle.Screen
win.title("Simple Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)  #stops window from updating, speeds up the game

# Player A
player_a = turtle.Turtle()
player_a.speed(0)  #speed of animation, set to maximum
player_a.shape("square")
player_a.color("white")
player_a.shapesize(stretch_wid=5, stretch_len=1)
player_a.penup()
player_a.goto(-350, 0)

# Player B
player_b = turtle.Turtle()
player_b.speed(0)  #speed of animation, set to maximum
player_b.shape("square")
player_b.color("white")
player_b.shapesize(stretch_wid=5, stretch_len=1)
player_b.penup()
player_b.goto(350, 0)

# Ball


# Main loop
while True:
  win.update()
  

