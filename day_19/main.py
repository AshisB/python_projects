import random
from turtle import Turtle,Screen

screen=Screen()
screen.setup(width=500,height=400)
is_race_on=False

colors=["red","green","blue","yellow","purple","orange"]
user_bet=screen.textinput(title="Make a bet",prompt="Please choose turtle color: red, green, blue, yellow, purple, orange")
user_bet=user_bet.lower()
while True:
    if user_bet in colors:
        break
    else:
        print('You bet is out of our listed turtles.')
        user_bet = screen.textinput(title="Make a bet",prompt="Please choose turtle color: red, green, blue, yellow, purple, orange")
        user_bet = user_bet.lower()


all_kurmas=[]
if user_bet:
    ypos = -150
    for color in colors:
        kurma = Turtle(shape="turtle")
        kurma.color(color)
        kurma.penup()
        kurma.goto(x=-230, y=ypos)
        ypos += 50
        all_kurmas.append(kurma)
    is_race_on=True

    while is_race_on:
        for kurma in all_kurmas:
            random_distance=random.randint(0,10)
            kurma.forward(random_distance)
            # if kurma.pos()[0]>210:
            if kurma.xcor()>210:
                if user_bet==kurma.pencolor():
                    print(f'Your bet {kurma.pencolor()} turtle won the race.')
                else:
                    print(f'Your bet {user_bet} turtle lost {kurma.pencolor()} turtle won.')
                is_race_on=False




screen.exitonclick()
