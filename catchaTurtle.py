"""
Random appearance of the shape on different parts of the screen
The event of a shape being clicked
The score updating
The timer updating

Think about
xPos=random between 0 & 112
yPos=random between 0 & 324
"""
# a121_catch_a_turtle.py
# -----import statements-----
import turtle as trtl
import random as rand

# -----game configuration----
xMin = 0
xMax = 112
yMin = 0
yMax = 324
score = 0

timerUp = False
counterInterval = 1000
color = "red"
shape = "triangle"
size = 2
fontSetup = ("Arial", 20, "normal")
timer = 30
colors = ["red", "blue", "purple", "yellow"]
sizes = [2, 4, 6, 8, 10, 12]


# -----initialize turtle-----
turtle = trtl.Turtle()
turtle.shape(shape)
turtle.turtlesize(size)
turtle.fillcolor(color)
scoreWriter = trtl.Turtle()
scoreWriter.goto(300, -300)

counter = trtl.Turtle()
counter.goto(-300, -300)


# -----game functions--------

def spot_clicked(x, y):
    turtle.goto(rand.randint(xMin, xMax), rand.randint(yMin, yMax))
    scoreChange()
    turtle.stamp()
    chosencolor=rand.choice(colors)
    rand.choice(sizes)
    turtle.fillcolor(chosencolor)

def scoreChange():
    global score
    score += 1
    scoreWriter.clear()
    scoreWriter.write(score, font=fontSetup)
    print(score)

def countdown():
    global timer, timerUp
    counter.clear()
    if timer <=0:
        counter.write("Time's Up", font=fontSetup)
        timerUp = True
    else:
        counter.write("Timer: " + str(timer), font=fontSetup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counterInterval)


# -----events----------------
turtle.onclick(spot_clicked)

wn = trtl.Screen()
wn.bgcolor("lightblue")
wn.ontimer(countdown, counterInterval)
wn.mainloop()
