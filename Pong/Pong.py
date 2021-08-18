import turtle
import os
import winsound

wn = turtle.Screen()
wn.title("Pong by Alex")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A, left paddle
paddle_a = turtle.Turtle()
paddle_a.speed(0) #Sets speed of paddle animation with 0 being the maximum
paddle_a.shape("square") #Default size is 20x20px
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #100x20px
paddle_a.penup()
paddle_a.goto(-350, 0) #Sets starting point

# Paddle B, right paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0) #Sets speed of paddle animation with 0 being the maximum
paddle_b.shape("square") #Default size is 20x20px
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #100x20px
paddle_b.penup()
paddle_b.goto(350, 0) #Sets starting point

# Ball
ball = turtle.Turtle()
ball.speed(0) #Sets speed of paddle animation with 0 being the maximum
ball.shape("square") #Default size is 20x20px
ball.color("white")
ball.penup()
ball.goto(0, 0) #Sets starting point
ball.dx = 0.08 #moves by 2px
ball.dy = -0.08

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)    #top middle
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor() #.ycor returns y coordinate (from turtle module)
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()  # .ycor returns y coordinate (from turtle module)
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #.ycor returns y coordinate (from turtle module)
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()  # .ycor returns y coordinate (from turtle module)
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen() #Listens for keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")    #Up and Down arrowkeys
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    #Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1   #Reverses the direction
        os.system("afplay bounce.wav&")
        winsound.PlaySound("resources/bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1   #Reverses the direction
        os.system("afplay bounce.wav&")
        winsound.PlaySound("resources/bounce.wav", winsound.SND_ASYNC)

    #Left and right
    if ball.xcor() > 390:
        ball.goto(0, 0)    #Sets ball to center
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)    #Sets ball to center
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1   #Bouncing
        os.system("afplay bounce.wav&")
        winsound.PlaySound("resources/bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1   #Bouncing
        os.system("afplay bounce.wav&")
        winsound.PlaySound("resources/bounce.wav", winsound.SND_ASYNC)
