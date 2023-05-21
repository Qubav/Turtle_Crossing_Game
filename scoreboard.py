from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCOREBOARD_POSITION = (-265, 250)

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.level = 1

        self.penup()
        self.hideturtle()
        self.goto(SCOREBOARD_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align = "left", font = FONT)

    def set_level_up(self):

        self.level += 1
    
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVEr", align = "center", font = FONT)
        