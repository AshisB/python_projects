from turtle import Turtle,Screen
from pong_paddle import PongPaddle
from ball import Ball
from score import Score
from divider import Divider
import time



#setting up the screen
screen=Screen()
screen.setup(800,600)
screen.bgcolor('black')
screen.title('Pong')
screen.listen()
screen.tracer(0)


# creating the paddle
r_paddle=PongPaddle(360,0)
l_paddle=PongPaddle(-360,0)
ball=Ball()
score=Score()
divider = Divider()


# Move paddle

screen.onkey(r_paddle.MoveUp, 'Up')
screen.onkey(r_paddle.MoveDown, 'Down')
screen.onkey(l_paddle.MoveUp, 'w')
screen.onkey(l_paddle.MoveDown, 's')

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(ball.speedball)
    ball.MoveBall()

    if ball.xcor() > 410 or ball.xcor() < -410:
        if ball.xcor() > 0:
            flag = 'l'
        else:
            flag = 'r'
        score.ScoreUpdate(flag)
        ball.ResetBall()

    else:
        if ball.ycor()>280 or ball.ycor()<-280:
            ball.BounceWall()

        # For right paddle collision
        y_r_diff = ball.distance(r_paddle)


        # For left paddle collision
        y_l_diff = ball.distance(l_paddle)

        if (y_r_diff < 50 and 330 < ball.xcor() < 360 and ball.movex > 0) or (y_l_diff < 50 and -360 < ball.xcor() < -330 and ball.movex < 0):
            ball.BounceBall()
















screen.mainloop()

# screen.exitonclick()