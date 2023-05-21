from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCOREBOARD_POSITION = (-265, 250)

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()

        # setting up variable value that stores level to 1
        self.level = 1

        # executing starting methods
        self.penup()
        self.hideturtle()
        self.goto(SCOREBOARD_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Method updates scoreboard."""

        self.clear()
        self.write(f"Level: {self.level}", align = "left", font = FONT)

    def set_level_up(self):
        """Method increases player score value by 1."""

        self.level += 1
    
    def game_over(self):
        """Method writes \"GAME OVER\" in centre of the window and clears player score."""

        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align = "center", font = FONT)
        