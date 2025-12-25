from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html
from ui import UserInterface



question_bank = [Question(html.unescape(question["question"]),question["correct_answer"]) for question in question_data]

quiz = QuizBrain(question_bank)
ui=UserInterface(quiz)





