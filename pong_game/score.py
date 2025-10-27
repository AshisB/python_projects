from turtle import Turtle


SCORE_Y=150
SCORE_FONT=('Arial',100,'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score_left=0
        self.score_right = 0
        self.ScoreOutput()



    def ScoreUpdate(self,side):
        if side=='l':
            self.score_left+=1
        if side=='r':
            self.score_right+=1

        self.ScoreOutput()

    def ScoreOutput(self):
        self.clear()
        self.goto(-100, SCORE_Y)
        self.write(self.score_left, font=SCORE_FONT)
        self.goto(30, SCORE_Y)
        self.write(self.score_right, font=SCORE_FONT)

    def GameOver(self):
        self.goto(0, 0)
        self.write('Game Over', align='center', font=('Arial', 20, 'normal'))


