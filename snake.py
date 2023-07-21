from turtle import Turtle
POSS = [(0, 0), (-20, 0), (-40, 0)]
HEADING = [ 0, 90, 180, 270]
MOVE_DIS = 20
class Snake:

    def __init__(self):
        self.list = []
        self.create_snake()
        self.head = self.list[0]
    # def __init__(self):
    #     self.list = []
    #
    #     poss = [(0, 0), (-20, 0), (-40, 0)]
    #     for position in poss:
    #         self.t = Turtle("square")
    #         self.t.color("white")
    #         self.t.penup()
    #         self.t.goto(position)
    #         self.list.append(self.t)
    #
    def create_snake(self):
        for position in POSS:
            self.add_seg(position)

    def add_seg(self, position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.list.append(t)

    def extend(self):

        self.add_seg(self.list[-1].position())

    def move(self):
        for poss_index in range(len(self.list) - 1, 0, -1):
            new_x = self.list[poss_index - 1].xcor()
            new_y = self.list[poss_index - 1].ycor()
            self.list[poss_index].goto(new_x, new_y)
        self.head.forward(MOVE_DIS)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset(self):
        for seg in self.list:
            seg.goto(1000, 1000)

        self.list = []
        self.create_snake()
        self.head = self.list[0]
        self.move()
