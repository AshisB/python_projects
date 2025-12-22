from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from tkinter import *
import html

window=Tk()
window.title('Quizzer Trivia')
window.config(padx=20,pady=20,bg='#ffffff')

question_bank = [Question(html.unescape(question["question"]),question["correct_answer"]) for question in question_data]
print(question_bank)
quiz = QuizBrain(question_bank,window)
quiz.view_modal()





window.mainloop()




