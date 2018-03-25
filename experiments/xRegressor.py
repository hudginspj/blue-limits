
import sklearn
from sklearn.neural_network import MLPRegressor

from sklearn.ensemble import RandomForestRegressor
from sklearn import svm
import numpy



class Regressor(object):
    try:
        # The class "constructor" - It's actually an initializer
        def __init__(self, num_outputs):
            self.num_outputs = num_outputs
            self.regressors = []
            for i in range(num_outputs):
                self.regressors.append(self.makeRegressor())

        def predict(self, xWindow):
            yOutputs = []
            for i_out in range(self.num_outputs):
                prediction = self.regressors[i_out].predict(numpy.array([xWindow]))
                yOutputs.append(prediction[0])
            return yOutputs

   

        def train(self, xWindows, yOutputs):
            xWindowArr = numpy.array(xWindows)
            for i_out in range(self.num_outputs):
                ys = []
                for i in range(yOutputs.__len__()):
                    ys.append(yOutputs[i][i_out])
                yArr = numpy.array(ys)
                self.regressors[i_out].fit(xWindowArr, yArr)
            # assert yOutputs[0].__len__() >= 1
            # assert xWindows[0].__len__() >= 1

        def makeRegressor(self):
            # r = sklearn.neighbors.KNeighborsRegressor()
            r = sklearn.neural_network.MLPRegressor()
            # r = svm.SVR(gamma=0.0001, C= 100)
            r = RandomForestRegressor()
            return r
    except Exception as e:
        pass




# # clf = sklearn.svm.SVR(gamma=0.001, C=100.)
# clf = RandomForestRegressor()
# clf.fit(windows, target)

