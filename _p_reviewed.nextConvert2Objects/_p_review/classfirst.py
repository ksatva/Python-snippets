class Point(object):
    '''represents a point in a 2d space'''
point1 = Point()
x = point1.x = 3.0
y = point1.y = 4.0
print('(%g, %g)'%(x,y))

import math
distance = math.sqrt(x**2+y**2)
print(distance)

def printpoint(p):
    print('(%g, %g)'%(p.x,p.y))

printpoint(point1)

#------------------------\
#rectangles
class Rectangle(object):
    '''Represents a rectangle

    attribute: width, height, corner'''

box = Rectangle()
box.width=100.0
box.height=200.0
box.corner = Point()
box.corner.x =0.0
box.corner.y=0.0


def findcenter(rect):
    p = Point()
    p.x = rect.corner.x+rect.width/2.0
    p.y = rect.corner.y+rect.height/2.0
    return p

center = findcenter(box)
printpoint(center)
