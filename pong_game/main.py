from turtle import Turtle,Screen
from paddle import Paddle

#setting up the screen
screen=Screen()
screen.setup(800,600)
screen.bgcolor('black')
screen.title('Pong')



# creating the paddle
paddle=Paddle()
paddle.CreatePaddle()















screen.exitonclick()