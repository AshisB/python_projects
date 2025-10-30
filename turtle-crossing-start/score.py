from turtle import Turtle

SCORE_X=-270
SCORE_Y=270
SCORE_FONT=('Arial',10,'bold')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score=0
        self.level = 1
        self.DisplayOutput()

    def ScoreLogic(self):
        #we will calculate score using colors of cars in other complex level
        pass


    def ScoreUpdate(self):
        self.score+=1
        self.DisplayOutput()


    def LevelUpdate(self):
        self.level+=1
        self.score=0
        self.DisplayOutput()


    def DisplayOutput(self):
        self.clear()
        self.goto(SCORE_X, -SCORE_Y)
        self.write(f'SCORE={self.score}', font=SCORE_FONT)
        self.goto(SCORE_X, SCORE_Y)
        self.write(f'LEVEL={self.level}', font=SCORE_FONT)



    def GameOver(self):
        self.goto(0, 0)
        self.write('Game Over', align='center', font=('Arial', 20, 'normal'))


