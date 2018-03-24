
import sklearn
from sklearn.ensemble import RandomForestRegressor
import numpy



class Regressor(object):
    # The class "constructor" - It's actually an initializer 
    def __init__(self):
        this.

    def train(xWindows, yOutputs)


    def addPoint(self, point):
        self.points.append(point)
        self.counter += 1

    def nextXWindow(self):
        if self.counter >= WINDOW_SIZE + 1:
            ret = []
            for i in range(WINDOW_SIZE):
                point = self.points[self.counter - i - 1]
                ret.append(point[0])
            return ret
        else:
            return None

    def nextYOutputs(self):
        if self.counter >= WINDOW_SIZE + 1:
            return [self.points[self.counter][0]]
        else:
            return None


# clf = sklearn.svm.SVR(gamma=0.001, C=100.)
clf = RandomForestRegressor()
clf.fit(windows, target)

