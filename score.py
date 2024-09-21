from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.total = 0
        self.penup()
        self.color("white")
        self.goto(0, 275)
        self.hideturtle()
        self.display()

    def count(self):
        self.total = self.total + 1
        self.clear()
        self.display()

    def display(self):
        self.goto(0, 275)
        self.write(f"Score: {self.total}", move=True, align="center", font=('Arial', 14, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=True, align="center", font=('Arial', 14, 'normal'))
