import os
import time
import random
import pyautogui
from humancursor import SystemCursor

class Helpers:
    def __init__(self):
        self.cursor=SystemCursor()
        

    def rand_helper_func(self,range_start,range_stop):
        random_number=random.randint(range_start,range_stop)
        return random_number
    
    def rand_forminput_func(self,xcor,ycor):
        new_xcor=xcor+self.rand_helper_func(0,15)
        new_ycor=ycor+self.rand_helper_func(0,2)
        return new_xcor,new_ycor
    
    def humanlike_move_click(self,xcor,ycor):
        target_x,target_y=self.rand_forminput_func(xcor,ycor)
        self.cursor.move_to([target_x,target_y])
        self.cursor.click_on([target_x,target_y])
        print('Succesfuly clicked')

    
    def random_typing(self,char_string):
        time.sleep(1)
        for char in char_string:
            # Type character
            pyautogui.write(char)
            
            # Variable delay based on character
            if char in ".,!?":
                delay = random.uniform(0.3, 0.6)  # Pause at punctuation
            elif char == " ":
                delay = random.uniform(0.15, 0.3)  # Slight pause between words
            else:
                delay = random.uniform(0.05, 0.15)  # Normal typing
            
            # 2% chance of micro-hesitation
            if random.random() < 0.02:
                delay += random.uniform(0.2, 0.5)
            
            time.sleep(delay)
        
        # Brief pause before hitting tweet button
        time.sleep(random.uniform(0.5, 1.2))
        print("Succesfully done")
