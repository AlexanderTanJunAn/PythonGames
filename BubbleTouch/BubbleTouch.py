import turtle
import random
import math
import os
import winsound

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Simple Python Game as Intro to Classes by Alex")
wn.setup(width=700, height=700)
wn.tracer(0)
wn.bgpic("bg.gif")

class Game(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(-290, 310)
        self.score = 0

    def update_score(self):
        self.clear()
        self.write("Score: {}".format(self.score), False, align="left",font=("Arial", 14, "normal"))
    
    def change_score(self, points):
        self.score += points
        self.update_score()

    def play_sound(self):
        os.system("afplay bounce.wav&")
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)   #controls animation speed, 0 means no animate just draw as fast as possible
        self.color("white")
        self.pensize(5)     #width of border (i.e 5px)

    def draw_border(self):
        self.penup()
        self.goto(-300, -300)
        self.pendown()
        self.goto(-300, 300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)

class Player(turtle.Turtle):    #Player is a child class of turtle class

    def __init__(self):     #Class constructor (init Player)
        turtle.Turtle.__init__(self)    #Self refers to turtle object (init Turtle)
        self.penup()
        self.shape("triangle")
        self.color("white")
        self.speed = 0.4

    def move(self):
        self.forward(self.speed)

        # Border checking
        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)

    def turnleft(self):
        self.left(30)

    def turnright(self):
        self.right(30)
    
    def increasespeed(self):
        self.speed += 0.05

    def decreasespeed(self):
        if self.speed > 0.05:
            self.speed -= 0.05

class Goal(turtle.Turtle):
    
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("green")
        self.shape("circle")
        self.speed = 0.4
        self.goto(random.randint(-250,250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))

    def jump(self):
        self.goto(random.randint(-250,250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))

    def move(self):
        self.forward(self.speed)

        # Border checking
        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)

# Create class instances
player = Player()   #an instance of Player class (player object) (self above is player)
border = Border()
game = Game()
game.change_score(0)

# Draw the border
border.draw_border()

# Creating multiple goals
goals = []
for count in range(6):
    goals.append(Goal())

# Keyboard bindings
wn.listen()
wn.onkeypress(player.turnleft, "Left")
wn.onkeypress(player.turnright, "Right")
wn.onkeypress(player.increasespeed, "Up")
wn.onkeypress(player.decreasespeed, "Down")

# Main loop
while True:
    wn.update()
    player.move()

    for goal in goals:
        goal.move()

        if player.distance(goal) < 20:
            goal.jump()
            game.play_sound()
            game.change_score(10)

wn.mainloop()