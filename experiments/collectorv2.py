import numpy as np
MIN_WINDOWS = 10
WINDOW_SIZE = 10
import xSimData

class Collector(object):


    # The class "constructor" - It's actually an initializer 
    def __init__(self):
        self.columns = 5
        self.points = []
        self.counter = -1

    def addPoint(self, point):
        self.points.append(point)
        self.counter += 1

    def nextXWindow(self):
        if self.counter >= WINDOW_SIZE + 1:
            l = []
            for i in range(WINDOW_SIZE):
                point = self.points[self.counter-i-1]
                print(point)
                l.append(point[1]['mode'])
                l.append(point[1]['orbitAngle'])
                l.append(point[1]['temp'])

            return l
        else:
            return None

    def nextYOutputs(self):
        if self.counter >= WINDOW_SIZE + 1:
            return [self.points[self.counter][1]['temp']]
        else:
            return None



if __name__ == "__main__":
    c = Collector()
    for i in range(100):
        point = xSimData.nextPoint()
        c.addPoint(point)
    print(c.nextXWindow())
    print(c.nextYOutputs())






