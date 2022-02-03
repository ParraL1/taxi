#Name: Lilliana Parra
#Github username: ParraL1
#Date: 2/1/2022
#Description: reading the odometer and x,y coordinates of a cab

class Taxicab:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y
        self.odometer = 0
#starting point


    def move_x(self, value):
        self.x_coord += value
        self.odometer += abs(value)

    def move_y(self, value):
        self.y_coord += value
        self.odometer += abs(value)

#read x,y coordinates
    def get_x_coord(self):
        return self.x_coord

    def get_y_coordinate(self):
        return self.y_coord

#end odometer reading
    def get_odometer(self):
        return self.odometer