import pandas as pd
from turtle import Turtle,Screen
from state import State
from score import Score
import time

screen=Screen()
turtle=Turtle()
state=State()
score=Score()



try:
    screen.addshape('blank_states_img.gif')
    turtle.shape('blank_states_img.gif')
    print("Shape loaded successfully")
except Exception as e:
    print(f"Error loading shape: {e}")
    print("Continuing without the shape...")

answers=[]
remaining_states=[]
states_all_data=pd.read_csv('50_states.csv')
states_list=states_all_data['state'].to_list()


#This for taking input from the user
screen.title('US STATES GAME')
for _ in range(50):
    state_name=screen.textinput(f'Attempt:{score.attempt}/50' if score.attempt>0 else 'Guess the State','Enter next US state').title()
    while state_name in answers:
        state_name=screen.textinput(f'Already Exist!!!,{score.attempt}/50' if score.attempt>0 else "" ,'Enter next US state').title()
    if state_name=='Exit':
        break 
       
        #Taking out xa nd y cordinates
    if state_name in states_list:
        state_data=states_all_data[states_all_data['state']==state_name]
        x_cor=state_data['x'].item()
        y_cor=state_data['y'].item()
        state.LocateState(x_cor,y_cor,state_name)
        score.update()
        answers.append(state_name)
    score.UpdateAttempt()



#After game ends,also to generate csv 
if score.score<50:
    for answer in answers:
        states_all_data=states_all_data[states_all_data['state']!=answer]  
    remaining_states=states_all_data
    df=pd.DataFrame({'Remaining States Name': remaining_states['state']})
    df.to_csv('remaining_state.csv', index=False)

                













score.DisplayScoreFinal()
time.sleep(5)
screen.destroy()


screen.mainloop()