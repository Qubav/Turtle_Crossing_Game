import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# setting up screen window
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

# setting up objects for player, cars and scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# setting up screen to listen for key pressing and execute given function
screen.listen()
screen.onkey(player.move_forward, "Up")

# setting up game_is_on value to True
game_is_on = True

# main loop
while game_is_on:

    # time between every screen updated
    time.sleep(0.1)

    # every screen updated there is 1 in 6 chance that new car will be created
    car_manager.create_car()

    # every screen update all cars move for fixed amount of units
    car_manager.move_cars()

    # updating screen
    screen.update()

    # collision detection by comparing coordinates of player to all of the cars
    for car in car_manager.all_cars:

        # reading player's and car's y axis coordinates
        car_y = car.ycor()
        turtle_y = player.ycor()
        
        # checking if player's y coordinate is close to car's y coordinate
        if turtle_y < car_y + 20 and turtle_y > car_y - 20:

            # reading player's and car's x axis coordinates
            car_x = car.xcor()
            turtle_x = player.xcor()

            # checking if player's x coordinate is close to car's x coordinate
            if turtle_x < car_x + 30 and turtle_x > car_x - 30:

                # writing GAME OVER in centre of game screen
                scoreboard.game_over()

                # changing game_is_on value to False so loop ends
                game_is_on = False

    # turtle reaching target detection
    if player.check_if_turtle_crossed_road() is True:

        # if player reached target
        # player returns to start position
        player.return_to_start()

        # cars speed is increased
        car_manager.speed_up_cars()

        # players level is increased by 1
        scoreboard.set_level_up()

        # scoreboard is updated
        scoreboard.update_scoreboard()
    
screen.exitonclick()