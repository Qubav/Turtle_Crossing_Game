from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self) -> None:
        super().__init__() 
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.goto(STARTING_POSITION)
    
    def move_forward(self):

        self.forward(MOVE_DISTANCE)

    def check_if_turtle_crossed_road(self):

        if self.ycor() > 285:
            return True

    def return_to_start(self):

        self.goto(STARTING_POSITION)
