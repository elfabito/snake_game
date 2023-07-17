from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}", True, align=ALIGNMENT, font=FONT)
    def raise_score(self):
        self.clear()
        self.goto(0, 270)
        self.score += 1
        self.update_score()

    def game_over(self):
        self.home()
        self.write(f"Score : {self.score}", True, align=ALIGNMENT, font=FONT)



