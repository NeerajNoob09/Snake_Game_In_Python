from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.color("blue")
        self.hideturtle()
        self.update_scorecard()

    def update_scorecard(self):
        self.write(f"Score: {self.score}", False, "center", ("Arial", 18, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", ("Arial", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scorecard()
