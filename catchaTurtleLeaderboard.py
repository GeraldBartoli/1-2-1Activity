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
import leaderboard as lb

# -----game configuration----
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name:")
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
timer = 5
colors = "red", "blue", "purple", "yellow"

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
        manage_leaderboard()
    else:
        counter.write("Timer: " + str(timer), font=fontSetup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counterInterval)



# manages the leaderboard for top 5 scorers
def manage_leaderboard():
    global leader_scores_list
    global leader_names_list
    global score
    global spot

    # load all the leaderboard records into the lists
    lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

    # TODO
    if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

    else:
        lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)
# -----events----------------
turtle.onclick(spot_clicked)

wn = trtl.Screen()
wn.bgcolor("lightblue")
wn.ontimer(countdown, counterInterval)
wn.mainloop()
