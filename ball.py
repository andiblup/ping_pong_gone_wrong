
from turtle import Turtle
import random
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.predefined_colors = ["green", "blue", "yellow", "orange", "purple", "ivory", "grey", "pink", "cyan4", "purple1", "red", "LimeGreen", "brown", "DeepSkyBlue"]
        self.speed("fastest")
        self.shape("circle")
        self.color("limegreen")
        self.penup()
        ##
        #self.setheading(random.randint(0, 359)#
        # random startrichtung / positiv oder negativ für x und y
        self.startList = [1, 2]
        self.startX = random.choice(self.startList)
        self.startY = random.choice(self.startList)
        ###
        self.x_move = 10
        self.y_move = 10
        
        self.move_speed = 0.035
        ###
        if self.startX == 1:
            self.x_move *= 1
        elif self.startX == 2:
            self.x_move *= -1
            
        if self.startY == 1:
            self.y_move *= 1
        elif self.startY == 2:
            self.y_move *= -1
        
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.92
        self.color(self.predefined_colors[random.randint(0, 13)])
        

    
    def restart(self):
        a = self.xcor()
        self.hideturtle()
        self.goto(0, 0)
        self.move_speed = 0.05
        self.showturtle()
        print("3")
        time.sleep(0.2)
        print("2")
        time.sleep(0.2)
        print("1")
        time.sleep(0.2)
        print("GO")
        if a < 0:
            self.x_move = -10
        elif a > 0:
            self.x_move = 10
        self.y_move = random.randint(-10, 10)
    
    def stop_move(self):
        self.x_move = 0
        self.y_move = 0
    
    def get_ycor(self):
       return self.ycor()

    def get_xcor(self):
       return self.xcor()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    