from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.food_location
    def food_location(self):
        ran_x = random.randint(-260, 260)
        ran_y = random.randint(-260, 260)
        self.goto(ran_x, ran_y)