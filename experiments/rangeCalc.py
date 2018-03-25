
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
        ranges = []
        for i_out in range(self.num_outputs):
            predictedErr = self.regressors[i_out].predict(numpy.array([xWindow]))
            ranges.append(predictedErr * 2)
        return ranges

    def train(self, xWindows, yOutputs, predictions):
        nFlatten = 5
        xWindowArr = numpy.array(xWindows[nFlatten:])
        for i_out in range(self.num_outputs):
            errs = []
            for i in range(nFlatten, yOutputs.__len__()):
                dif = 0.0
                for j in range(nFlatten):
                    real = yOutputs[i-j][i_out]
                    pred = predictions[i-j][i_out]
                    dif += abs(real-pred)
                dif = dif / float(nFlatten)
                errs.append(dif)
            errArr = numpy.array(errs)

            self.regressors[i_out].fit(xWindowArr, errArr)

    def trainUnflat(self, xWindows, yOutputs, predictions):
        xWindowArr = numpy.array(xWindows)
        for i_out in range(self.num_outputs):
            errs = []
            for i in range(yOutputs.__len__()):
                real = yOutputs[i][i_out]
                pred = predictions[i][i_out]
                dif = abs(real-pred)
                errs.append(dif)
            errArr = numpy.array(errs)

            self.regressors[i_out].fit(xWindowArr, errArr)
        

if __name__ == "__main__":
    print(nextPoint())







