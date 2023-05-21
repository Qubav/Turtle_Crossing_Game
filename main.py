import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_forward, "Up")
# screen.onkey()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_cars()
    screen.update()

    # collision detection 
    for car in car_manager.all_cars:
        car_y = car.ycor()
        turtle_y = player.ycor()

        if turtle_y < car_y + 20 and turtle_y > car_y - 20:
            car_x = car.xcor()
            turtle_x = player.xcor()

            if turtle_x < car_x + 30 and turtle_x > car_x - 30:
                game_is_on = False

    # turtle reaching goal detection

    if player.check_if_turtle_crossed_road() is True:
        player.return_to_start()
        car_manager.speed_up_cars()
    

screen.exitonclick()