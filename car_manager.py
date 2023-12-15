from turtle import Turtle

Colors = ["red", "black", "orange", "yellow", "green", "blue", "purple"]
import random


class Cars(Turtle):
    def __init__(self):
        self.all_car = []

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(Colors[random.randint(0, 6)])
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_car.append(new_car)

    def move_cars(self):
        for car in self.all_car:
            car.backward(5)


