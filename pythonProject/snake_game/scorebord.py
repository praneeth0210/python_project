from turtle import Turtle


class Scorebord(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score+=1
        self.clear()

        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))

    def Game_over(self):
        self.goto(0,0)
        self.write("Game over", align="center", font=("Arial", 15, "normal"))




