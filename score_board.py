from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self) :
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear() #so that score doesnt override
        self.goto(-150,200)
        self.write(f"A:{self.l_score}", align="center",font=("Courier",50,"normal"))
        self.goto(150,200)
        self.write(f" B:{self.r_score}", align="center",font=("Courier",50,"normal"))

   

    def l_point(self):
        self.l_score +=1
        self.update_scoreboard()

    def r_point(self):
        self.r_score +=1
        self.update_scoreboard()

    def game_over_A(self):
        self.color("red")
        self.goto(0, 0)
        self.write(f"Game over\n A win", align="center", font=("Courier",50,"normal")) 

    def game_over_B(self):
        self.color("red")
        self.goto(0, 0)
        self.write(f"Game over\n B win", align="center", font=("Courier",50,"normal"))       