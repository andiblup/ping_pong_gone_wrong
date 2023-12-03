
from turtle import Screen
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# screen
screen = Screen()
screen.setup(width=1000, height=600)
screen._root.resizable(False, False)
screen.bgcolor("black")
screen.title("PONG")

rPaddle = Paddle((450, 0))
lPaddle = Paddle((-450, 0))
ball = Ball()
score = Scoreboard()


gameloop = True
while gameloop:
    time.sleep(ball.move_speed)
    ball.move()
    screen.listen()
    screen.update()
    titleScore = str(score.l_score) + " : " + str(score.r_score)
    screen.title(titleScore)
    screen.onkeypress(lPaddle.go_up, "w")
    screen.onkey(lPaddle.go_up, "w")

    screen.onkeypress(lPaddle.go_down, "s")
    screen.onkey(lPaddle.go_down, "s")
        
    screen.onkeypress(rPaddle.go_up, "Up")
    screen.onkey(rPaddle.go_up, "Up")
        
    screen.onkeypress(rPaddle.go_down, "Down")
    screen.onkey(rPaddle.go_down, "Down")    
    # print(ball.xcor())
    
    # north / south / wall collisions
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    
    #Detect collision with paddle
    if ball.distance(rPaddle) < 45 and ball.xcor() >= 430 or ball.distance(lPaddle) < 45 and ball.xcor() <= -430:
        ball.bounce_x()
    
    # Detect collision with east / west / wall
    if ball.xcor() <= -510:
        ball.stop_move()
        score.r_points()
        score.update_scoreboard()
        ball.restart()
    elif ball.xcor() >= 510:
        ball.stop_move()
        score.l_points()
        score.update_scoreboard()
        ball.restart()
