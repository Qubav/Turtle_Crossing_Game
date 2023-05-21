from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self) -> None:
        self.all_cars: list [Turtle] = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Method has chance 1 in 6 to create new car. Created car is added to attribute list with all cars and performs the same actions as rest."""

        # drawing a random number from 1 to 6
        random_chance = random.randint(1, 6)

        # if random_chance is equal to 1 new car is created and added
        if random_chance == 1:

            # creating new Turtle object that will be treated like car
            new_car = Turtle("square")

            # setting up new_car's attributes
            new_car.penup()
            new_car.setheading(0)
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid = 1, stretch_len = 2)

            # drawing random y coordinate for car's starting location
            random_y = random.randint(-250, 250)

            # setting up car's starting location
            new_car.goto(300, random_y)

            # appending new car to car list attribute
            self.all_cars.append(new_car)

    def move_cars(self):
        """Method makes all of the cars move forward a given number of units."""

        # looping for all cars in cars list
        for car in self.all_cars:

            # making car move
            car.backward(self.move_distance)
    
    def speed_up_cars(self):
        """Increasing single car move distance by fixed amount of units."""

        self.move_distance += MOVE_INCREMENT