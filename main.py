# import random
import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

game_is_on = True
screen = None
snake = None
food = None
scoreboard = None

def setup_screen():
    global screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("#1a1a1a")  # Dark gray background
    screen.tracer(0)
    screen.title("🐍 Snake Game 🍎")
    return screen

def reset_game():
    global snake, food, scoreboard, game_is_on
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    game_is_on = True

def main():
    global game_is_on, screen, snake, food, scoreboard
    screen = setup_screen()
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(reset_game, "r")  # Restart game with 'r' key
    
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        
        # Check for food collision
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.inc_score()
        
        # Check for wall collision
        if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or 
            snake.head.ycor() > 280 or snake.head.ycor() < -280):
            game_is_on = False
            scoreboard.game_over()
        
        # Check for self collision
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
                break

if __name__ == "__main__":
    main()
    screen.exitonclick()

