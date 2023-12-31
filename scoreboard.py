from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, -280)
        self.update_score()
        self.move_speed = 0.1

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Arial", 24, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))

