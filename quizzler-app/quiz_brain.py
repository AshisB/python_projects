import textwrap
from tkinter import *
from ui import THEME_COLOR


class QuizBrain:

    def __init__(self, q_list,window):
        self.window = window
        self.score_text = None
        self.canvas_question_text = None
        self.canvas = None
        self.true_btn_image = None
        self.false_btn_image = None
        self.button_true = None
        self.button_false = None
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None


    def next_question(self):
        try:
            self.button_true.config(state='normal')
            self.button_false.config(state='normal')
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            self.view_modal()
        except IndexError:
            self.canvas.itemconfig(self.canvas_question_text,text=f"Your score is {self.score}/{len(self.question_list)}\nThank You for playing")
            self.button_true.config(state='disabled')
            self.button_false.config(state='disabled')

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            self.canvas.config(bg='green')
            self.canvas.itemconfig(self.score_text,text=f"⭐ {self.score}",fill='white')
        else:
            self.canvas.config(bg='red')
            self.canvas.itemconfig(self.score_text, text=f"⭐ {self.score}", fill='white')

        self.button_true.config(state='disabled')
        self.button_false.config(state='disabled')
        self.window.after(1000,self.next_question)


    def view_modal(self):
        self.current_question = self.question_list[self.question_number]
        self.canvas = Canvas(width=500, height=350, bg=THEME_COLOR)
        self.score_text=self.canvas.create_text(
            470, 20,  # Very close to corner
            text=f"⭐ {self.score}",
            font=('Arial', 16, 'bold'),
            fill='darkgreen',
            anchor='ne'
        )
        self.canvas_question_text=self.canvas.create_text(250, 175, text=f'Question:{self.question_number+1}\n\n{textwrap.fill(self.current_question.text,60)}', font=('Arial', 12, 'bold'))
        self.canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.true_btn_image = PhotoImage(file='./images/true.png')
        self.button_true = Button(image=self.true_btn_image, highlightthickness=0, relief='flat',command=lambda:self.check_answer('True'))
        self.button_true.grid(row=1, column=0)

        self.false_btn_image = PhotoImage(file='./images/false.png')
        self.button_false = Button(image=self.false_btn_image, highlightthickness=0, relief='flat',command=lambda:self.check_answer('False'))
        self.button_false.grid(row=1, column=1)
