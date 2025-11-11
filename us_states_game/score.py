from turtle import Turtle,Screen

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('blue')
        self.score=0
        self.attempt=0
        self.UpdateScore()
       
    
    def update(self):
        self.score+=1
        self.UpdateScore()
      

    def UpdateAttempt(self):
        self.attempt+=1   
        self.UpdateScore()
      

    def UpdateScore(self):
        self.clear()
        self.goto(250, 250)
        self.write(f'{self.attempt}/50 | Score={self.score}', align='center', font=('Arial', 15, 'bold'))   

    def DisplayScoreFinal(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"You have scored {self.score} out of 50. \n{'Congratulations!!!' if self.score > 45 else 'Try Again!Find remaining state csv to read remaining state'}", 
           align='center', font=('Arial', 11, 'bold'))
        