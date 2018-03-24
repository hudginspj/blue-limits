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
            l = [point[1]['mode'], point[1]['orbitAngle'], point[1]['temp']]
            for i in range(WINDOW_SIZE):
                point = xSimData.nextPoint()
                l.append(point[1]['mode'])
                l.append(point[1]['orbitAngle'])
                l.append(point[1]['temp'])
            array = np.array(l)

            return array
        else:
            return None

    def nextYOutputs(self):
        if self.counter >= WINDOW_SIZE + 1:
            return [self.points[self.counter][0]]
        else:
            return None



if __name__ == "__main__":
    c = Collector()
    for i in range(100):
        c.addPoint([i])
    print(c.nextXWindow())
    print(c.nextYOutputs())






