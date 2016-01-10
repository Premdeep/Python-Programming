# coordinates class in python

import math

class coordinates(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,other):
        return math.sqrt(( self.x-other.x)**2 + (self.y-other.y))


import math

def sq(x):
    return x*x


class Coordinates(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"
    def distance(self,other):
        return math.sqrt(sq(self.x - other.x)
                         + sq(self.y - other.y))



class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y
    
    def __eq__(self,other):
        return (self.x == other.x) and (self.y == other.y)

    def __repr__(self):        
        return "Coordinate("+str(self.x)+", "+str(self.y)+")"

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
