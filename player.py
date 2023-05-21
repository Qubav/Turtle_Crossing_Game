from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self) -> None:
        super().__init__()

        # executing methods
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.goto(STARTING_POSITION)
    
    def move_forward(self):
        """Method makes turtle go forward for fixed amount of units."""

        self.forward(MOVE_DISTANCE)

    def check_if_turtle_crossed_road(self):
        """Method check if player has crossed road successfully, and returns True if player did or False if player didn't."""

        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def return_to_start(self):
        """Method changes players position to starting position."""

        self.goto(STARTING_POSITION)
