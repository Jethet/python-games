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
ball = turtle.Turtle()
ball.speed(0)  #speed of animation, set to maximum
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2


# Define player_a function
def player_a_up():
  y = player_a.ycor()
  y += 20
  player_a.sety(y)

def player_a_down():
  y = player_a.ycor()
  y -= 20
  player_a.sety(y)
  
# Define player_b function
def player_b_up():
  y = player_b.ycor()
  y += 20
  player_b.sety(y)

def player_b_down():
  y = player_b.ycor()
  y -= 20
  player_b.sety(y)

# Keyboard binding
win.listen()
win.onkeypress(player_a_up, "1")
win.onkeypress(player_a_down, "2")
win.onkeypress(player_b_up, "9")
win.onkeypress(player_b_down, "0")

# Main loop
while True:
  win.update()
  
  # Move the ball
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)
  
  # Set border (screen height 600, ball 20x20, means border is 290 up or 290 down)
  if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1  #reverses the direction
    
  if ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1
    
  # Set border (screen width 800, ball 20x20, means border is 390 up or 390 down)
  if ball.xcor() > 390:
    ball.goto(0, 0)
    ball.dx *= -1
    
  if ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dx *= -1  
  
  # Paddle and ball collisions: ball hits between top and bottom of player square
  if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player_b.ycor() + 40 and ball.ycor() > player_b.ycor() -40):
    ball.setx(340)
    ball.dx *= -1
      
  if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player_a.ycor() + 40 and ball.ycor() > player_a.ycor() -40):
      ball.setx(-340)
      ball.dx *= -1
    