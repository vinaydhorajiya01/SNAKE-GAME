from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 24, "bold")
SMALL_FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("#4CAF50")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", 
                  align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("#FF5252")
        self.write("GAME OVER!", align=ALIGN, font=FONT)
        self.goto(0, -40)
        self.color("#4CAF50")
        self.write("Press 'R' to Restart", align=ALIGN, font=SMALL_FONT)
        
        if self.score > self.high_score:
            self.high_score = self.score

    def inc_score(self):
        self.score += 1
        self.update_scoreboard()


