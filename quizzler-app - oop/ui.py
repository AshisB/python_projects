from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#d3d3d3"


class UserInterface:
    def __init__(self, quiz: QuizBrain):
        self.window = Tk()
        self.window.title('Quizzer Trivia')
        self.window.config(padx=20, pady=20, bg='#375362')
        self.question_number = 0
        self.score = 0
        self.quiz = quiz
        self.view_modal()
        self.get_next_question()
        self.window.mainloop()

    def view_modal(self):
        self.canvas = Canvas(width=500, height=350, bg=THEME_COLOR)
        self.score_text = self.canvas.create_text(
            470, 20,  # Very close to corner
            text=f"⭐ {self.score}",
            font=('Arial', 16, 'bold'),
            fill='darkgreen',
            anchor='ne'
        )
        self.canvas_question_text = self.canvas.create_text(250, 175, width=450, text='', font=('Arial', 12, 'bold'))
        self.canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.true_btn_image = PhotoImage(file='./images/true.png')
        self.button_true = Button(image=self.true_btn_image, highlightthickness=0, relief='flat',
                                  command=lambda: self.get_check_answer('True'))
        self.button_true.grid(row=1, column=0)

        self.false_btn_image = PhotoImage(file='./images/false.png')
        self.button_false = Button(image=self.false_btn_image, highlightthickness=0, relief='flat',
                                   command=lambda: self.get_check_answer('False'))
        self.button_false.grid(row=1, column=1)

    def get_next_question(self):
        self.canvas.config(bg=THEME_COLOR)

        if self.quiz.still_has_question():
            self.button_true.config(state='normal')
            self.button_false.config(state='normal')

            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_question_text, text=f'Thank you for playing this game.\nYour total score is {self.quiz.score}/{self.quiz.question_number}')

    def get_check_answer(self, answer):
        checked_answer = self.quiz.check_answer(answer)
        if checked_answer == True:
            self.canvas.config(bg='green')
            self.canvas.itemconfig(self.score_text, text=f"⭐ {self.quiz.score}", fill='white')
        else:
            self.canvas.config(bg='red')
            self.canvas.itemconfig(self.score_text, text=f"⭐ {self.quiz.score}", fill='white')

        self.button_true.config(state='disabled')
        self.button_false.config(state='disabled')
        self.window.after(1000, self.get_next_question)
