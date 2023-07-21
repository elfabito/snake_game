from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.h_score = 0
        with open("high_score.txt", mode="r") as file:
            self.h_score = int(file.read())

        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def high_score(self):

        self.goto(0, 270)
        if self.score > self.h_score:
            self.h_score = self.score
        self.update_score()
        with open("high_score.txt", mode="w") as file:
            file.write(f"{self.h_score}")
    def update_score(self):
        self.clear()
        self.goto(0, 270)


        self.write(f"Score : {self.score} , High-Score : {self.h_score}", True, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        self.score = 0
        self.update_score()
    def raise_score(self):

        self.goto(0, 270)
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.home()
    #     self.write(f"Score : {self.score}", True, align=ALIGNMENT, font=FONT)




