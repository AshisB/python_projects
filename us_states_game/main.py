import pandas as pd
from turtle import Turtle,Screen
from state import State
from score import Score

screen=Screen()
turtle=Turtle()
state=State()
score=Score()


#This is for the background of the game. Map of US
screen.addshape('blank_states_img.gif')
turtle.shape('blank_states_img.gif')  

answers=[]
states_all_data=pd.read_csv('50_states.csv')
states_list=states_all_data['state'].to_list()


#This for taking input from the user
screen.title('US STATES GAME')
for _ in range(50):
    state_name=screen.textinput('Input State','Enter next US state').title()
    while state_name in answers:
        state_name=screen.textinput('Already Exist!!!','Enter next US state').title()
        #Taking out xa nd y cordinates
    if state_name in states_list:
        state_data=states_all_data[states_all_data['state']==state_name]
        x_cor=int(state_data.x)
        y_cor=int(state_data.y)
        state.LocateState(x_cor,y_cor,state_name)
        score.update()
        answers.append(state_name)
         
    score.UpdateAttempt()
                  
















screen.mainloop()