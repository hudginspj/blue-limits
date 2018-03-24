
import sklearn
from sklearn.ensemble import RandomForestRegressor
import numpy



class Ranger(object):
    # The class "constructor" - It's actually an initializer 
    def __init__(self, num_outputs):
        self.num_outputs = num_outputs
        self.regressors = []
        for i in range(num_outputs):
            self.regressors.append(RandomForestRegressor())

    def calcRanges(self, xWindow):
        yOutputs = []
        for i_out in range(self.num_outputs):
            # prediction = self.regressors[i_out].predict(xWindow)
            yOutputs.append(0.5)
        return yOutputs

    def train(self, xWindows, yOutputs):
        xWindowArr = numpy.array(xWindows)
        for i_out in range(self.num_outputs):
            ys = []
            for i in range(yOutputs.__len__()):
                ys.append(yOutputs[i][i_out])
            yArr = numpy.array(ys)
            self.regressors[i_out].fit(xWindowArr, yArr)
        

if __name__ == "__main__":
    print(nextPoint())







