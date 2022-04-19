from turtle import Turtle
MOVE_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.location = -40
        self.ls = []
        for x in range(0, 3):
           self.add_s(self.location, 0)
           self.location += 20
        self.head = self.ls[0]
    def add_s(self, locationX, locationY):
        self.s = Turtle()
        self.s.penup()
        self.s.shape("square")
        self.s.color("white")
        self.s.goto(locationX, locationY)
        self.ls.append(self.s)
    def extend(self):
        self.add_s(self.ls[-1].xcor(),self.ls[-1].ycor())


    def move(self):
        for seq_num in range(len(self.ls) - 1, 0, -1):
            new_x =  self.ls[seq_num - 1].xcor()
            new_y =  self.ls[seq_num - 1].ycor()
            self.ls[seq_num].goto(new_x, new_y)
        self.ls[0].forward(MOVE_DIST)
    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset(self):
        for s in self.ls:
            s.goto(1000, 1000)
        self.ls.clear()
        for x in range(0, 3):
            self.add_s(self.location, 0)
            self.location += 20
        self.head = self.ls[0]