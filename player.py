from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Black")
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.right(-90)

    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    def goto_start(self):
        self.goto(0, -280)




