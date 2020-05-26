#Given two ordered pairs calculate the distance between them. Round to two decimal places. This should be easy to do in 0(1) timing.
import math

def distance(x1, y1, x2, y2):
    '''
    the func returns the distance between two pairs of coordinates
    '''
    return round(math.sqrt(pow((x2-x1),2)+pow((y2-y1),2)),2)


print(distance(1,2,3,4))
print(distance.__doc__)