

from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.loop = False
        self.loopCount = 0
        
        self.yCord = coordinates[1]
        self.xCord = coordinates[0]
        self.goto(self.xCord, self.yCord)
        
    def go_down(self):
        self.yCord -= 20
        self.goto(self.xCord, self.yCord)
    
    def go_up(self):
        self.yCord += 20
        self.goto(self.xCord, self.yCord)

    def go_up_loop(self):
        self.loop = True
        while self.loop:
            self.loopCount += 1
            self.yCord += 20
            self.goto(self.xCord, self.yCord)
            if self.loopCount >= 5:
                self.loop = False

    def go_down_loop(self):
        self.loop = True
        while self.loop:
            self.yCord -= 20
            self.loopCount += 1
            self.goto(self.xCord, self.yCord)
            if self.loopCount >= 5:
                self.loop = False

    
    def loop_end(self):
        self.loop = False







