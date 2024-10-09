import turtle
import time

# Variables Area
path = r"teddyBear.gif"
clicks=0
timeLeft=10
startGame=False

# Factions Area
def clickCounter(x,y):
    global clicks,startGame
    if startGame==True:
        clicks +=1
        score.clear()
        score.write(f"Clicks:{clicks}", align="center", font=("Arial", 24, "normal"))
    else:
        return
    
def timeCountdown(timeLeft):
    while timeLeft>0:
        time.sleep(1)
        timeLeft-=1
        timer.clear()
        timer.write(f"{timeLeft}", align="center", font=("Arial", 24, "normal"))
    timer.clear()
    timer.write(f"Time Stoped", align="center", font=("Arial", 24, "normal"))

# Main Code Area
window = turtle.Screen()
window.register_shape(path)
window.title("Click Game")
window.bgcolor("cyan")

bear = turtle.Turtle()
bear.shape(path)
bear.speed(0)

instractions=turtle.Turtle()
instractions.hideturtle()
instractions.color("black")
instractions.penup()
instractions.goto(0,330)
instractions.write(f"The aim of the game is to get the most clicks in the next 10 seconds", align="center", font=("Arial", 22, "normal"))
instractions.goto(0,300)
instractions.write(f"Click on the bear and click as many clicks as you can!", align="center", font=("Arial", 22, "normal"))

timer=turtle.Turtle()
timer.hideturtle()
timer.color("black")
timer.penup()
timer.goto(0,230)
timer.write(f"Time", align="center", font=("Arial", 24, "normal"))

score = turtle.Turtle()
score.hideturtle()
score.color("black")
score.penup()
score.goto(0,-300)
score.write(f"Score", align="center", font=("Arial", 24, "normal"))

bear.onclick(clickCounter)
if (startGame==False):
    startGame=True
    timeCountdown(10)
    startGame=False

window.mainloop()