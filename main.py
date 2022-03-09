#ping pong game

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0) #it will turn off the animation that is created in the beginning

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkeypress(l_paddle.go_down, "s")

#u need to manually turnon the animation after paddle is already at its place
game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    #detect collision with (paddle)
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
       ball.bounce_x()

    #detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_postiton()
        scoreboard.l_point()

     #detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_postiton()
        scoreboard.r_point()

    # Game over when reaches score 10
    if scoreboard.l_score == 10:
        game_is_on = False
        scoreboard.game_over_A() 
    elif scoreboard.r_score == 10:
        game_is_on = False
        scoreboard.game_over_B()        


screen.exitonclick()