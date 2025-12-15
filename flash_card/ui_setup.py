COUNTER=5000
from tkinter import *
from tkinter import messagebox
from random import choice
import json
import os
from data_filter import DataFilter

class UI_SETUP:
    def __init__(self,window,background_color,csv_data_list):
        self.window=window
        self.score=0
        self.GetScore()
        self.background_color=background_color
        self.word_list=csv_data_list
        self.CheckReset()
       
       

    def Create_UI(self):
        try:
            self.front_canvas=Canvas(width=800,height=526,bg=self.background_color,highlightbackground=self.background_color)
            self.card_front = PhotoImage(file='./images/card_front.png')
            self.front_canvas.create_image(410, 280, image=self.card_front)
            self.title=self.front_canvas.create_text(410,190,text='',font=('Arial',40,'italic'))
            self.word=self.front_canvas.create_text(410,280,text="",font=('Arial',60,'bold'))
            self.front_canvas.grid(row=0,column=0,columnspan=2)
        except FileNotFoundError:
            self.Label(text='Card front File is Missing')
        
            
      


        try:
            self.card_right=PhotoImage(file='./images/right.png')
            self.button_right=Button(image=self.card_right,bd=0,highlightthickness=0,relief="flat",command=lambda correctflag=1:self.NextWord(correctflag))
            self.button_right.grid(row=1,column=0)
        except FileNotFoundError:
            self.Label(text='Card Right File is Missing')

        try:
            self.card_wrong=PhotoImage(file='./images/wrong.png')
            self.button_wrong=Button(image=self.card_wrong,bd=0,highlightthickness=0,relief="flat",command=lambda wrongflag=0:self.NextWord(wrongflag))
            self.button_wrong.grid(row=1,column=1)
        except FileNotFoundError:
            self.Label(text='Card Wrong File is Missing')


            # FLOATING SCORE (doesn't affect grid layout!)
        self.score_label = Label(
                                    text=f"Score: {self.score}",
                                   font=("Arial", 14, "bold"),
                                   bg="lightgreen",
                                   relief="ridge",
                                   borderwidth=3,
                                   padx=10,
                                   pady=5)
        # Place in top-right corner
        self.score_label.place(relx=0.98, rely=0.02, anchor="ne")    
        self.NextWord(0)



    def NextWord(self,flag):   
        if flag==1:
            self.old_word['correct']=1
            # print(self.old_word)
          
       
        
        new_word_list=[word for word in self.word_list if word['correct']==0]
        # print(new_word_list)
        # print(len(new_word_list))
        try:
            new_word=choice(new_word_list)
        except IndexError:
            self.SaveProgress()
            self.GetScore()
            self.score_label.config(text=f"Score: {self.score}")
            self.CheckReset() 
        else:
            try:
                self.back_canvas.grid_remove()  #removes back card
                self.front_canvas.grid()   #reinitiates front card
            except AttributeError:
                self.front_canvas.grid()   #reinitiates front card
            self.front_canvas.itemconfig(self.title,text='English')
            self.front_canvas.itemconfig(self.word,text=new_word['english'].capitalize())

        # set counter  and disable buttons
        self.counter_running =True
        # self.CheckCounterRunning()  
        if hasattr(self, 'flip_timer_id'):
            self.window.after_cancel(self.flip_timer_id)

        savestatus=self.SaveProgress() #save progress
        if savestatus:
            self.old_word=new_word
            self.flip_timer_id=self.window.after(COUNTER, lambda new_word=new_word:self.FlipCard(new_word))   #count down started again for flipping     
            self.GetScore()
            self.score_label.config(text=f"Score: {self.score}")

         
    def FlipCard(self,new_word):
        self.front_canvas.grid_remove() 
        self.back_canvas=Canvas(width=800,height=526,bg=self.background_color,highlightbackground=self.background_color)
        self.card_back = PhotoImage(file='./images/card_back.png')
        self.back_canvas.create_image(410, 280, image=self.card_back)
        self.title=self.back_canvas.create_text(410,190,text='Nepali',font=('Arial',40,'italic'),fill='white')
        self.word=self.back_canvas.create_text(410,280,text=new_word['nepali'].capitalize(),font=('Arial',60,'bold'),fil='white')
        self.back_canvas.grid(row=0,column=0,columnspan=2)
       
        # reset counter  and enable buttons
        # self.counter_running = False
        # self.CheckCounterRunning()
             
    def SaveProgress(self):
        try:
            with open('./data/word_list.json','w') as f:
                json.dump(self.word_list,f)
        except FileNotFoundError:
              messagebox.showerror('Error','File Missing')
        else:
            return True        
            

    # def CheckCounterRunning(self): we disable it because we donot need disable buttons /not using controlled flow of flip cars
    #     if self.counter_running:
    #         self.button_right.config(state="disabled")
    #         self.button_wrong.config(state="disabled")
    #     else:
    #         self.button_right.config(state="normal")
    #         self.button_wrong.config(state="normal") 


    def CheckReset(self):
        new_word_list=[word for word in self.word_list if word['correct']==0]    
        if len(new_word_list)==0:
            user_choice=messagebox.askokcancel('Congratulations!!',f'You have sucessfully completed this task with score {self.score}.\n Do u want to play & learn again?')
            if user_choice:
                # os.remove("./data/word_list.json")
                for word in self.word_list:
                    word['correct']=0
                try:
                    with open('./data/word_list.json','w') as f:
                        json.dump(self.word_list,f)
                except FileNotFoundError:
                    messagebox.showerror('Error','File Missing')    
                #reseting and restrarting from first
                for widget in self.window.winfo_children():
                    widget.destroy()   
                self.Create_UI()     
            else:
                messagebox.showinfo('Thank You :)','Thank You! for playing.')
                self.window.after(250, lambda: self.window.destroy())
        else:
             self.Create_UI()    

    def GetScore(self):
        try:
            with open('./data/word_list.json','r') as f:
                word_list=json.load(f)
                correct_word_list=[word for word in word_list if word['correct']==1]
                self.score=len(correct_word_list)
        except FileNotFoundError:
            messagebox.showerror('Error','File Missing')
     


#-----------------------------------flow-------------------------------------#
# 1) def Create_UI(self):           we initiates function which is  for setting up  UI
# 2) def CheckCounterRunning(self): inside function create_UI after fininshing UI setup we disable buttons
# using this function it makes controlled flash card flow.
# we are using hasattr buit in function of python to cancel timer when button wrong/right button is clicked
# 3)def FlipCard(self,new_word):    we call this function to flip the first card inside create_UI function
# 4)def CheckCounterRunning(self):  In flip card we again call this function to enabled buttons currently dcomented
# 5)def NextWord(self,flag):      this function activates after we click butoons right and wrong buttons.Button
# important because  it saves progress of user and also checks correct flag to 1 for right answers.

# 6)def SaveProgress(self,new_word):  this function saves users progress in json file
#                                 
# 7)def CheckCounterRunning(self):  we call it to disable buttons as front card is being shown.staticmethod
# 8)def FlipCard(self,new_word):     now again flip the card to back card.
# 9)  def CheckReset(self): this function checks if user has complete all the words or not .this function resets every thing back to as it is is user says yes if not close game window
#10) def GetScore(): this function is to get score of users correctly guessed words
