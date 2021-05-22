from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
        self.heading = RIGHT

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle(shape="square")
        new_segment.color("#4CAF50")
        new_segment.shapesize(stretch_wid=0.8, stretch_len=0.8)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
        if position == STARTING_POSITIONS[0]:
            new_segment.color("#2E7D32")
            new_segment.shapesize(stretch_wid=1, stretch_len=1)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        self.head.setheading(self.heading)
        self.head.forward(MOVE)

    def up(self):
        if self.heading != DOWN:
            self.heading = UP

    def down(self):
        if self.heading != UP:
            self.heading = DOWN

    def left(self):
        if self.heading != RIGHT:
            self.heading = LEFT

    def right(self):
        if self.heading != LEFT:
            self.heading = RIGHT

