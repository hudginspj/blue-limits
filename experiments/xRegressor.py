
import sklearn
from sklearn.ensemble import RandomForestRegressor
import numpy



class Regressor(object):
    # The class "constructor" - It's actually an initializer 
    def __init__(self, num_outputs):
        self.num_outputs = num_outputs
        self.regressors = []
        for i in range(num_outputs):
            self.regressors.append(self.makeRegressor())

    def predict(self, xWindows):
        assert xWindows[0].__len__() >= 1
        return [1.0, -5.0]

    def train(self, xWindows, yOutputs):
        xWindowArr = numpy.array(xWindows)
        for i_out in range(num_outputs):
            ys = []
            for i in range(yOutputs.__len__()):
                ys.append(yOutputs[i][out])
            yWindowArr = numpy.array(ys)
            regressors[i_out].fit(xWindows, ys)]
        # assert yOutputs[0].__len__() >= 1
        # assert xWindows[0].__len__() >= 1

    def makeRegressor(self):
        r = RandomForestRegressor()
        return r

    def addPoint(self, point):
        self.points.append(point)
        self.counter += 1

#     def nextXWindow(self):
#         if self.counter >= WINDOW_SIZE + 1:
#             ret = []
#             for i in range(WINDOW_SIZE):
#                 point = self.points[self.counter - i - 1]
#                 ret.append(point[0])
#             return ret
#         else:
#             return None

#     def nextYOutputs(self):
#         if self.counter >= WINDOW_SIZE + 1:
#             return [self.points[self.counter][0]]
#         else:
#             return None


# # clf = sklearn.svm.SVR(gamma=0.001, C=100.)
# clf = RandomForestRegressor()
# clf.fit(windows, target)

