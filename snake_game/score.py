from turtle import Turtle

SCORE_POS=(0,260)
SCORE_COLOR='black'
SCORE_FONT=("Arial", 16, "bold")
SCORE_ALIGN='center'

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(SCORE_POS)
        self.color(SCORE_COLOR)
        self.score_count=0
        self.highscore=0
        self.updateScore()


    def scoreCount(self):
        self.score_count+=1
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.write(f'Score={self.score_count},High Score={self.highscore}', align=SCORE_ALIGN, font=SCORE_FONT)

    def hitTheWall(self):
        self.goto(0,0)
        self.write(f'Game Over', align=SCORE_ALIGN, font=SCORE_FONT)

    def resetScore(self):
        if self.score_count>self.highscore:
            self.highscore = self.score_count
        self.score_count=0
        self.updateScore()


