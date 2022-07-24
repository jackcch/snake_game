from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align=ALIGNMENT, font=FONT)

